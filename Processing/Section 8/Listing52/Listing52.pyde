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

funnyRectObj = FunnyRect()

def setup():
    size(600,600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRectObj.setSize(50)

def draw():
    background(255)
    fill(50)
    funnyRectObj.setCenter(mouseX, mouseY)
    funnyRectObj.render()
