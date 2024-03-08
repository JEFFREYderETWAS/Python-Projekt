import pytesseract
import cv2
import pyautogui
import time
#Macht ein screenshot und nimmt sich dem text von screenshot man kann zwischen string und intiter entscheiden


input("etwas:")
time.sleep(11)
screenshot = pyautogui.screenshot()
screenshot.save("test.png")

etwas =input(True)

img = cv2.imread("test.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

test = pytesseract.image_to_string(img)


str_oder_int = input("int or str:")

if str_oder_int == "str":
    print(test)
elif str_oder_int == "int":
    print(test,eval(test))
