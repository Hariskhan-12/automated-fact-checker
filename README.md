# Automated Fact-Checker Agent 🕵️‍♂️📝

A **modular, end-to-end fact-checking pipeline** that converts user claims into verified, concise, social-media-ready summaries. Built for the **AiForAll 6-Hour Hackathon Challenge**, this project demonstrates rapid prototyping of AI workflows under time constraints.

---

## 🌟 Features

- **Researcher Agent** 🔎  
  Gathers top sources, summarizes definitions, key evidence, perspectives, and recent developments.

- **Fact-Checker Agent** ✅  
  Verifies each claim as True (✅), Uncertain (⚠️), or False (❌), with short reasoning and citations from trusted sources.

- **Communicator Agent** 📝  
  Generates concise, reader-friendly social media posts (<600 characters) using emoji-based clarity.

- **Graph-Based Workflow**  
  Modular pipeline: `Claim → Researcher → Fact-Checker → Communicator → Output`.

---

## 🛠️ Technologies Used

- Python 3.x  
- [LangGraph](https://pypi.org/project/langgraph/) for workflow orchestration  
- OpenAI / Hugging Face / Groq for LLM-based processing  
- Free libraries and APIs only  

---

## ⚡ Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/automated-fact-checker.git
cd automated-fact-checker
