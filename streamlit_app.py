#!/usr/bin/env python3
"""
Streamlit Cloud entry point for the Damage Prompt Generator.

This wraps the existing static page (damage-prompt-generator.html) and renders
it inside Streamlit. All logic stays client-side: the page calls the Groq API
directly from the browser using the API key the user types in.

Deploy on Streamlit Cloud with this file as the "Main file path".
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Damage Prompt Generator", page_icon="🎨", layout="centered")

HTML_FILE = Path(__file__).parent / "damage-prompt-generator.html"

html = HTML_FILE.read_text(encoding="utf-8")

# Render the full page inside Streamlit. height must be tall enough to show the
# whole form without an inner scrollbar feeling cramped; scrolling=True is a
# safety net for smaller screens.
components.html(html, height=1100, scrolling=True)
