import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM

load_dotenv()

def get_llm():
    return WatsonxLLM(
        model_id="ibm/granite-13b-instruct-v2",
        url=os.getenv("WATSONX_URL"),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        params={
            "temperature": 0.3, 
            "max_new_tokens": 512
        }
    )
