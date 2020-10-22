from colorama import init, Fore, Back
import os
import msvcrt as m
import sys
from time import sleep
#this is a random change
#methods
def wait():
    m.getch()
def typewrite(string):
    for char in string:
        sleep(0.01)
        sys.stderr.write(char)
#setup    
init()
clear = lambda: os.system('cls')
isRunning = True
print(Fore.GREEN)

#main
while (isRunning):
    
    typewrite("Select one of the options below [1-7]\n 1. Start a revision session\n 2. Add a module\n 3. Add a subtopic\n 4. View daily report\n 5. View weekly report\n 6. Add break suggestions\n 7. Exit\n")
    choice = input()
    clear()   
    if (choice == "1"):        
        print("You chose 1")
    elif (choice == "2"):
        print("You chose 2")
    elif (choice == "3"):
        print("You chose 3")
    elif (choice == "4"):
        print("You chose 4")
    elif (choice == "5"):
        print("You chose 5")
    elif (choice == "6"):
        print("You chose 6")
    elif (choice == "7"):
        isRunning = False
        break
    else:
        print("Invalid option, please enter value 1-7")
    wait()
    clear()