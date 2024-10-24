from langchain_community.llms import ollama

# This should list all available models
available_models = ollama.list_models()
print(available_models)
