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

def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model , messages=messages) # type: ignore
    ans=response.choices[0].message.content
    return ans

# bad_prompt="This is a user complaint : My girlfriend broke up with me" 
# this is a laptop company so our chatbot must answer questions that falls under his domain not crap like this so we will add role prompt
bad_prompt="""

#ROLE : You are a support assistant at a mobile/laptop company responsible for handling user complaints

#TASK : You have to calssify the issue in a category

#CONSTRAINTS : You have to calssify the issue in the following categories - billing issue , software issue , hardware issue , return

#OUTPUT FORMAT : Your answer should be in one word only . That word should be one of the categories given in constraints

#EXAMPLE : For instance , if a user says i want a refund then the category is return 

#FALLBACK : if the issue is unrelated to any of the following categories mentioned in the constraints , then the answer should be sorry i can't help with this request

This is a user complaint : my laptop is not working

"""
print(llm_ans(bad_prompt))