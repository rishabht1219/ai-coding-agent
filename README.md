# 🤖 AI Coding Agent (Gemini)

A simple CLI-based AI agent using Google Gemini that can read, write, and execute code via tool-calling.

## 🚀 Features
- Multi-step reasoning loop
- File operations (read, write, list)
- Run Python scripts
- Basic autonomous bug fixing

## 🔑 Setup
1. Install dependencies:
   pip install google-genai python-dotenv

2. Create `.env`:
   GEMINI_API_KEY=your_api_key_here

## ▶️ Usage
python main.py "your prompt here"

Verbose mode:
python main.py "fix bug" --verbose

## ⚠️ Note
This is a **demo project**. No security or sandboxing — use carefully.

## 💡 Example
- "List files"
- "Read main.py"
- "Fix the bug in calculator"