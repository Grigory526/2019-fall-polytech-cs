def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(30)
    noLoop()  

def draw():  
    stroke(20)  
    for i in range (7):
        line(i * 50 + 50 , 200, 200 + (i - 1)*50, 300) 
