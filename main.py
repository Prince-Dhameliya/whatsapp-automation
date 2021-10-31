import webbrowser
import pyautogui
import time

person_name ='Prince' #input('enter a name whome you wan to sent a messages : ')
type_msg = 'efejefewf eeeeeeeeeeeeeeeeeeee efffffffffffffffffffffv                   d ddddddddddddddddddddee         feefefef'#input('enter msg whatever you want tom send : ')

webbrowser.open('https://web.whatsapp.com/')
time.sleep(10)
#print(pyautogui.position())

pyautogui.click(286,259)
pyautogui.typewrite(person_name)

time.sleep(5)
pyautogui.click(291,427) #163 259

time.sleep(3)
pyautogui.click(862,969) 
pyautogui.typewrite(type_msg)


time.sleep(2)
pyautogui.click(1790,970)



