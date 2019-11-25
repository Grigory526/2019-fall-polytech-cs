def setup():
    global img0,img1,img2,img3
    background(100)
    smooth()
    img0 = loadImage("000.jpg")
    img1 = loadImage("001.jpg")
    img2 = loadImage("002.jpg")
    img3 = loadImage("003.jpg")
    size(720, 500)
    

def draw():
    global img0,img1,img2,img3
    background(100)
    image(img0 , 0, 0)
    image(img1 , mouseX * 0.7 - 150, 100)
    image(img2 , 0, 0)
    image(img3 , width - mouseX * 1.5, 35)
