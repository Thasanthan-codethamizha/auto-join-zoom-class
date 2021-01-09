import subprocess
import time
import pyautogui

file = open("info.txt")

text= file.readlines()

meetingid=str(text[0])
pswd=str(text[1])
file.close
def sign_in(meetingid,pswd):
        meetingid=meetingid
        pswd=pswd
        print(meetingid)
        print(pswd)
        subprocess.call("C:\\Users\\n\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        
        time.sleep(3)
        
        join_btn= pyautogui.locateCenterOnScreen(r'F:\\Projects\\P-Projects\\python projects\\zoom_automate\\join.png')
        pyautogui.moveTo(join_btn)
        pyautogui.click()
        time.sleep(5)
        pyautogui.write(meetingid)
        
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.write(pswd)
        pyautogui.press('enter')
        
sign_in(meetingid,pswd)

