import runpy
import os
import time
print("hello")
print("boot system?")
print("Y/N")
answer=(input("insert answer here:"))

if  answer==("Y"):

    password = input("password:")

    if password == "ERR_4o4":
        print("correct password")
        time.sleep(0.6)
        os.system("cls")
        print("here are all the options pick one")
        print("1.spam")
        print("2.calculator")
        print("3.counting")
        print("4.ZERO")
        answer2=(input("insert answer here:"))
        if answer2==("1"):
            os.system('cls')
            runpy.run_path("spam.py", init_globals=None, run_name=None)

        elif answer2==("2"):
            os.system('cls')
            runpy.run_path("cal.py")

        elif answer2==("3"):
            os.system('cls')
            runpy.run_path("counting.py", init_globals=None, run_name=None)

        elif answer2==("4"):
            os.system('cls')
            runpy.run_path("C:\\Users\\manji\\Downloads\\python code\\ZERO\\ZERO.py", init_globals=None, run_name=None)
    else:
        print("wrong password")
        input()

elif answer==("N"):
   os.system('cls')
   print("shutting down")
   time.sleep(3)

else:
    print("sorry you can only answer by saying Y/N")
    time.sleep(2)
    print("we are going to reset")
    print("please wait...")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    os.system('cls')
    runpy.run_path("main_menu.py.py", init_globals=None, run_name=None)
 #runpy.run_path("C:\\Users\\manji\\source\\repos\\cal\\cal.py", init_globals=None, run_name=None)

