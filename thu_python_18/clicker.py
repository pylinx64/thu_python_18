import pyautogui
import time

# перемещение x, y
pyautogui.moveTo(320, 748)

# имитирует клик левой клавиши
pyautogui.click()

pyautogui.moveTo(400, 690)
pyautogui.click()

while True:
    # имитирует текст (набор на клаве)
    pyautogui.typewrite('sadasdas')
    
    # имитирует нажатие и отпускание клавиши
    pyautogui.press("enter")
    time.sleep(0.15)
