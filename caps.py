##import pyautogui
##
##
from win32api import GetKeyState 
from win32con import VK_CAPITAL 
import pyautogui

#ctypes.WinDLL('user32'); 
#user32.GetKeyState.restype = ctypes.c_short

def getCapsState():
##    import ctypes
##    hllDll = ctypes.WinDLL ("User32.dll")
##    VK_CAPITAL = 0x14
##    return hllDll.GetKeyState(VK_CAPITAL)

    if GetKeyState(VK_CAPITAL) == 1:
        print ("CAPS Lock is on.")
        return True
    elif GetKeyState(VK_CAPITAL) == 0:
        print ("CAPS Lock is off.")
        return False



def operations():
    pyautogui.moveTo(270,893,1)
    pyautogui.click()
    pyautogui.PAUSE = 2
    pyautogui.hotkey('alt','tab')
    pyautogui.moveTo(947,411,0.2)
    pyautogui.click()
    pyautogui.typewrite('pi100035', interval=0.02)
    pyautogui.press('tab')
    pyautogui.typewrite('tere20', interval=0.02)
    pyautogui.moveTo(659,476,0.2)
    pyautogui.click()
    pyautogui.moveTo(795,606,0.2)
    pyautogui.click()
    pyautogui.moveTo(652,423,0.2)
    pyautogui.click()


def main():
    if getCapsState():
        pyautogui.hotkey('capslock')
    #getCapsState()
        
if __name__ == '__main__':
    main()
