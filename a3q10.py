# Create a function that returns all the unique permutations of a given string.
def permutation(s):
    if len(s)==0:
        return []
    elif len(s)==1:
        return [s]
    else:
        perm=[]
        for i in range(len(s)):
            for j in permutation(s[:i]+s[i+1:]):
                perm.append(s[i]+j)
        return perm
s=input("Enter a string:")
print(permutation(s))                