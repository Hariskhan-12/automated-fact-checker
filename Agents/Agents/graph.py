# graph.py
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

# Import agents
from researcher import researcher_node
from fact_checker import factchecker_node
from communicator import communicator_node  # New Communicator node
from llm_client import llm

# ---- State Schema ----
class GraphState(TypedDict):
    query: str
    research_results: str
    factcheck_results: str
    social_post: str  # New field for Communicator output

# ---- Memory ----
memory = MemorySaver()

# ---- Build Graph ----
graph = StateGraph(GraphState)

# Add nodes
graph.add_node("researcher", researcher_node)
graph.add_node("factchecker", factchecker_node)
graph.add_node("communicator", communicator_node)  # Add communicator node

# Add edges
graph.add_edge(START, "researcher")
graph.add_edge("researcher", "factchecker")
graph.add_edge("factchecker", "communicator")  # Connect Fact-Checker → Communicator
graph.add_edge("communicator", END)

# Compile workflow
workflow = graph.compile(checkpointer=memory)
