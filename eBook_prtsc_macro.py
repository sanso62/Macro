from pynput.keyboard import Key, Controller
import time

keyboard=Controller()
n_page=int(input()) # Input the number of pages
time.sleep(10)
for i in range(n_page):
    # Print screen
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.print_screen)
        keyboard.release(Key.print_screen)
    time.sleep(2)
    
    # Go to the next page
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(5)
    
