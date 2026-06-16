# 🔍 Damage Verification Assistant

A Streamlit app that helps a returns/claims reviewer evaluate product photos
submitted with damage claims. Upload a photo of a delivered product and a vision
model produces an objective assessment:

1. **Product** — type, brand, packaging
2. **Visible damage** — itemized, with locations
3. **Severity** — None / Minor / Moderate / Severe
4. **Consistency** — does the damage look like genuine shipping/handling damage, a
   manufacturing defect, or normal wear? (advisory — it cannot definitively detect
   photo manipulation)
5. **Recommendation** — Approve / Send to human review / Request more evidence
6. **Confidence** — and what would raise it

> This is **decision support for a human reviewer**. It does not make automated
> approval decisions and cannot prove an image is authentic or edited. Treat every
> output as advisory.

## Multi-provider

Pick your provider in the sidebar and paste your own API key (used only for your
request, never stored):

| Provider | Default model | Get a key |
|----------|---------------|-----------|
| Anthropic (Claude) | `claude-opus-4-8` | console.anthropic.com |
| OpenAI | `gpt-4o` | platform.openai.com |
| Groq | `meta-llama/llama-4-scout-17b-16e-instruct` | console.groq.com |

You can also type a custom model id.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Cloud

1. Push this repo to GitHub.
2. On share.streamlit.io, set **Main file path** to `streamlit_app.py`.
3. Reboot the app.

`requirements.txt` installs `streamlit`, `anthropic`, and `openai`.
