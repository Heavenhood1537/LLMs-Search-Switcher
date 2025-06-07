import streamlit as st
from dotenv import load_dotenv
import requests
import threading
import os
import time

# Load environment variables
load_dotenv()

# Google API credentials
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def google_search(query):
    """Perform a Google search using Programmable Search Engine."""
    url = "https://www.googleapis.com/customsearch/v1" 
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query
    }
    try:
        response = requests.get(url, params=params)
        return response.json().get("items", [])
    except Exception as e:
        print(f"❌ Google Search request failed: {e}")
        return []

def ask_ollama_with_timeout(prompt, model_name="gemma3", timeout=20):
    """Send prompt to local Ollama model with a timeout."""
    result = {"answer": ""}
    error = {"msg": ""}

    def wrapper():
        try:
            url = "http://localhost:11434/api/generate"
            payload = {
                "model": model_name,
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(url, json=payload)
            result["answer"] = response.json().get("response", "")
        except Exception as e:
            error["msg"] = f"❌ Ollama request failed: {e}"

    timer = threading.Timer(timeout, lambda: None)  # Dummy function
    timer.start()
    try:
        wrapper()
    finally:
        timer.cancel()  # Cancel timer even if wrapper raises an error

    if error["msg"]:
        return error["msg"]
    return result["answer"]

def safe_get_content(result):
    title = result.get("title", "No Title")
    content = result.get("snippet", "No Content")  # Use 'snippet' field
    return f"{title}: {content}"

def main():
    st.set_page_config(page_title="LLM + Internet Search", layout="centered")
    st.title("🧠 LLM + Internet Search")
    st.markdown("Ask anything and get real-time answers — powered by **Google CSE** and **Ollama**.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Model Selection Dropdown
    available_models = ["gemma3", "mistral", "llama3.1", "codellama", "openhermes"]
    selected_model = st.selectbox("Select Model", available_models)

    query = st.text_input("Enter your question:")

    if st.button("Search"):
        if query:
            with st.spinner(f"🔍 Searching with Google CSE..."):
                results = google_search(query)

                # Limit context to top 2 results, each truncated to 100 chars
                limited_results = results[:2]
                context = "\n".join([safe_get_content(r)[:100] for r in limited_results])

                full_prompt = f"""
Use the given context to answer the question clearly and concisely.

Question: {query}

Context:
{context}
"""

            try:
                with st.spinner(f"🧠 Getting response from {selected_model} via Ollama..."):
                    answer = ask_ollama_with_timeout(full_prompt, model_name=selected_model, timeout=30)
            except Exception as e:
                answer = f"⚠️ An error occurred: {e}"

            st.session_state.chat_history.append({
                "question": query,
                "answer": answer,
                "model": selected_model
            })

    # Display chat history
    for i, item in enumerate(st.session_state.chat_history):
        st.markdown(f"**You:** {item['question']}")
        st.markdown(f"**🤖 {item['model']}**: {item['answer']}")
        st.markdown("---")

if __name__ == "__main__":
    main()