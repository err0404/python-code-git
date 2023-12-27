import time
import os

with open("frames.txt", "r")as file:
    frames = file.read()
    frames = frames.split(".")

input()
while True:
    for frame in frames:
        print(frame)
        time.sleep(0.2)
        os.system("cls")