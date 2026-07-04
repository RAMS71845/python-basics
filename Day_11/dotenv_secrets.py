import os
from dotenv import load_dotenv
load_dotenv()
demo_key=os.environ.get("DEMO_API_KEY")
if(demo_key):
    print("Found",demo_key)
else:
    print("NOT FOUND")

demo_key=os.environ.get("GEMINI_API_KEY")
if(demo_key):
    print("Found",demo_key)
else:
    print("NOT FOUND")

