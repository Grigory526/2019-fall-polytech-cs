counter=0
cx = 250
cy = 250
cRadius = 200
mcolor=0

def setup(): 
    size(500, 500)
    smooth()

    background(50)
    strokeWeight(2)
    stroke(250)


def draw():
    global counter,mcolor
    x1 = sin(counter)*cRadius + cx
    y1 = cos(counter)*cRadius + cy
    mcolor += 1
    stroke(mcolor)
    line(cx , cy , x1 , y1)
    counter += 2*PI/255
    
    while counter > 2*PI:
        counter = 0
        mcolor = 0
        background(50)


def keyPressed():
    if (key== "s"):
        saveFrame(" myProcessing .png")
