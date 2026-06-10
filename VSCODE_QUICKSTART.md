# 🚀 VS Code Quick Start

## 5-Minute Setup in VS Code

### Step 1: Get Groq API Key (1 min)
1. Go to https://console.groq.com
2. Click "Sign up" (free)
3. Go to "API Keys" section
4. Click "Create API Key"
5. Copy the key to clipboard

### Step 2: Open Files in VS Code (1 min)

1. **Open VS Code**
2. **File** → **Open Folder** → Select your project folder
3. You should see:
   - `damage-prompt-generator.html` ← The main app
   - `README.md` ← Instructions
   - `server.py` ← Python server script
   - `server.js` ← Node.js server script (optional)

### Step 3: Run the App (3 choices - pick ONE)

#### ✅ EASIEST - Live Server Extension (Recommended for VS Code)

1. Go to VS Code Extensions (left sidebar, 4 squares icon)
2. Search: `Live Server`
3. Install the one by **Ritwick Dey**
4. Right-click `damage-prompt-generator.html`
5. Select **"Open with Live Server"**
6. Browser opens automatically! 🎉

---

#### Option 2 - Python Server (Built-in)

If you have Python installed:

1. Open VS Code Terminal: **Ctrl+`** (backtick)
2. Type: `python server.py` (or `python3 server.py`)
3. Press Enter
4. Wait for message: "Server running at: http://localhost:8000"
5. Click the link in terminal OR open: http://localhost:8000/damage-prompt-generator.html

---

#### Option 3 - Node.js Server

If you have Node.js installed:

1. Open VS Code Terminal: **Ctrl+`**
2. Type: `npm install express open`
3. Type: `node server.js`
4. Browser opens automatically

---

### Step 4: Use the App

1. **Paste API Key** into the app
2. **Upload Image** - click button or drag-drop
3. **Click "Generate Damage Prompt"**
4. **Wait 3-5 seconds** while it analyzes
5. **Copy Prompt** with the button
6. **Paste anywhere** - Midjourney, DALL-E, etc.

---

## Random Damage Each Time!

Every time you click "Generate", you get different random combinations:

```
Random combination example 1:
- severe fractured cracks
- moderate corroded erosion  
- light gaping holes

Random combination example 2 (next click):
- extreme charred burn
- moderate dented crushing
- light weathered erosion
```

The AI analyzes YOUR image, so each one is unique to what you uploaded.

---

## What You're Using

| File | Purpose |
|------|---------|
| `damage-prompt-generator.html` | The actual app (everything in ONE file) |
| `server.py` | Python server (optional, for local testing) |
| `server.js` | Node server (optional, for local testing) |
| `README.md` | Full documentation |

---

## Common Issues & Fixes

### "Module 'X' not found" (Python/Node)
→ Just use **Live Server** extension instead. No modules needed.

### API Key shows "error"
→ Double-check you copied it correctly from groq.com
→ Check you have free credits remaining

### Image won't load
→ Try JPG or PNG format
→ Make sure file is less than 5MB

### Server won't start
→ Close any other apps using port 8000
→ Or use Live Server extension (easier)

---

## VS Code Tips

**Hot Reload**: When you edit files, Live Server auto-reloads your browser

**Terminal Keyboard Shortcut**: `Ctrl+`  (backtick) opens terminal

**Quick Open**: `Ctrl+P` to jump to files quickly

**Extensions**: `Ctrl+Shift+X` to open Extensions sidebar

---

## Next Steps

1. Create amazing damaged textures
2. Use prompts with: Midjourney, DALL-E, Stable Diffusion
3. Iterate - upload different images, generate multiple times
4. Share your creations!

---

Happy generating! 🎨
