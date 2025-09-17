import pyautogui
import time
text = input("Enter your text: ")

while True:
    time.sleep(0)
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    time.sleep(0)