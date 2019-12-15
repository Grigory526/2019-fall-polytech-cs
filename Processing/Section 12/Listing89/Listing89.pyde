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
        if (frameCount %3 == 0):
            blendMode(ADD)
        else:
            blendMode(BLEND)
        myX =int( random(0, width))
        myImg = video.get(myX,0, mySize, height)
        image(myImg, myX, 0)
        mySize =int( random(1, 50))
