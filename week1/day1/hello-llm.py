#  if not able to run code run using python hello-llm.py
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API error")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

message=[{
    "role":"user",
    "content":"What is an LLM"
}]

response=client.chat.completions.create(model=model,messages=message) # this underline under messages is just a pylance type-checking warning so we will ignore it by writing # type: ignore
print(response)

print("##############################")

answer=response.choices[0].message.content
print(answer)