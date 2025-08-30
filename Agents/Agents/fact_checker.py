# agents/factchecker.py
from typing import TypedDict
from llm_client import llm
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from prompts import FACT_CHECKER_PROMPT

# ---- State definition (optional) ----
class FactCheckerState(TypedDict):
    query: str
    research_results: str
    factcheck_results: str

# ---- Fact-Checker logic ----
def factchecker_agent(research_results: str) -> str:
    """
    Takes the Researcher output and produces a fact-checked verdict.
    Returns a structured text output.
    """
    # Prepare LLM prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", FACT_CHECKER_PROMPT),
        ("human", f"Researcher output:\n{research_results}")
    ])
    
    # Create chain and run
    chain = LLMChain(llm=llm, prompt=prompt)
    factcheck_output = chain.run({})
    
    return factcheck_output

# ---- Node wrapper for LangGraph ----
def factchecker_node(state: FactCheckerState) -> FactCheckerState:
    """
    Node function to integrate into LangGraph workflow.
    """
    output = factchecker_agent(state["research_results"])
    state["factcheck_results"] = output
    return state
