# uv add groq python-dotenv numpy sentence-transformers
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer

# all-MiniLm-L6-v2 is a compact, lightweight transformer model that converts sentences and short paragraphs into a 384-dimensional dense vector space for text comparison and search i.e. there are 384 fetures to compare from 

# working of cosine_similarity function - cos θ = (a · b) / (||a|| · ||b||)

def cosine_similarity(a,b): # When two embedding vectors mean the same thing, the angle theta between them is 0 degrees . The cosine of 0 degrees is 1, which intuitively represents a 100% match.
    return np.dot(a,b)/( # np.dot(a,b) will give the dot product of a,b  Ex - a=(3,4) b=(5,6) then a·b = a1b1 + a2b2 => a·b=39
        np.linalg.norm(a)*np.linalg.norm(b) # this is finding magnitude of vector a and b them multiplying it Ex- |a|=root(a1^2+a2^2)
    )

model=SentenceTransformer("all-MiniLM-L6-v2")
# text="Machine Learning is fun"

# embedding=model.encode(text)
# print(embedding.shape)
# print(embedding)

t1="There are 24 paid leaves"
t2="There are 24 vacation days"

v1=model.encode(t1)
v2=model.encode(t2)

print(cosine_similarity(v1,v2)) # 0.43657768

t3="There are 24 paid leaves"
t4="There are 24 paid leaves"

v3=model.encode(t3)
v4=model.encode(t4)

print(cosine_similarity(v3,v4)) # 1.0000001
# Computers can't represent most decimal numbers exactly in binary. During the dot product and magnitude calculations, tiny rounding errors can accumulate.