def numberToText(n):
    nstr=str(n)
    result=''
    for digit in n:
    str:
        if digit == '0':
            result += 'zero '
        elif digit == '1':
            result += 'one '
        elif digit == '2':
            result += 'two '
        elif digit == '3':
            result += 'three '
        elif digit == '4':
            result += 'four '
        elif digit == '5':
            result += 'five '
        elif digit == '6':
            result += 'six '
        elif digit == '7':
            result += 'seven '
        elif digit == '8':
            result += 'eight '
        elif digit == '9':
            result += 'nine '
    return result.strip()
user_input = input("Enter a positive number: ")
if user_input.isdigit():
        number = int(user_input)
        result = numberToText(number)
        print("Text representation:", result)
else:
        print("Please enter a valid positive number.")
        

