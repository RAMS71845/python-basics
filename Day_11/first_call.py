#pip intsall groq
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.environ.get("GROQ_API")
if not api_key:
    raise SystemExit("set GROQ_API_KEY in a .env file first" )
client = Groq(api_key=api_key)
response=client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[#message has two types-system and user message
      {
        "role": "system",
        "content": "u r a singer of hindi bollywood u have to answer the questions in 2 lines by a song"
      },
      {
          "role":"user",
           "content":"What is the meaning of full stack development"
      }
    ],
)

print(response.choices[0].message.content)

usage=response.usage
print()
print("Prmopt Tokens :",usage.prompt_tokens)
print("Response Tokens: ",usage.completion_tokens)
print("Total Tokens : ",usage.total_tokens)
