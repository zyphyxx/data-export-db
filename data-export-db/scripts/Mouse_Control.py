import pyautogui as mouse

# await
mouse.sleep(2)

# print position
print(mouse.position())

# move
mouse.moveTo(x=-429, y=634)

# click
mouse.doubleClick(x=-429, y=634)

# await
mouse.sleep(2)

# write
mouse.typewrite('excel')



