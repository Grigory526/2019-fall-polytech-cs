rotateCounter = 0

def setup():
    global font, font2
    size(600, 600)
    smooth()
    background(0)
    font = loadFont("BookAntiqua-Bold-48.vlw")
    font2 = loadFont("MicrosoftYaHei-Bold-48.vlw")

    
def draw():
    global rotateCounter, font, font2
    filter(BLUR, 3)
    translate(width/2, height/2)
    
    pushMatrix()
    textFont(font, 48)
    rotate(rotateCounter)
    fill(255)
    text("Black", mouseX - width/2, mouseY - height/2)
    popMatrix()
    
    pushMatrix()
    textFont(font2, 48)
    rotate(-rotateCounter * 1.5)
    fill(0)
    text("White", width/2 - mouseX, height/2 - mouseY)
    popMatrix()
    
    rotateCounter += 0.05
