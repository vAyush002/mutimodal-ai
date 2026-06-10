@echo off
title Damage Prompt Generator

echo ============================================
echo Starting Damage Prompt Generator...
echo ============================================
echo.
echo Open this in your browser:
echo http://localhost:8080/damage-prompt-generator.html
echo.

python -m http.server 8080

pause