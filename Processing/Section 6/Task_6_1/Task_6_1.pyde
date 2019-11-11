Первая часть задания
 
def setup ():
    size(500, 500)
    smooth()
    strokeWeight(1)
    background(0)

i = 0
k = 1

def draw ():
    global i
    global k
    stroke(i, 20)
    line(mouseX,mouseY,random(0,500),0)
    i = i + k
    if(i == 255):
        k=-1

    if(i == 0):
        k=1
        
Вторая часть задания

def setup ():
    size(500, 500)
    smooth()
    strokeWeight(1)
    background(0)

i = 0
k = 1

def draw ():
    global i
    global k
    stroke(i, 20)
    line(mouseX,mouseY,random(0,500),random(0,500))
    i = i + k
    if(i == 255):
        k=-1

    if(i == 0):
        k=1



        
        
        
        
        
        
        
        
