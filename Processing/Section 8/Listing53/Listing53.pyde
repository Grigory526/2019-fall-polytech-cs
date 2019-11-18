counter = 0
cx = 0
cy = 0
fsize = 0

class FunnyRect():
    def setCenter(self, x,y):
        self.x = x
        self.y = y

    def setSize(self, size):
        self.size = size

    def render(self):
        rect(self.x, self.y, self.size, self.size)


funnyRect = FunnyRect()
funnyRect1 = FunnyRect()

def setup():
    size(600,600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRect.setSize(50)
    funnyRect1.setSize(50)

def draw():
    global counter
    background(255)
    fill(50)
    
    objX = mouseX +sin(counter)*150
    objY = mouseY +cos(counter)*150
    
    funnyRect.setCenter(mouseX, mouseY)
    funnyRect.render()
    
    funnyRect1.setCenter(objX, objY)
    funnyRect1.render()
    counter +=0.05
