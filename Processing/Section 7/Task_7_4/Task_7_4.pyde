def setup(): 
    size(500,500)
    smooth()
    background(255)
    strokeWeight(1)
    
    
counter = 0
counter1 = 0
cx = 250
cy = 250
cRadius = 10


def draw():
    global counter,counter1,cRadius
    
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    
    x1 = nx - sin(counter)*20
    y1 = ny - cos(counter)*20
    x2 = nx + sin(counter)*20
    y2 = ny + cos(counter)*20
    
    fill(random(0,255), random(0,255),random(0,255))
    ellipse(x1, y1, x2/10, y2/10)
    
    
    counter +=0.1
    if counter > 2*PI:
        counter = 0
    
    counter1 +=0.01
    cRadius += counter/50
    
    if counter1 > 2*PI:
        counter1 = 0
