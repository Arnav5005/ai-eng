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
# 3 prompts
prompt1="Hi"
prompt2="What are blackholes"
prompt3="Write a 1000 words essay on machine learning"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model , messages=messages , max_tokens=500) # type: ignore
    usage=response.usage
    print(f"prompt : {prompt} --> your tokens (input) : {usage.prompt_tokens} + completion tokens (output) : {usage.completion_tokens} = total tokens : {usage.total_tokens} , Finish reason ---> {response.choices[0].finish_reason}") # type: ignore

    #  we also added finish reason in the end which will give the reason for the response to complete if it's stop it means it ended naturally if it's length that means it stopped due to token cap which was set to 500 tokens