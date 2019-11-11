xCoordinate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 

def setup():
    size(500,500)
    smooth()
    noStroke()
    myInit()
    
    
def myInit():
    for i in range (len(xCoordinate)):
        xCoordinate[i] = 250 + random(-100,100)


def draw():
    background(50)
    for i in range (len(xCoordinate)):
        fill(20)
        ellipse(xCoordinate[i], 250, 5, 5)
        fill(250, 40)
        ellipse(xCoordinate[i], 250, 10*i,10*i)
        
    if (mouseX > width/2):
        myInit()
        
    print( max(xCoordinate))
