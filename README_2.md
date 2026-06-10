# 🎨 Damage Prompt Generator — Setup & Run

Small web app that analyzes an uploaded image (using the Groq vision API) and generates realistic, randomized "damage" prompts (cracks, erosion, burn, dents, holes) you can paste into image generators.

## Requirements
- Browser (Chrome/Firefox/Edge)
- One of: Node.js (>=12) or Python 3
- (Optional) Groq API key to enable AI analysis

## Quick: open directly
Open `damage-prompt-generator.html` in your browser (double-click or right‑click → Open with → Browser). This works without running a local server but some browsers restrict file APIs when opened from `file://`.

## Run as a local server (recommended)

Node (recommended if you have Node):

```bash
npm install
npm start
```

This runs `server.js` and serves the project at:

```
http://localhost:8000/damage-prompt-generator.html
```

Python (quick static server):

```bash
# from project root
python -m http.server 8000
# or, to match included run.bat, use 8080
python -m http.server 8080
```

Then open:

```
http://localhost:8000/damage-prompt-generator.html
http://localhost:8080/damage-prompt-generator.html
```

Python server script (automatically opens browser):

```bash
python server.py
# opens http://localhost:8000/damage-prompt-generator.html
```

Windows helper:

```
run.bat
# This runs: python -m http.server 8080
```

## Get a Groq API Key (optional but enables AI analysis)
1. Create an account at https://console.groq.com
2. Create an API key in the dashboard
3. Paste the key into the top API Key field in the app UI

## How to use the UI
1. Paste your Groq API key (optional)
2. Upload an image (JPG/PNG recommended, <5MB)
3. Click "Generate" — the app analyzes the image and produces a damage prompt
4. Click "Copy to Clipboard" and paste into your image generator

## File Summary (project root)
```
damage-prompt-generator.html
package.json
server.js          ← Node static server (http://localhost:8000)
server.py          ← Python server (http://localhost:8000)
run.bat            ← Windows helper (starts HTTP server on 8080)
README_2.md        ← This file
VSCODE_QUICKSTART.md
```

## Troubleshooting
- "API Error": verify your Groq API key and internet connection
- Image not loading: try JPG/PNG and smaller file sizes
- Node errors: run `npm install` then `npm start`
- Python errors: ensure `python --version` shows Python 3

## Notes
- `server.js` uses port `8000` and will attempt to open your browser automatically
- `run.bat` launches a Python simple server on port `8080` (Windows convenience)

Enjoy creating realistic damage prompts! 🎨
