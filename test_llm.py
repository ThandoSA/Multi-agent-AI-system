import os
from langchain_ibm import WatsonxLLM

# Environment variables
os.environ["WATSONX_APIKEY"] = "L3Hgk0nMumhwjRuZ4on_EHu-1B29HJmoY-9YYJI_q7K-"

PROJECT_ID = "eb4b5fd3-9969-4cf6-8597-f7e265a5f5da"

llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",
    project_id=PROJECT_ID,
    url="https://us-south.ml.cloud.ibm.com",
    params={
        "temperature": 0.7,
        "max_new_tokens": 300
    }
)

response = llm.invoke("Explain multi-agent AI in simple terms.")
print(response)
