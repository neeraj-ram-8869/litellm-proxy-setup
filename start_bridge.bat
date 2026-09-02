@echo off
title Claude-NVIDIA Local Bridge
color 0A
echo ========================================================
echo   Starting LiteLLM Proxy for Claude Desktop & Filesystem
echo ========================================================

set "NVIDIA_NIM_API_KEY=YOUR_NVIDIA_API_KEY_HERE"
cd /d "%~dp0"

echo [ + ] Launching LiteLLM with config.yaml...
litellm --config config.yaml --port 4000 --num_workers 2

pause
