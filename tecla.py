import keyboard
import time

while True:
    
    if keyboard.is_pressed('a'):
        print ("A")        
        time.sleep(.1)
    if keyboard.is_pressed('b'):
        print ("b")        
        time.sleep(.1)

