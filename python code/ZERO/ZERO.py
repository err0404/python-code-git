import time
from datetime import datetime
import os
import runpy
from colorama import Fore
from pynput.keyboard import Key, Controller
import socket
keyboard = Controller()
keyboard.press(Key.f11)

options_Y = ["yes", "y", "Y", "YES", "ye"]
options_N = ["no", "n", "N", "NO", "nah"]
print("hi")
print("would you like to")
print("initiate ZERO?")
print("Y/N")
boot = input()
os.system("cls")

boot_time = 0.04


if boot in options_Y:
    with open("zero title screen.txt", "r") as file:
        logo = file.read()

    lines_logo = logo.split('\n')


    def logo_print_fuct():
        for line in lines_logo:
            time.sleep(boot_time)
            print(line)


    logo_print_fuct()
    time.sleep(1)

    commands = False
    try:
        with open("memory_zero.txt", "r") as file:
            lines = file.readlines()
    except:
        print(Fore.RED + "ERROR_404\ncannot find memory unable to run" + Fore.RESET)
        input()


    if not lines or len(lines) == 0:
        time.sleep(1)
        print("hello i am ZERO, what is your name?")
        time.sleep(0.05)
        print("")
        name = input("hi my name is:")
        with open("memory_zero.txt", "w") as file:
            file.write("name = " + name)
        print("\nhi " + name)

        print("")
        print("what is your date of birth(dd/mm/yyyy)")
        time.sleep(0.05)
        print("")
        print("")
        birth_date = input("my date of birth is:")
        with open("memory_zero.txt", "a") as file:
            file.write("\nbirth date(dd/mm/yyyy) = " + birth_date)
        print("your date of birth is:" + birth_date)
        time.sleep(2)
        print("thanks for the information,please rerun ZERO")



    else:
        name_line = lines[0].strip()
        birth_line = lines[1].strip()
        birth_line_cal = lines[1].strip()

        name = name_line.split("=")[1].strip()
        birth_date = birth_line.split("=")[1].strip()
        birth_date_cal = birth_line_cal.split("=")[1].strip()

        print("hi " + name)
        time.sleep(0.4)
        print("welcome back!")
        time.sleep(0.4)
        now_raw = datetime.now()
        now = now_raw.strftime("%d/%m/%Y")
        current_year = now_raw.year
        birth_Date = datetime.strptime(birth_date_cal, "%d/%m/%Y")
        birth_year = birth_Date.year
        age = current_year - birth_year
        print("your age is "+str(age))
        time.sleep(0.4)
        print("birth date:"+birth_date)
        time.sleep(0.4)
        print("current time is "+str(now))
        time.sleep(0.2)
        U_input = ""
        print("\ntype help for commands")

        commands = True

        while commands == True:
            U_input = input()
            U_input = U_input.strip()

            if U_input.lower() == "help":
                print("""List of all commands:
                      help: displays all commands
                      ZERO: runs ZERO (does not function)
                      cls mem: clears ZERO's memory
                      close: close's the program
                      descript:give simple description of ZERO,(something)
                      show ip:shows ip address, host name
                      cls: clears screen""")

            elif U_input.lower() == "cls mem":
                with open("memory_zero.txt", "w") as file:
                    file.write("")
                print("memory_zero is cleared")

            elif U_input == "close":
                exit()

            elif U_input.lower() == ("cls"):
                os.system("cls")

            elif U_input.lower() == "descript":
                print("zero is a project by krish, it currently remembers your name,age,birth date even after closer.\nthis will be used for something greater in the future :]")

            elif U_input.lower() == "show ip":
                host_name = socket.gethostname()
                ip_address = socket.gethostbyname(host_name)
                print("host:", host_name)
                print("IP address:", ip_address)

            else:
                print(Fore.RED + "ERROR_404")
                print("could not find "+U_input, " command" + Fore.RESET)




elif boot in options_N:
    print("")
    print("bye :)")
    time.sleep(0.5)

else:
    print(Fore.RED + "ERROR\ninput_not_recognised" + Fore.RESET)
    time.sleep(1)
    os.system('cls')
    time.sleep(1)

    try:
        runpy.run_path("ZERO.py")

    except:
        print("failed to run again\nrestarting...")
        time.sleep(3)
        os.system('cls')
        runpy.run_path("ZERO.py")


