import pyautogui
import time

pyautogui.keyDown('win')
pyautogui.press('5')
pyautogui.keyUp('win')
time.sleep(2)
pyautogui.press(['down', 'down'])
pyautogui.press('enter')
pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down',
                'down', 'down', 'down', 'down', 'down', 'down', 'down'])
pyautogui.press('enter')
time.sleep(1)
pyautogui.press(['down', 'down'])
pyautogui.press('delete')
time.sleep(1)
pyautogui.keyDown('shift')
pyautogui.press('f10')
pyautogui.keyUp('shift')
time.sleep(2)
pyautogui.press('s')
pyautogui.press('enter')
pyautogui.moveTo(1268, 888, duration=0.3)
pyautogui.dragTo(1268, 888, duration=0.1, button='left')
time.sleep(2)
pyautogui.typewrite('git clone https://github.com/Jason021356/Tech-Chat.git')
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite('exit')
pyautogui.press('enter')
time.sleep(1)
pyautogui.keyDown('alt')
pyautogui.press('f4')
pyautogui.keyUp('alt')