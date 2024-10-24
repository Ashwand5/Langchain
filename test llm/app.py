from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import google.generativeai as genai

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

## LANGSMITH tracking
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

# llm = ChatGoogleGenerativeAI(model="models/gemini-pro")
# response=llm.invoke("Hi")
# print(response)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatGoogleGenerativeAI(model="models/gemini-pro")
output_parser=StrOutputParser()


if input_text:
    try:
        formatted_prompt = prompt.format(question=input_text)
        
        llm_response = llm.invoke(formatted_prompt)

        # Debug: Print the full response to understand its structure
        # st.write("Full Response from Gemini:")
        # st.json(llm_response)  # Display the entire response for debugging
        
        if hasattr(llm_response, 'content'):
            response_content = llm_response.content
        else:
            response_content = "No valid response received."

        st.write("Response from Gemini:")
        st.write(response_content)
    
    except Exception as e:
        st.error(f"Error: {str(e)}")