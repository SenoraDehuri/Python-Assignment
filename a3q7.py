# Write a Python function to check whether an alphabet is a vowel or consonant.
def isVowel(s):
    if s in['a','e','i','o','u']:
        return True
    return False
s=input("Enter a alphabet")
if isVowel(s):
    print("Vowel")
else:
    print("Consonant")
    
