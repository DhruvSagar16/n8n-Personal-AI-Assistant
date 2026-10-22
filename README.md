# 🤖 Personal AI Assistant — n8n + Streamlit

An AI-powered personal assistant built using **n8n, Python, Streamlit, and Groq** to interact with an AI agent through a simple chat interface and automate everyday tasks.

## 📌 Overview

The Personal AI Assistant combines a Streamlit web interface with an n8n automation workflow. Users can send natural-language requests and receive responses from an AI agent that can use connected tools to perform different tasks.

## ✨ Features

- 💬 **AI Chat Assistant** — Ask questions in natural language.
- 📅 **Calendar Management** — Assist with scheduling events and meetings.
- 📧 **Email Assistance** — Read, summarize, and help draft email replies.
- ✅ **Task Management** — Manage tasks and to-do lists.
- 📝 **Quick Notes** — Save and organize notes.
- 💰 **Expense Tracking** — Query expenses and budget-related information.
- 🧠 **AI Agent with Tools** — Uses an n8n AI Agent with connected tools and a Groq chat model.
- 🔗 **Streamlit Interface** — Provides an interactive chat experience.

*The availability of individual features depends on the tools, integrations, and credentials configured in the n8n workflow.*

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — Chat interface
- **n8n** — Workflow automation and AI agent orchestration
- **Groq API** — Language model access
- **Requests** — Communication between Streamlit and the n8n webhook
- **Simple Memory** — Conversation context within the configured workflow

## 🏗️ Architecture

1. The user enters a message in the Streamlit chat interface.
2. The Python application sends the message to an n8n webhook.
3. The n8n AI Agent processes the request using the configured language model, memory, and connected tools.
4. The workflow returns its response through the webhook.
5. Streamlit displays the response in the chat interface.

## 📂 Project Structure

```text
n8n-Personal-AI-Assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env                 # Local only; do not commit
```

An exported n8n workflow JSON file can also be included if you choose to share the workflow configuration.

## ⚙️ Prerequisites

Before running the project, install:

- Python 3.10 or a compatible version supported by your dependencies
- Git
- Docker Desktop, if running n8n locally with Docker
- A API key
- Credentials for any external services used by your workflow

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DhruvSagar16/n8n-Personal-AI-Assistant.git
cd n8n-Personal-AI-Assistant
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run the following and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure n8n

Run n8n locally or configure a hosted n8n instance.

If running locally with Docker, make sure n8n is accessible at `http://localhost:5678`.

Import the workflow JSON if one is included in the repository, or recreate the workflow in n8n. Configure the required model, memory, integrations, and credentials, then activate the workflow.

**Important:** Configure your own credentials in n8n. Never share API keys, OAuth tokens, or exported workflow files containing secrets.

### 5. Configure the webhook URL

Create a `.env` file in the project root:

```env
N8N_WEBHOOK_URL=http://localhost:5678/webhook/YOUR_WEBHOOK_PATH
```

Replace the example path with the production webhook URL from your own n8n workflow.

Install `python-dotenv` if it is not already listed in `requirements.txt`:

```bash
python -m pip install python-dotenv
```

The Python application should load the variable from `.env` using `os.getenv("N8N_WEBHOOK_URL")`.

Keep `.env` private and ensure it is excluded by `.gitignore`.

### 6. Run the Streamlit application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser and start chatting with your assistant.

## 🔐 Security Notes

- Do not commit `.env` files or API keys.
- Keep OAuth credentials and tokens inside n8n's credential manager.
- Review exported workflow JSON files before uploading them.
- Use appropriate authentication and access controls before exposing webhooks publicly.
- A local n8n webhook is not accessible to a publicly hosted Streamlit app unless n8n is also securely hosted or exposed through an appropriate network configuration.

## 🔮 Future Improvements

- Deploy the Streamlit interface and n8n workflow for remote access.
- Add user-specific conversation sessions and memory.
- Improve error handling and request validation.
- Add authentication and access controls.
- Expand integrations with additional productivity tools.

## 👨‍💻 Author

**Dhruv Sagar**

AI & Data Science graduate interested in AI agents, LLM applications, workflow automation, and building practical AI-powered solutions.

## 📄 License

This project is available for learning and personal use. Add a license file if you want to specify formal reuse and distribution permissions.

