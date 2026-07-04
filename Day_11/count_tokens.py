from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.environ.get("GROQ_API")
if not api_key:
    raise SystemExit("set GROQ_API_KEY in a row" )
client = Groq(api_key=api_key)
samples=[
    "Hello",
    "I love learning about AI"
    "Antidistabilsihment"
    "namastey,kaise ho aap"
]

def prompt_tokens(text):
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
           messages=[{"role":"user","content":text}]
        )
    return response.usage.prompt_tokens

print("text=>prompt token count")
for text in samples: 
    print(text,"->",prompt_tokens(text))