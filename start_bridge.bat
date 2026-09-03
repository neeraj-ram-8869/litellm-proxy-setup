@echo off
title Claude-NVIDIA Local Bridge
color 0A
echo ========================================================
echo   Starting LiteLLM Proxy for Claude Desktop & Filesystem
echo ========================================================

set "NVIDIA_NIM_API_KEY=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"
cd /d C:\Users\ACER

echo [ + ] Launching LiteLLM with config.yaml...
litellm --config config.yaml --port 4000 --num_workers 2

pause
