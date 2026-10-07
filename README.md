# AI Code Review Assistant

An AI-powered code review tool that analyzes source code for bugs, security
vulnerabilities, performance issues, and code-quality problems.

The application uses OpenRouter for AI-powered analysis and Streamlit for the
web interface.

## Features

- AI-powered code review
- Bug detection
- Security vulnerability analysis
- Performance issue detection
- Code-quality suggestions
- Line-specific issue reporting
- Severity classification:
  - Critical
  - Warning
  - Suggestion
- Supports C++, Python, and Java
- API error handling
- Streamlit web interface

## Tech Stack

- Python
- Streamlit
- OpenAI Python SDK
- OpenRouter API
- python-dotenv

## Project Structure

```text
AI-Code-Review-Assistant/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── app/
    ├── main.py
    └── reviewer.py