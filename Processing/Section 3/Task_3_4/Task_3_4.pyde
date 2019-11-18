def setup():
    size(400, 400)
    smooth()
    noLoop()
    background(10)

  
def draw():
    strokeWeight(10)
    stroke(150)
    fill(50)
    rectMode(CORNERS)
    rect(200, 100, 250, 200)
    fill(250)
    rectMode(CORNERS)
    rect(100, 200, 200, 300)
