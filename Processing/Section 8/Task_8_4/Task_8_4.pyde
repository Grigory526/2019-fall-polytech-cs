centerX = 0
centerY = 0 
angle = 0
fsize  = 0
weight = 0
counter = 0
centerX=250
centerY=250
angle= 0
size1= 150
weight = 1

class MyEllipse():
    
    def MyEllipse():
        centerX=cX
        centerY=cY
        angle=cA
        size=eS
        weight=Ew

    def render(self, size1):
        fill(200, size1/20)
        x1 = centerX + cos(counter)*100 - cos(angle)*size1/2
        y1 = centerY + sin(counter)*100 + sin(angle)*size1/2
        
        stroke(250, 100)
        strokeWeight(weight)
        ellipse(x1,y1,size1,size1)
        
ellipseObj = MyEllipse()
        
def setup():
    size(500,500)
    smooth()
    background(10)
    ellipseOjb=(250,250,0,150,1)
    
def draw():
    global counter
    counter += 0.01
    if (counter > TWO_PI):
        counter = 0
        
    ellipseObj.render(sin(counter*4)*mouseX)
