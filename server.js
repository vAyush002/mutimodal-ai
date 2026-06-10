#!/usr/bin/env node
/**
 * Simple HTTP Server for Damage Prompt Generator
 * 
 * Setup:
 *   npm install express
 * 
 * Run:
 *   node server.js
 * 
 * Then open: http://localhost:8000/damage-prompt-generator.html
 */

const express = require('express');
const path = require('path');
const open = require('open');

const app = express();
const PORT = 8000;

// Serve static files from current directory
app.use(express.static(path.join(__dirname)));

// No caching
app.use((req, res, next) => {
    res.set('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
    res.set('Pragma', 'no-cache');
    res.set('Expires', '0');
    next();
});

// Start server
app.listen(PORT, () => {
    console.log('=============================================');
    console.log('🎨 Damage Prompt Generator Server');
    console.log('=============================================');
    console.log(`✓ Server running at: http://localhost:${PORT}`);
    console.log(`✓ Open in browser: http://localhost:${PORT}/damage-prompt-generator.html`);
    console.log(`✓ Press Ctrl+C to stop`);
    console.log('=============================================');
    
    // Try to open in browser automatically
    try {
        open(`http://localhost:${PORT}/damage-prompt-generator.html`);
    } catch(err) {
        // Silently fail if open doesn't work
    }
});
