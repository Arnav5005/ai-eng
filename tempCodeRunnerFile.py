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
# random ass text
text="Hello my name is Arnav i am 19 i recently bought a laptop Lenovo LOQ Ryzen 7 7435hs rtx 4060 24gb RAM 512 gb SSD and it's having performance issues , address - G-8 sandesh nagar , kankhal , haridwar , 249408"
prompt=f"This is a customer ticket. Please extract the necessary information from this - {text}"

message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model,messages=messages) # this underline under messages is just a pylance type-checking warning so we will ignore it by writing # type: ignore

answer=response.choices[0].message.content
print(answer)