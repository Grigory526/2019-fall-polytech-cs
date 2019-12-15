add_library('video')

mySize = 0

def setup():
    global video
    size(640, 480)
    smooth()
    background(0)
    noStroke()
    video = Capture(this, width, height)
    video.start()

    
def draw():
    global mySize
    
    if (video.available()):
        video.read()
    
        if (mouseX > 20 and mouseY > 20):
            if (mouseX < width - 20 and mouseY < height - 20):
                if (frameCount % 5 == 0):
                    blendMode(BLEND)
                    noTint()
                    fill(0, 10)
                    rect(0, 0, width, height)
                else:
                    blendMode(ADD)
            x = mouseX + random(-100, 100)
            y = mouseY + random( -100, 100)
            wx = 20 + random(0,200)
            wy = 20 + random(0,200)
            tmpImg = video.get(mouseX, mouseY, int(wx), int(wy))
            tint(random(50, 255), random(50, 255), random(50, 255))
            image(tmpImg, x, y)
