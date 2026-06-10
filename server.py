#!/usr/bin/env python3
"""
Simple HTTP Server for Damage Prompt Generator
Run: python server.py
Then open: http://localhost:8000/damage-prompt-generator.html
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

def start_server():
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("🎨 Damage Prompt Generator Server")
        print("=" * 60)
        print(f"✓ Server running at: http://localhost:{PORT}")
        print(f"✓ Open in browser: http://localhost:{PORT}/damage-prompt-generator.html")
        print(f"✓ Press Ctrl+C to stop")
        print("=" * 60)
        
        try:
            webbrowser.open(f"http://localhost:{PORT}/damage-prompt-generator.html")
        except:
            pass
        
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
