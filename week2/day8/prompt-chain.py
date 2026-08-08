import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
   raise ValueError("API Error")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

JD="""
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIS
- 2+ years of experience
"""
Resume="""
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""

def ask_llm(system_prompt,user_prompt):
    sys_msg={
        "role":"system",
        "content":system_prompt
    }
    user_msg={
        "role":"user",
        "content":user_prompt
    }
    messages=[sys_msg,user_msg]
    response=client.chat.completions.create(model=model , messages=messages)
    answer=response.choices[0].message.content
    return answer

def step1_resume_extract():
    # extract skills from resume
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the candidate's resume provided.
    Only return the skills no other information. Do not invent any skills by yourself 
    """
    user_prompt=f"""
    Extract the skills from this resume {Resume}
    """
    return ask_llm(system_prompt,user_prompt)

def step2_JD_extract():
    # extract skills from JD
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the JD(Job Description) provided.
    Only return the skills no other information. Do not invent any skills by yourself 
    """
    user_prompt=f"""
    Extract the skills from this JD {JD}
    """
    return ask_llm(system_prompt,user_prompt)

def step3_match(candidate,jd):
    # match candidate's skills to JD
    system_prompt="""
    You are a professional HR assistant. Compare the skills of candidates and the skills required for the job in the JD and produce a final score between 1 and 100 also produce a short verdict whether the candidate is a good fit for the role or not. 
    """
    user_prompt=f"""
    compare and match the skills
    JD:{jd}
    Candidate:{candidate}
    """
    return ask_llm(system_prompt,user_prompt)

candidate=step1_resume_extract()
sleep(2)
jd=step2_JD_extract()
sleep(2)
score=step3_match(candidate,jd)
print(score)