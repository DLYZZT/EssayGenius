from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from .prompts import ESSAY_CORRECTION_PROMPT

def create_essay_correction_chain(api_key=None, model_name="gpt-4o", temperature=0.3):
    llm = ChatOpenAI(
        model=model_name,
        openai_api_key=api_key,
        temperature=temperature
    )
    
    chain = (
        RunnablePassthrough.assign(
            essay=lambda x: x["essay"]
        )
        | ESSAY_CORRECTION_PROMPT
        | llm
        | StrOutputParser()
    )
    
    return chain 