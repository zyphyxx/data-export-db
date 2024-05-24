
import pyautogui as options

result = options.confirm('Choose de Options', buttons=['excel', 'word', 'notepad'])

if result == 'excel':

    # hotkeys
    options.hotkey('win', 'r')
    options.typewrite('excel')
    options.press('enter')
    options.sleep(2)

    # print(options.position())
    options.moveTo(x=265, y=252)
    options.sleep(1)
    options.click(x=265, y=252)

    options.typewrite('hello world')

elif result == 'word':
    print('word')
else:
    print('notepad')
