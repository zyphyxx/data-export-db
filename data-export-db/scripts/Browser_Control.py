import pyautogui as mouse

# prep
mouse.sleep(2)
print(mouse.position())

# open browser
mouse.doubleClick(x=37, y=130)
mouse.sleep(2)

# search google
mouse.typewrite('https://www.google.com/')
mouse.press('enter')
mouse.sleep(2)

# search dolar today
mouse.typewrite('dolar hoje')
mouse.press('enter')
mouse.sleep(2)


