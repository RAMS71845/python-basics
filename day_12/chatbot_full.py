"""
exit,quit->leave
/reset->clr history
history->show how many turns are stored
save-> dump the messages to chat_history
/load->read back"""
  
import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()
MODEL="llama-3.1-8b-instant"
HISTORY_FILE="chat_history.json"
SYSTEM_PROMPT="You are a frindly ,concise assistant. Keep replies short and clear"

def save(messages:list)->None:
    with open(HISTORY_FILE,"w",encoding="utf-8") as f:
        json.dump(messages,f,indent=2,ensure_ascii=False)
        print(f"Bot:Saved{len(messages)} messages to {HISTORY_FILE}.\n")
                
def load() ->list:
    try:
        with open(HISTORY_FILE,"r",encoding="utf-8") as f:
            messages=json.load(f)
        print(f"Bot: Loaded {len(messages)}from {HISTORY_FILE}.\n")
        return messages
    except FileNotFoundError:
        print(f"Bot: No {HISTORY_FILE} yet -- nothing to load")
        return fresh_history()
def fresh_history()-> list:

 """A new conversation :just the system message"""
 return [{"role":"system","content":SYSTEM_PROMPT}]
   
 
def main()->None:
    client=Groq(api_key=os.environ.get("GROQ_API"))
    messages=fresh_history()
    print("ChatBot Raedy. Commands:/reset/history/save/load/exit \n")
    while True:
        user_text=input("You:  ").strip()
        if not user_text:
            continue
        cmd=user_text.lower()
        if cmd in {"/exit","/quit"}:
            print("Bot: Bye!")
            break
        if cmd=="/reset":
            messages=fresh_history()
            print("Bot: conversation cleared.\n")
            continue
        if cmd =="/save":
            save(messages)
            continue
        if cmd == "/history":
            count = sum(1 for m in messages if m["role"] != "system")
            print(f"Bot: {count} messages in history (excluding the system prompt).\n")
            continue
        if cmd=="/load":
            messages=load()
            continue
        messages.append({"role":"user","content":user_text})
        chat=client.chat.completions.create(model=MODEL,messages=messages)
        reply = chat.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": reply})
        print("Bot:", reply, "\n")


if __name__ == "__main__":
    main()






           