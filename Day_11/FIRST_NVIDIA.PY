from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)
response=client.chat.completions.create(
    model="deepseek-ai/deepseek-v4-pro",
    messages=[
        {"role":"user","content":"What is full stack development ?"}
        
    ]
)
print (response.choices[0].message.content)