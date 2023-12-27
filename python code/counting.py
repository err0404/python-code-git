import time
import runpy
import os
print("input the number you want to count up to")
b=input()
print("now the time between each number")
c=input()


print("..............................................................")

for a in range(int(b)):
    time.sleep(float(c))
    print(a+1)

print("..............................................................")

print("there you go your answer is")
print(int(b))
print("happy?")
print("would you like to head back to main menu?")
reset=input("")
if reset==("Y"):
    print("ok")
    os.system('cls')
    runpy.run_path("main_menu.py", init_globals=None, run_name=None)
