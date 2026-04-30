# AI-Workflow-Agent-API
# 🤖 AI Workflow Agent API

A production-style backend system that transforms natural language requests into structured multi-step workflows using LLM-powered agents and tool orchestration.

Built with **FastAPI + LangGraph + LLM integration (Gemini/Ollama/OpenAI-ready)**.

---

## 🚀 Overview

This project demonstrates how modern AI agents work in real-world systems:

- Converts natural language into structured plans
- Breaks tasks into executable steps
- Executes tools sequentially
- Maintains workflow state
- Returns structured JSON outputs

It simulates real-world automation systems used in AI SaaS products.

---

## 🧠 Key Features

- 🧩 LLM-powered Planner Agent
- ⚙️ LangGraph workflow orchestration
- 🔧 Tool-based execution system
- 📩 Email simulation tool (mock)
- 📝 Summarization tool
- 📦 Formatter tool (structured output generation)
- 📊 Execution logger
- 🔁 Retry + error handling system
- ⚡ Async FastAPI backend

---

## 🏗️ Architecture

```text
User Request
     ↓
FastAPI Endpoint (/agent)
     ↓
Planner Agent (LLM)
     ↓
LangGraph Workflow Engine
     ↓
Executor Nodes (Tools)
     ├── Summarizer Tool
     ├── Formatter Tool
     ├── Email Tool (Mock)
     └── Logger Tool
     ↓
Final Structured Response

📦 Tech Stack
Python 3.10+
FastAPI
LangGraph
LLM Provider (Gemini / Ollama / OpenAI compatible)
Async/Await architecture
Pydantic models

AI-Workflow-Agent-API/
│
├── app/
│   ├── main.py                 # FastAPI entry point
│   ├── routes/
│   │   └── agent_routes.py     # API endpoints
│   │
│   ├── graph/
│   │   └── workflow.py         # LangGraph workflow
│   │
│   ├── tools/
│   │   ├── summarizer.py
│   │   ├── formatter.py
│   │   ├── emailer.py
│   │   └── logger.py
│   │
│   └── utils/
│       └── llm.py              # LLM abstraction layer
│
├── test.py
├── requirements.txt
└── README.md

{
  "input": "summarize this article and email it to me",
  "plan": [
    "summarize text",
    "format email",
    "send email"
  ],
  "tool_calls": [
    {
      "tool": "summarizer",
      "input": "...",
      "output": "summary text"
    },
    {
      "tool": "formatter",
      "input": "...",
      "output": "formatted email"
    },
    {
      "tool": "emailer",
      "input": "...",
      "output": {
        "status": "sent"
      }
    }
  ],
  "final_output": {
    "status": "sent",
    "message": "Email sent successfully (mock)"
  },
  "status": "success"
}

▶️ How to Run Locally
1. Clone repository
git clone https://github.com/your-username/ai-workflow-agent-api.git
cd ai-workflow-agent-api
2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Add environment variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here
5. Run server
uvicorn app.main:app --reload
6. Test API
curl -X POST "http://127.0.0.1:8000/agent" \
-H "Content-Type: application/json" \
-d '{"input": "summarize this article and email it"}'
🧪 Example Use Cases
AI email automation
Task decomposition agents
Workflow automation systems
LLM orchestration demos
Backend AI engineering portfolio project
☁️ Deployment (Render)
Build Command
pip install -r requirements.txt
Start Command
uvicorn app.main:app --host 0.0.0.0 --port 10000
🧠 Learning Goals

This project helps you understand:

LLM orchestration
Agent-based systems
Tool calling architecture
Workflow automation
Production backend design
State management in AI systems
🔮 Future Improvements
Add persistent memory (Redis / DB)
Add streaming responses
Add authentication layer
Add multi-agent collaboration
Replace mock email with real SMTP integration
Add vector database memory layer