from email import message
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API error")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

# Schema and validation

class Ticket(BaseModel):
    name: str
    email: str
    model: str 
    issue: str

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f"Extract the personal information from ticket based on this schema and give me a json output {schema}" # NOTE - give me a json output  this is necessary to include in system_prompt otherwise it will show error

message_system={
    "role": "system",
    "content": system_prompt
}

# random ass text

text="Hello my name is Arnav i am 19 , My email id -  arnavpratapsingh2006@gmail.com . I recently bought a laptop Lenovo LOQ Ryzen 7 7435hs rtx 4060 24gb RAM 512 gb SSD and it's having performance issues , address - G-8 sandesh nagar , kankhal , haridwar , 249408"

prompt=f"This is a customer ticket. Please extract the necessary information from this - {text}"

message={
    "role": role,
    "content": prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format) # this underline under messages is just a pylance type-checking warning so we will ignore it by writing # type: ignore

answer=response.choices[0].message.content
print(answer)

# how to extract info from json
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.model)
print(ticket.issue)