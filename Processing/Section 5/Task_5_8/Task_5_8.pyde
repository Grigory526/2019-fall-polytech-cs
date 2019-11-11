def setup():
    size(500, 500)
    smooth()
    background(255)
    noStroke()
    noLoop()

def draw():
    for i in range(10):
        for k in range(5):
            fill(i*20)
            rect(i*40+50,(2*k-1)*40+75, 35, 35)
            fill(180-i*20)
            rect(i*40+50,2*k*40+75,35,35)
        
        
            
            
