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
role="user"
prompt="What is an LLM"

message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model,messages=messages) # this underline under messages is just a pylance type-checking warning so we will ignore it by writing # type: ignore
print(response)

print("##############################")

answer=response.choices[0].message.content
print(answer)

# we can do this too

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is an LLM?"
#         }
#     ]
# )
# print(response.choices[0].message.content)