from random import*
from time import*
from os import*
logo = """
|-----------------------------------------------|
|  |-----|                uY Soft               |
|  |   u |               Pythonix               |
|  |-----|-----|           pY-DOS               |
|        |  Y  |          Version               |
|        |-----|-----       6.0                 |
|              |            Built on            |
|    pY-DOS    |    New Technology  1.1.1022    |
|-----------------------------------------------|
"""
logoData = """
|--------|
|       -|
|
|--------|
|        |
|        |
|--------|
"""
def c():
    sleep(0.5)
    system("cls")
def helloscr():
    print("pYDOS 6 Hello Screen:>")
    print("------------------------------------------------")
    print("Hello!")
    print("Hi!")
    print("Hola!")
    print("Bonjour!")
    print("------------------------------------------------")
    print("(Press <Enter> key to log in.)")
    log = input("Log:>")
    c()
def dos():
    print(logo)
    sleep(2)
    c()
    helloscr()
    while True:
        print("------------------------------------------------")
        print("Pythonix pY-DOS 6 Options Menu:>")
        space1 = "------------------------------------------------"
        print(space1)
        print("Settings:>")
        space2 = "                                                "
        print(space2)
        print("1.Version")
        print(space1)
        print("Apps & Docs:>")
        print(space2)
        print("2.Calculator.py")
        print("3.GuessingNumbers.py")
        print("4.Exit")
        print(space1)
        print("Windows NT 6 Commands:>")
        print("(Cannot be used on Windows Vista/XP/2003/2000/98 or earlier)")
        print(space2)
        print("5.Start CMD")
        print("6.Start MSconfig")
        print("7.Start PowerShell")
        print("8.Start Regedit")
        print("9.Start Explorer")
        #print("10.Which Windows OSes are Windows NT 6?")
        print(space1)
        op = int(input("Local:>"))
        c()
        if op == 5:
            system("start cmd")
        elif op == 10:
            print("Windows 11,Windows 10,Windows 8.x,Windows 7")
            c()
        elif op == 6:
            system("start msconfig")
        elif op == 7:
            system("start powershell")
        elif op == 8:
            system('start regedit')
        elif op == 9:
            system("start explorer")
        elif op == 4:
            break
        elif op == 1:
            print(logoData)
            print("Pythonix pY-DOS 6")
            print("Standard Edition(Free)")
            print("Pythonix Core:")
            print("Pythonix Version 1.1.1012")
            sleep(2)
            c()
            pass
        elif op == 2:
            print("----------Calculator.py----------")
            print("Choose a way:")
            print("1=+ 2=- 3=* 4=/")
            ways = int(input("Way:"))
            num1 = int(input("The first number is:"))
            num2 = int(input("The second number is:"))
            if ways == 1:
                print(num1 + num2)
            elif ways == 2:
                print(num1 - num2)
            elif ways == 3:
                print(num1 * num2)
            else:
                print(num1 / num2)
            c()    
        elif op == 3:
            print("-----GuessingNumbers.py-----")
            print("The number is from 1 to 100.")
            answer = randint(1,100)
            while 1:
                i = int(input("Guess:"))
                if i > answer:
                    print("It is big.")
                elif i < answer:
                    print("It is small.")
                else:
                    print("Great!")
                    sleep(0.5)
                    break
            c()    
        else:
            print("Wrong letters.Type again.")
dos()    
