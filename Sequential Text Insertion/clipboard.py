from pynput import keyboard
import pyautogui as pygui
from tkinter import *
import sys

root=Tk()
texts = []
cancelCombination = keyboard.Key.esc
pasteCombination = keyboard.Key.insert

controller = keyboard.Controller()


i = 0
def on_press(key):
    global i,cancelCombination,pasteCombination,controller
    if(key == cancelCombination):
        sys.exit()
    if(key == pasteCombination):
        controller.type(texts[i])
        i = i+1
        if(i>=len(texts)):
            sys.exit()


def retrieve_input():
    global texts
    inputValue=textBox.get("1.0","end-1c")
    texts = inputValue.split('\n')
    print("Press insert to paste")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()



textBox=Text(root, height=20, width=100)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Copy", 
                    command=lambda: retrieve_input())
buttonCommit.pack()

mainloop()