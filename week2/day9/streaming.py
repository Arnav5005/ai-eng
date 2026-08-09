import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_keys=os.getenv("GROQ_API_KEY")

if not my_api_keys:
    raise ValueError("API Error")

client=Groq(api_key=my_api_keys)

model="llama-3.3-70b-versatile"
prompt="Explain how internet works"
message=[{
    "role":"system",
    "content":prompt
}]

# without streaming
# response=client.chat.completions.create(model=model, messages=message)
# answer=response.choices[0].message.content
# print(answer)

# with streaming
stream=client.chat.completions.create(model=model, messages=message, stream=True) # type: ignore
for chunk in stream:
    content=chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)