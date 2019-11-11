1-ая вариация
 
def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
    
cx=350
cy=370
cRadius=20
counter1=0
counter=0

def oneLineDraw(ncx , ncy):
    x1 = ncx - sin(counter1)*(700)
    y1 = ncy - cos(counter1)*(700)
    x2 = ncx + sin(counter1)*(700)
    y2 = ncy + cos(counter1)*(700)
    line (x1 , y1 , x2 , y2)
    

def draw():
    global counter,counter1,cx,cy,nx,ny,cRadius
    stroke(191,115,115,10)
    
    
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    
    x1 = nx - sin(counter)*(20)
    y1 = ny - cos(counter)*(20)
    x2 = nx + sin(counter)*(20)
    y2 = ny + cos(counter)*(20)

    oneLineDraw(x2 , y2)
    oneLineDraw(x1 , y1)

    counter += 0.1
    if (counter > 2*PI):
        counter = 0
    
    
    counter1 += 0.01
    cRadius += counter /20
    
    if (counter1 > 2*PI):
        counter1 = 0
        
        
2-ая вариация
        
def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
    
cx=350
cy=370
cRadius=20
counter1=0
counter=0

def oneLineDraw(ncx , ncy):
    x1 = ncx - sin(counter1)*(700)
    y1 = ncy - cos(counter1)*(700)
    x2 = ncx + sin(counter1)*(700)
    y2 = ncy + cos(counter1)*(700)
    line (x1 , y1 , x2 , y2)
    

def draw():
    global counter,counter1,cx,cy,nx,ny,cRadius
    stroke(191,115,115,10)
    
    
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    
    x1 = nx - sin(counter)*(20)
    y1 = ny - cos(counter)*(20)
    x2 = nx + sin(counter)*(20)
    y2 = ny + cos(counter)*(20)

    oneLineDraw(x2 , y2)
    oneLineDraw(x1 , y1)

    counter += 0.1
    if (counter > 2*PI):
        counter = 0
    
    
    counter1 += 0.01
    cRadius += counter /20
    
    if (counter1 > 2*PI):
        counter1 = 0
