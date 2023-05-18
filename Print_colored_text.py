"""
    Print colored text:
    create a python function that takes a text from the user and
    print the text in colors
"""
from colorama import Fore

def insert_sentence():
    sentence = input("Enter text: ")
    print(Fore.RED + sentence)

insert_sentence()

