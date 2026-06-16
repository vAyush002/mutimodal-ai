#!/usr/bin/env python3
"""
Damage Verification Assistant — Streamlit Cloud app.

Upload a photo of a delivered product and a vision model produces an objective
damage assessment for a human claims/returns reviewer: what the product is, what
damage is visible, how severe it is, whether the damage pattern looks consistent
with genuine shipping/handling, and a recommendation (approve / human review /
request more evidence).

This is a decision-support tool for reviewers. It does NOT make automated
approval decisions and cannot definitively prove an image is authentic or
manipulated — every output is advisory and meant to be checked by a person.

Providers are swappable: Groq, OpenAI, and Anthropic (Claude). Each user supplies
their own API key in the sidebar; keys are held only for the duration of the
request and never stored server-side.

Deploy on Streamlit Cloud with this file as the "Main file path".
"""

import base64

import streamlit as st

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

st.set_page_config(page_title="Damage Verification Assistant", page_icon="🔍", layout="centered")

GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# Provider -> list of suggested vision-capable models. The first entry is the
# default. Users can also type a custom model id.
PROVIDER_MODELS = {
    "Anthropic (Claude)": [
        "claude-opus-4-8",
        "claude-sonnet-4-6",
        "claude-haiku-4-5",
    ],
    "OpenAI": [
        "gpt-4o",
        "gpt-4o-mini",
    ],
    "Groq": [
        "meta-llama/llama-4-scout-17b-16e-instruct",
    ],
}

PROVIDER_KEY_HELP = {
    "Anthropic (Claude)": ("console.anthropic.com", "https://console.anthropic.com/settings/keys"),
    "OpenAI": ("platform.openai.com", "https://platform.openai.com/api-keys"),
    "Groq": ("console.groq.com", "https://console.groq.com/keys"),
}

SYSTEM_PROMPT = """\
You are a shipping-and-logistics damage assessor. You help a human returns/claims \
reviewer evaluate a photo that a customer submitted with a damage claim for a \
delivered product. Your job is to describe what you see objectively and flag \
anything that warrants a closer look — not to make the final decision.

Analyze the image and respond in Markdown with exactly these sections:

### 1. Product
What the product appears to be (type, brand if legible, packaging material).

### 2. Visible damage
A bullet list of each distinct issue you can see, with its location. If you see no \
damage, say so plainly.

### 3. Severity
One of: None / Minor / Moderate / Severe — with a one-line justification.

### 4. Consistency
Assess whether the damage pattern looks consistent with genuine courier/shipping/\
handling/delivery mishandling (crushing, drops, punctures, water, stacking), a \
pre-existing manufacturing defect, or normal wear. If anything looks inconsistent \
or staged, say what and why. State explicitly that you CANNOT definitively detect \
digital photo manipulation — this is an advisory observation for a human, not proof.

### 5. Recommendation
One of: Approve replacement/refund / Send to human review / Request more evidence — \
with reasoning. When evidence is ambiguous or the photo is unclear, prefer "Send to \
human review" or "Request more evidence" over a definitive call.

### 6. Confidence
Low / Medium / High, and what would raise it (e.g., a clearer photo, the shipping \
box, a timestamp).

Be concise and factual. Do not invent details you cannot see in the image."""

USER_INSTRUCTION = (
    "Assess this product photo submitted with a damage claim. Follow the six-section "
    "format exactly."
)


# ---------------------------------------------------------------------------
# Provider calls
# ---------------------------------------------------------------------------


def _user_text(context: str) -> str:
    text = USER_INSTRUCTION
    if context.strip():
        text += f"\n\nReviewer-supplied context: {context.strip()}"
    return text


def assess_anthropic(api_key: str, model: str, image_b64: str, media_type: str, context: str) -> str:
    import anthropic

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_b64,
                        },
                    },
                    {"type": "text", "text": _user_text(context)},
                ],
            }
        ],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def assess_openai_compatible(
    api_key: str, model: str, image_b64: str, media_type: str, context: str, base_url: str | None
) -> str:
    """Works for both OpenAI and Groq — Groq exposes an OpenAI-compatible API."""
    from openai import OpenAI

    client = OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        max_tokens=1500,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": _user_text(context)},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{media_type};base64,{image_b64}"},
                    },
                ],
            },
        ],
    )
    return response.choices[0].message.content or ""


def run_assessment(
    provider: str, api_key: str, model: str, image_bytes: bytes, media_type: str, context: str
) -> str:
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    if provider == "Anthropic (Claude)":
        return assess_anthropic(api_key, model, image_b64, media_type, context)
    if provider == "OpenAI":
        return assess_openai_compatible(api_key, model, image_b64, media_type, context, base_url=None)
    if provider == "Groq":
        return assess_openai_compatible(api_key, model, image_b64, media_type, context, base_url=GROQ_BASE_URL)
    raise ValueError(f"Unknown provider: {provider}")


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

st.title("🔍 Damage Verification Assistant")
st.caption(
    "Decision support for returns/claims reviewers. Upload a delivered-product photo and "
    "a vision model describes the damage, rates severity, and recommends a next step. "
    "**Every output is advisory — a human makes the final call.**"
)

with st.sidebar:
    st.header("Settings")
    provider = st.selectbox("Provider", list(PROVIDER_MODELS.keys()))

    model_choice = st.selectbox("Model", PROVIDER_MODELS[provider] + ["Custom…"])
    if model_choice == "Custom…":
        model = st.text_input("Custom model id", value=PROVIDER_MODELS[provider][0])
    else:
        model = model_choice

    site, url = PROVIDER_KEY_HELP[provider]
    api_key = st.text_input("API key", type="password", help=f"Get a key at {site}")
    st.caption(f"Need a key? [{site}]({url}) — keys are used only for your request, never stored.")

uploaded = st.file_uploader("Product photo", type=["jpg", "jpeg", "png", "webp", "gif"])
context = st.text_area(
    "Optional context for the reviewer",
    placeholder="e.g. Customer reports the box arrived crushed; ordered a glass jar of honey.",
    height=80,
)

if uploaded is not None:
    st.image(uploaded, caption="Submitted photo", use_container_width=True)

assess = st.button("Assess damage", type="primary", disabled=uploaded is None)

if assess:
    if not api_key.strip():
        st.error("Please enter your API key in the sidebar.")
    elif not model.strip():
        st.error("Please choose or enter a model in the sidebar.")
    else:
        media_type = uploaded.type or "image/jpeg"
        try:
            with st.spinner(f"Assessing with {provider} ({model})…"):
                result = run_assessment(
                    provider, api_key.strip(), model.strip(), uploaded.getvalue(), media_type, context
                )
            st.markdown("## Assessment")
            st.markdown(result)
            st.download_button("Download assessment (.md)", result, file_name="damage_assessment.md")
            st.info(
                "This assessment is advisory and may be wrong. It cannot prove a photo is "
                "authentic or edited. A human reviewer should confirm before any payout."
            )
        except Exception as exc:  # noqa: BLE001 — surface any provider/SDK error to the user
            st.error(f"Assessment failed: {exc}")
            st.caption("Check that the API key is valid, has credit, and the model supports image input.")
