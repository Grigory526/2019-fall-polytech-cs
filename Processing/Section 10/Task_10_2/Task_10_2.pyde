def setup():
    global img1,img2
    background(100)
    smooth()
    img1 = loadImage("data/001.jpg")
    img2 = loadImage("data/002.jpg")
    size(784, 600)

coint = 0

def mouseClicked():
    global coint
    if (mouseButton== LEFT):
        coint += 5
        if (coint < 0):
            coint = 0
    if (mouseButton== RIGHT):
        coint -=5
        if(coint >100):
            coint = 100

def draw():

    myTintBO = map(coint, 0, 100 , 0, 255)
    myTintVP = map(coint , 0, 100 , 255, 0)
    
    tint(255, myTintVP)
    image(img1 , 0, 0)
    tint(255, myTintBO)
    image(img2 , 0, 0)
