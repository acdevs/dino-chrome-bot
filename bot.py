from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
import numpy as np
pyautogui.alert('Hi I\'m a Chrome Dino Bot!')
print('INITIALISING...')
for i in range(3,0,-1):
        time.sleep(1)
        print(i)
class cordinates(): 
        # coordinates of replay button to start the game 
        replaybutton =(342, 243)
        # this coordinates represent the top-right coordinates 
        # that will be used to define the front box 
        dinasaur = (146, 268)
        
def restartGame(): 

        # using pyautogui library, we are clicking on the 
        # replay button without any user interaction 
        pyautogui.click(cordinates.replaybutton)
        pyautogui.keyDown('Up')
        pyautogui.keyUp('Up')
        # we will keep our Bot always down that 
        # will prevent him to get hit by bird 
        ###pyautogui.keyDown('down') 

def press_space():
        # releasing the Down Key 
        ###pyautogui.keyUp('down')
        # pressing Space to overcome Bush 
        pyautogui.keyDown('space') 

        # so that Space Key will be recognized easily 

        # printing the "Jump" statement on the 
        # terminal to see the current output 
        print("Whew! It's there ! jump")

        # releasing the Space Key 
        pyautogui.keyUp('space') 

        # again pressing the Down Key to keep my Bot always down 
        ###pyautogui.keyDown('down')
        
##def press_Down():
##       
##        # releasing the Down Key 
##        ###pyautogui.keyUp('down')
##        # pressing Space to overcome Bush 
##        pyautogui.keyDown('down') 
##
##        # so that Space Key will be recognized easily 
##        # printing the "Jump" statement on the 
##        # terminal to see the current output 
##        print('Whew! that\'s bird. Dunk!')
##        
##        # releasing the Space Key 
##        pyautogui.keyUp('down')
##        
##        # again pressing the Down Key to keep my Bot always down 
##        ###pyautogui.keyDown('down') 

def lowGrab(): 
        # defining the coordinates of box in front of dinosaur 
        box = (cordinates.dinasaur[0]+150, cordinates.dinasaur[1], 
                cordinates.dinasaur[0]+170, cordinates.dinasaur[1]+5) 

        # grabbing all the pixels values in form of RGB tupples 
        image = ImageGrab.grab(box) 

        # converting RGB to Grayscale to 
        # make processing easy and result faster 
        grayImage = ImageOps.grayscale(image) 

        # using numpy to get sum of all grayscale pixels 
        a = np.array(grayImage.getcolors()) 

        # returning the sum 
        print('Looking') 
        return a.sum() 
        
##def highGrab(): 
##        # defining the coordinates of box in front of dinosaur 
##        box = (cordinates.dinasaur[0]+150, cordinates.dinasaur[1]-30, 
##                cordinates.dinasaur[0]+170, cordinates.dinasaur[1]-20) 
##
##        # grabbing all the pixels values in form of RGB tupples 
##        image = ImageGrab.grab(box) 
##
##        # converting RGB to Grayscale to 
##        # make processing easy and result faster 
##        grayImage = ImageOps.grayscale(image) 
##
##        # using numpy to get sum of all grayscale pixels 
##        a = np.array(grayImage.getcolors()) 
##
##        # returning the sum 
##        print(a.sum()) 
##        return a.sum()        

# function to restart the game
reactTime=0.15
restartGame()
while True: 
        # 435 is the sum of white pixels values of box. 
        # You may get different value is you are taking bigger 
        # or smaller box than the box taken in this article. 
        # if value returned by "imageGrab" function is not equal to 435, 
        # it means either bird or bush is coming towards dinosaur 
        if(lowGrab() != 355):
                if reactTime>0.01:
                        reactTime-=0.002
                time.sleep(reactTime)
                press_space()
##        elif(highGrab() != 455):
##                press_Down()
                

