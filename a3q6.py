#Define a function to check if a given string is a palindrome. Example: madam ⟲ madam, racecar ⟲
# =============================================================================
#  racecar.
# =============================================================================
def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
s=input("Enter a string" )
if is_palindrome(s):
    print("Palindrome")
else:
    print("Not palindrome")