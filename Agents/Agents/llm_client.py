from langchain_groq import ChatGroq
import os

# Set your Groq API key in .env or directly here
groq_api_key = os.getenv("GROQ_API_KEY")

# Use LLaMA 3 or other Groq-supported model
llm = ChatGroq(
    groq_api_key=,
    model_name="openai/gpt-oss-120b",
    temperature=0.3,
)
