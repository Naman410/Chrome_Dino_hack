import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow from numpy import as array
import time

if __name__=="__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    pyautogui.press("enter")
    l = 552


    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        k = 0

        for i in range(500, l):
            for j in range(620, 670):
                if data[i, j] == 172:
                    pyautogui.press("up")
                    k = 1
                    l=l+2
                    break
            if k == 1:
                break







        '''   
        for i in range(1500, 1550):
            for j in range (900, 950):
                if data[i, j] < 50:
                    for i in range(350, 400):
                        for j in range(620, 700):
                             if  data[i, j] > 150:
                                 hit("up")
                else:
                    for i in range(350, 400):
                        for j in range(620, 700):
                            if data[i, j] < 200:
                                hit("up")

        # print(asarray(image))
        '''
        '''
        for i in range(1500, 1550):
            for j in range(900, 950):
                guess = data[i, j]
                data[i, j] = 0
                print(guess)

        for i in range(350, 400):
            for j in range(620, 700):
                guess = data[i, j]
                data[i, j] = 0
                print(guess)



        image.show()
        break
        '''

