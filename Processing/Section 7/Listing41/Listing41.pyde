cx = 250
cy = 250
cRadius = 200
counter=0
counter1=0

def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(1)


def draw(): 
    global counter,counter1,cRadius
    stroke(0, 30)

    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    
    x1 = nx - sin(counter)*200
    y1 = ny - cos(counter)*200
    x2 = nx + sin(counter)*200
    y2 = ny + cos(counter)*200

    line(x1 , y1 , x2 , y2)
    
    counter += 0.1
    if (counter > 2*PI): 
        counter = 0
    
    counter1+=0.01
    
    if (counter1 > 2*PI):
        counter1 = 0


def keyPressed():
    if (key== "s"):
        saveFrame(" myProcessing .png")
