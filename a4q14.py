#Write a python program that generates a tuple where each element is the square of an integer from 1 to 10

def generate():
    sq_tuple=tuple(i**2 for i in range(1,11))
    return sq_tuple
square=generate()
print(square)
