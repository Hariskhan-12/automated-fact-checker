# agents/communicator.py
from typing import TypedDict
from llm_client import llm
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

# Enhanced prompt template for Communicator
COMMUNICATOR_PROMPT = """
You are the Communicator Agent 📝. 
Your task is to convert the Fact-Checker results into a concise, plain-English social media post under 600 characters.

Rules:
1. ✅ Include key verified facts only.
2. ⚠️ Highlight important uncertainties or speculative claims.
3. ❌ Clearly mark false or unsupported claims.
4. Make it punchy, readable, and shareable.
5. Avoid jargon; briefly explain technical terms if needed.
6. Write in one paragraph, using emojis for clarity: ✅ for verified, ⚠️ for uncertain, ❌ for false.
7. Do not invent new claims; only summarize what the Fact-Checker provides.
8. Preserve short source names only if necessary, otherwise omit.

Input: Fact-Checker Results
{fact_checker_results}

Output Example:
✅ Quantum computers use qubits that can be in superposition. ⚠️ Some claims about speed-up in chemistry are unverified. ❌ Ignore fictitious claims like "neglecton". Key context: short, clear, reader-friendly.

Write a social media-ready paragraph under 600 characters.
"""

class CommunicatorState(TypedDict):
    query: str
    research_results: str
    factcheck_results: str
    social_post: str  # New field for output

def communicator_node(state: CommunicatorState) -> CommunicatorState:
    # Prepare LLM prompt
    prompt = ChatPromptTemplate.from_template(COMMUNICATOR_PROMPT)
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run LLM
    social_post = chain.run({"fact_checker_results": state["factcheck_results"]})
    
    # Update state
    state["social_post"] = social_post
    return state
