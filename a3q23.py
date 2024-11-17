def findVowel(str):
    vowels='aeiouAEIOU'
    indices=[]
    index=0
    for char in str:
        if char in vowels:
            indices.append(index)
        index+=1
    return indices
user=input("Enter a string")
indices=findVowel(user)
print(indices)