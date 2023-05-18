"""
    BMI calculator: 
    create a python function that takes the user height , weight and
    print 
        - the user BMI 
        - and if the user underweight , overweight or healthy
"""
from colorama import Fore , Style

def bmi_calculator(weight, height):
    bmi = weight / height**2
    print("BMI = ","%.2f" %bmi,'KG/m^2')    
    if bmi >= 18.5 and bmi <= 25:
        print(Fore.GREEN + "healthy")
        print(Style.RESET_ALL)
    elif bmi > 25:
        print(Fore.RED + "Overweight")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + "underweight")
        print(Style.RESET_ALL)


while True:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    height*= 0.01 # convert height from cm in meter 
    bmi_calculator(weight, height)
    ch = input("you want clacute again enter 'y' for yes 'n' for no: ")
    if ch in ['n','N']:
        break
