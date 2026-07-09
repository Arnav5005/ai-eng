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
prompt="suggest me a unique name for my clothing brand"

# System
message_system={
    "role":"system",
    "content":"You are a brand manager who suggests name for my clothing brand . Pick one name from your suggestions"
} 

message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]
# here we will also add temperature
response=client.chat.completions.create(model=model , messages=messages , temperature=2) # type: ignore
answer=response.choices[0].message.content
print(answer)