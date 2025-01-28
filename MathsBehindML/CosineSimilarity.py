import numpy as np

def cosine_similarity(a,b):
    dot_product = np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    return dot_product/(norm_a*norm_b)

m1 = np.array([5,0,3,1])
m2 = np.array([0,4,1,5])

u1 = np.array([4,0,5,1])

cosine_sim_u1m1 = cosine_similarity(u1,m1)
cosine_sim_u1m2 = cosine_similarity(u1,m2)

print("Cosine Similarity of u1m1: ", cosine_sim_u1m1)
print("Cosine Similarity of u1m2: ", cosine_sim_u1m2)


if cosine_sim_u1m1 > cosine_sim_u1m2:
    print("Watch M1")
else:
    print("Watch M2")