from numpy import sqrt, array

def my_norm(vec):
    print("Yeet")
    return sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)

def my_inner(vec1, vec2):
    return vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2]