def remove_punctuation(str):
    punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result=''
    for char in str:
        if char not in punctuation:
            result+=char
    return result
user=input("Enter a string")
result=remove_punctuation(user)
print(result)    