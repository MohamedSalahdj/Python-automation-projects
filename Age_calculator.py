"""
        Age Calculator : 
        create a python function that takes user birthdate and prints
        how old he is
"""
from datetime import datetime 
def age_calc():
    user_birthdate = input("Enter your date of birth: such as '18-06-1999' : ")
    birthdate = datetime.strptime(user_birthdate, '%d-%m-%Y').date()
    age = ( datetime.now().date().year - birthdate.year)
    return f"Your old are you '{age}'"

print(age_calc())