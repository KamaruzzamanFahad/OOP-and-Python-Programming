import pyautogui
number = input('enter a number: ') 
for i in range(int(number)):
    for j in range(i + 1):
     pyautogui.write( "#", interval=0.1) 
    pyautogui.press('enter')
