import webbrowser
import pyautogui
import time
from PIL import Image

img = Image.open("mk.png")

dataset ={
   "7045525200" : "hello!!",
  "79892663226" : "good morning!!"
}


for num,msg in dataset.items():
  

    b="https://wa.me/91"+str(num)
    webbrowser.open(b)
    # time.sleep(10)




    #for continue to chat
    time.sleep(20)
    pyautogui.click(952,445)

    #for set use whatsapp web
    time.sleep(2)
    pyautogui.click(954,541)



    #for type msg
    time.sleep(10)
    pyautogui.click(862,969) 
    pyautogui.typewrite(msg)

    #for send msg
    time.sleep(2)
    pyautogui.click(1790,970)

    time.sleep(20)




