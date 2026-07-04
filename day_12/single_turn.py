import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
MODEL="llama-3.1-8b-instant"

def main()->None:
    client=Groq(api_key=os.environ.get("GROQ_API_KEY"))
    messages=[
        {"role":"user","content":"In one sentence ,what is a chatbot?"}

    ]
    chat=client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    reply=chat.choices[0].message.Content
    print(reply.strip())

if __name__ =="__main__":
    main()

