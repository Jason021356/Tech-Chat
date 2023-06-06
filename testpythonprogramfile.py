import win32gui,win32con,win32ui
import pyautogui
import time

pyautogui.moveTo(281,37,duration=0.3)
pyautogui.dragTo(281,37,duration=0.1)
pyautogui.dragTo(281,37,duration=0.1)
time.sleep(1)
hwtb = win32gui.FindWindow(None,'Tech Chat網頁版')
left,top,right,bottom = win32gui.GetWindowRect(hwtb)
width = left - top
height = right - bottom
hwtbDC = win32gui.GetWindowDC(hwtb)
mfcDC = win32ui.CreateDCFromHandle(hwtbDC)
saveDC = mfcDC.CreateCompatibleDC()
saveBitmap = win32ui.CreateBitmap()
saveBitmap.CreateCompatibleBitmap(mfcDC,width,height)
saveDC.SelectObject(saveBitmap)
saveDC.BitBlt((0,0),(width,height),mfcDC,(0,win32con.SRCCOPY),96)

saveBitmap.SaveBitmapFile(saveDC,"TechChatFileSystemscreenshot.png")