import pyautogui as mouse

# hotkeys win
mouse.hotkey('win', 'r')
mouse.sleep(1)

# search notepad and open
mouse.typewrite('notepad')
mouse.press('enter')
mouse.sleep(1)

# write
mouse.typewrite('Hi, my name is Edgar')
mouse.sleep(1)

# get open window
action = mouse.getActiveWindow()
mouse.sleep(1)

# close window
action.close()
mouse.sleep(1)

# action close
mouse.press('tab')
mouse.sleep(2)
mouse.press('enter')

