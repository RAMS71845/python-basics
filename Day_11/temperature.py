"""
Low temp ->consistent,predictable
High Temp=? varied,creative

"""
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.environ.get("GROQ_API")
if not api_key:
    raise SystemExit("set GROQ_API_KEY in a .env file first" )
client = Groq(api_key=api_key)
prompt="Suggets a creative name for an AI tutoring app.Reply with just the name"
response=client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[#message has two types-system and user message

      {
          "role":"user","content":prompt}],
     temperature=0.6
)
app_name=response.choices[0].message.content
print(app_name)

#creative ya alag responses chahiye ho toh high rakho nahi toh low rakho for consitent anwers