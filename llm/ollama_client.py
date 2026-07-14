from langchain_ollama import ChatOllama


def get_llm():
    return ChatOllama(
        model="llama3.2",
        temperature=0.3,
        keep_alive="30m",
        num_predict=96,
        sync_client_kwargs={"timeout": 120.0},
        async_client_kwargs={"timeout": 120.0},
    )
