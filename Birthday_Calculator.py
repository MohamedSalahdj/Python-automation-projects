from  datetime import datetime

def birthday_calc():

    user_birthdate = input("Enter your date of birth: such as '18/06/1999' : ")
    birthdate = datetime.strptime(user_birthdate,  '%d/%m/%Y')
    
    if birthdate.month == datetime.now().date().month and birthdate.day < datetime.now().date().day:
        days_left_to_birthday = 365 - datetime.now().date().day
        print(days_left_to_birthday)

    elif birthdate.month < datetime.now().date().month:
        days_left_to_birthday = (((12 -  datetime.now().date().month ) + birthdate.month) * 30)  - ( 30 - datetime.now().date().day ) + (birthdate.day)
        print(days_left_to_birthday)
    
    else: 
        days_left_to_birthday = ( (birthdate.month - datetime.now().date().month) * 30 + (30 - datetime.now().date().day) - (30 - birthdate.day))
        print(days_left_to_birthday)
    
birthday_calc()