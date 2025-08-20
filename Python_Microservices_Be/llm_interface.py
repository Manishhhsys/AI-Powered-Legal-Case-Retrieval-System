# backend/llm_interface.py

from langchain_ollama import ChatOllama
import config

def get_llm():
    """
    Initializes and returns the ChatOllama instance.
    """
    llm = ChatOllama(
        model=config.LLM_MODEL_NAME,
        base_url=config.OLLAMA_BASE_URL
    )
    return llm