def shift_letters(str):
    result=''
    for char in str:
        if 'a'<=char<='z':
            if char=='z':
                result+='a'
            else:
                result+=chr(ord(char)+1)
        else:result+=char
    return result
    
user=input("enter a string")
result=shift_letters(user)
print(result)