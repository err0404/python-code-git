from pynput.keyboard import Key,Controller
import time
input()
print("close to end the suffering")
keyboard=Controller()

time.sleep(3)
keyboard.type('Huh?')
time.sleep(5)

with keyboard.pressed(Key.ctrl):
    keyboard.press('c')
    keyboard.release('c')

while 1==1:
 for i in range(450):
  with keyboard.pressed(Key.ctrl):
     keyboard.press('v')
     time.sleep(0.0003)
     keyboard.release('v')

 keyboard.press(Key.enter)


