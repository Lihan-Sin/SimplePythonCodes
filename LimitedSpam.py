import pyautogui
import time
message = 1
count = int(input("Enter how many times you want to spam: "))
text = input("Enter the text you want to spam: ")

while message <= count:
    time.sleep(0)
    pyautogui.typewrite(text + str( message))
    pyautogui.press("enter")
    time.sleep(0)
    message = message + 1
    