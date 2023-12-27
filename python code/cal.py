import os
import runpy
print("running program_cal")
print("select one:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
cal_answer=input("insert number here:")

if cal_answer==("1"):
        a=input("v1:")
        b=input("v2:")
        print("answer="+str(int(a)+int(b)))
        reset=input("reset?:")

elif cal_answer==("2"):
             a=input("v1:")
             b=input("v2:")
             print("answer="+str(int(a)-int(b)))
             reset=input("reset?:")

elif cal_answer==("3"):
             a=input("v1:")
             b=input("v2:")
             print("answer="+str(int(a)*int(b)))
             reset=input("reset?:")

elif cal_answer==("4"):
             a=input("v1")
             b=input("v2")
             print("answer="+str(int(a)/int(b)))
             reset=input("reset?:")

             
if reset==("Y"):
    print("ok reseting")
    os.system('cls')
    runpy.run_path("main_menu.py", init_globals=None, run_name=None)
