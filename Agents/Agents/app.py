# app.py
import streamlit as st
from graph import workflow  # Compiled workflow with Researcher + Fact-Checker + Communicator

st.set_page_config(page_title="Hackathon Fact-Checker", layout="centered")

st.title("🔎 Hackathon Fact-Checker Agent")
st.write("Enter a claim or question, and the pipeline will find evidence and verify it.")

# User input
user_input = st.text_input("Enter your claim or question:")

if st.button("Run Pipeline"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a query first.")
    else:
        # Initialize state with all required fields
        state_input = {
            "query": user_input,
            "research_results": "",
            "factcheck_results": "",
            "social_post": ""  # New field for Communicator
        }

        # Run full workflow (Researcher → Fact-Checker → Communicator)
        output = workflow.invoke(state_input, config={"configurable": {"thread_id": "user-123"}})

        # Display Researcher output
        st.subheader("📌 Researcher Results")
        research_bullets = output["research_results"].split("\n")
        for bullet in research_bullets:
            st.write(f"- {bullet}")

        # Display Fact-Checker output
        st.subheader("✅ Fact-Checker Results")
        factcheck_bullets = output["factcheck_results"].split("\n")
        for bullet in factcheck_bullets:
            st.write(f"- {bullet}")

        # Display Communicator output (Social Post)
        st.subheader("📝 Social Media Post")
        st.write(output.get("social_post", "No social post generated."))
