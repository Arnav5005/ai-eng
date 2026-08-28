import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API not found")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-20b"

# step 1 - knowledge base

knowledge_base={
    "name":"Arnav pratap singh",
    "age":20,
    "profession":"CS sudent"
}

# step 2 - retrieve info

def retrieval_info(question):
    question=question.lower()
    if "age" in question:
        return knowledge_base["age"]
    elif "profession" in question:
        return knowledge_base["profession"]
    else:
        return None
    
def ask_llm(question):
    context=retrieval_info(question)
    sys_prompt=f"""answer in one line only . Answer only based on this context , do not hallucinate. context: {context}"""
    system_message={
        "role": "system",
        "content": sys_prompt
    }
    message={
        "role": "user",
        "content": question
    }
    messages=[system_message, message]
    response=client.chat.completions.create(model=model, messages=messages)
    answer=response.choices[0].message.content
    return answer

question="what is Arnav's age ?" # you need to give exact prompt as written in retrieval software which matches keywords if i asked how old is arnav then he won't be able to answer this
print(ask_llm(question))