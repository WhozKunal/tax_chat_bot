# 🧾 Tax Assistant Chatbot

A production-ready, LangGraph-powered Tax Assistant Chatbot designed to simplify tax-related queries and automate routine tax support. This project uses **Flask** for the backend, **LangGraph** for agent workflows, and integrates with a customizable frontend UI.

---

## 🔧 Features

- 💬 Natural Language Query Handling
- 🧠 LangGraph Agent Integration
  - **Knowledgebase Agent** (RAG-based document retrieval)
  - **LLM Agent** (Tax-specific query resolution)
  - **Tool Agent** (External API & calculator support)
- 🧾 PDF Summary Generation for Tax Reports
- 📁 Document Upload & Metadata Extraction
- 🧑‍💼 Role-based Support (CA, Taxpayer, Auditor)
- 🌐 RESTful API Backend with Flask
- 🖥️ Plug-and-play Frontend UI (Chat Interface)

---

## 🛠️ Tech Stack

| Layer         | Tech                          |
|---------------|-------------------------------|
| Backend       | Python 3.10, Flask            |
| LLM Workflow  | LangGraph, OpenAI / Ollama    |
| Vector Store  | FAISS / Chroma                |
| File Parsing  | PyMuPDF / pdfminer            |
| Frontend      | HTML/CSS + Bootstrap / React  |
| Deployment    | Docker / Gunicorn / Nginx     |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-org/tax-assistant-chatbot.git
cd tax-assistant-chatbot
