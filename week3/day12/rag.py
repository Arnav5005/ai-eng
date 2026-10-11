import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer
import sys

# using cosine similarity to rank

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key not found")

client=Groq(api_key=my_api_key)

embed_model=SentenceTransformer("all-MiniLM-L6-v2")
groq_model="llama-3.3-70b-versatile"

# knowledge base

documents = [
"Employees receive 24 days of paid leave per year.",

"Employees work from the office on Tuesday, Wednesday and Thursday. ",

"Monday and Friday are optional work-from-home days.",

"Employees receive Rs 3000 per month for gym reimbursement.",

"Employees can claim Rs 2000 per month for home internet.",

"Employees have a 90 day notice period."
]

document_embedding=embed_model.encode(documents)

def cosine_simialrity(a,b):
    return np.dot(a,b)/(
        np.linalg.norm(a)*np.linalg.norm(b)
    )

def retrieve(query_embedding):
    scores=[]
    for i, embedding in enumerate(document_embedding):
        score=cosine_simialrity(query_embedding,embedding)  # find score of query for each line in document
        scores.append((score,documents[i])) # now the score list will append score as well as the line for which we found the score
    scores.sort(reverse=True) # top score will be on the top / front
    return scores[0] # this will return the first value of score i.e. the highest score

# now we are using our llm to give answer by retrieval because we will only get the document line using sentence transformer

def ask_llm(question,context):
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
    response=client.chat.completions.create(model=groq_model, messages=messages)
    answer=response.choices[0].message.content
    return answer

query="How much vacations do i get ?"
query_embedding=embed_model.encode(query)

score,context=retrieve(query_embedding) # as this function returns 2 values - score and document
# print(score) # used when we are not using llm
# print(context)
answer=ask_llm(query,context)
print(answer)

# why we need vector DB ?

# for transforming this 6 line docuument embeddings sentence transformer took 7.8kb which is too much so to deal with this problem we use vector DB as it stores these vector embeddings very efficiently and it also does searching very efficiently i.e. don't need to check scores of all the lines

# print(sys.getsizeof(document_embedding)) # 7808 bytes