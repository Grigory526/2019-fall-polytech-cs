i=0
k=0

def setup():
    size(500, 500)
    smooth()
    strokeWeight(1)
    background(0)
    
    
def draw():
    global i,k
    stroke(i, 20)
    line(mouseX , mouseY , random(0,500), 500)
    i +=k
    if(i == 255):
        k=-1
    
    if(i == 0):
        k=1
        
def keyPressed():
    if (key=="s"):
        saveFrame("myProcessing.png")
