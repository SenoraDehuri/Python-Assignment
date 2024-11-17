def days_in(month):
    month=month.lower()
    if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
       return "No. of days: 31 days"
    elif month == "april" or month == "june" or month == "september" or month == "november":
       return "No. of days: 30 days"
    elif month == "february":
        return "No. of days: 28/29 days"
month=input("Enter month")
result=(days_in(month))
print(result)