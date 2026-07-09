from email import message
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API error")

client==Groq(api_key=my_api_key)

model="llama-3.3-70n-versatile"
role="user"
prompt="What is an LLM"

message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model,messages=messages)
print(response)
print("##############################")
# response=response.content[0]