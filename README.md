# LiteLLM Proxy Setup for Claude / NVIDIA NIM

This repository contains the necessary configuration files and startup script to run a local LiteLLM proxy bridge, connecting applications (like Claude Desktop or open-source web UIs) to NVIDIA NIM models.

## Features
* Preconfigured config.yaml to alias Anthropic models (e.g., claude-opus-4.8-20260528) to NVIDIA Nemotron.
* Configured to drop unsupported parameters (reasoning_effort) to prevent 400 Bad Request errors.
* Max token overrides allowing for extended context windows (up to 1,000,000 tokens), provided your client supports it.

## Prerequisites
1. Python installed on your system.
2. An active NVIDIA NIM API key.

## Installation
1. Clone or download this folder to your new laptop.
2. Open your terminal or command prompt and install LiteLLM:
   pip install litellm
3. Open start_bridge.bat in a text editor (like Notepad).
4. Find the line: 
   set "NVIDIA_NIM_API_KEY=YOUR_NVIDIA_API_KEY_HERE"
   and replace YOUR_NVIDIA_API_KEY_HERE with your actual NVIDIA API key.

## Usage
Simply double-click start_bridge.bat!

It will boot up the LiteLLM proxy server on port 4000. You can then configure your AI applications to point to http://127.0.0.1:4000 to utilize the proxy.
