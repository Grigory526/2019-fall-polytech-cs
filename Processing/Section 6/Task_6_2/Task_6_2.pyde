def setup(): 
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(1)
    
i = 0
k = 1
flug = 1

def upDate():
    global i
    global k
    i = i + k
    if(i == 255):
        k=-1
    
    if(i == 0):
        k=1

def draw():
    stroke(i, 20)
    if(flug == 1):
        myRandom = random(-70,70)
        myY1 = mouseY - random(0,500)
        myY2 = mouseY + random(0,500)
        line (0, myY1 , 500, myY2)
        upDate()
