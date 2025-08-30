# agents/researcher.py
from typing import TypedDict, List
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from llm_client import llm
from prompts import RESEARCHER_PROMPT

# DuckDuckGo Search Tool
search_tool = DuckDuckGoSearchResults(name="DuckDuckGo", backend="news", num_results=5)

# State definition
class ResearchState(TypedDict):
    query: str
    results: List[str]

# ---- Step 1: Researcher Agent ----
def researcher_agent(query: str) -> str:
    """Uses DuckDuckGo + LLM summarization with timeout-safe fallback"""
    try:
        # Attempt live search
        search_results = search_tool.invoke(query)
    except Exception as e:
        print(f"⚠️ DuckDuckGo search failed: {e}")
        # Fallback: use mock results for hackathon demo
        search_results = [
            f"Sample evidence for '{query}' (Source: [Example](https://example.com))"
        ]

    # LLM Summarization
    prompt = ChatPromptTemplate.from_messages([
        ("system", RESEARCHER_PROMPT),
        ("human", f"User query: {query}\n\nSearch results: {search_results}")
    ])
    
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({})
    return response

# ---- Step 2: Convert to bullet points for Fact-Checker ----
def extract_bullets(text: str, max_bullets: int = 10) -> str:
    """
    Convert text into short, clear bullet points and limit to max_bullets.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a text processor. Convert the following text into clear, short bullet points, one claim per line."),
        ("human", f"Text:\n{text}")
    ])
    chain = LLMChain(llm=llm, prompt=prompt)
    bullets = chain.run({})
    
    # Limit number of bullets
    bullets_list = bullets.split("\n")
    limited_bullets = bullets_list[:max_bullets]
    return "\n".join(limited_bullets)

# ---- Node wrapper for LangGraph ----
def researcher_node(state: ResearchState) -> ResearchState:
    # Step 1: Get research summary
    summary = researcher_agent(state["query"])
    
    # Step 2: Convert summary into bullet points for Fact-Checker
    bullets = extract_bullets(summary, max_bullets=10)  # Limit to 10 bullets
    
    # Return updated state
    state["results"] = bullets
    return {"query": state["query"], "research_results": bullets}
