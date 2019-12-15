add_library('video')
 
def setup():
    global video
    size(640, 480)
    smooth()
    background(0)
    noStroke()
    video = Capture(this, width, height)
    video.start()

    
def draw():
    global video 
    
    if (video.available()):
        video.read()
    
    pushMatrix()
    scale(-1, 1)
    image(video, -width, 0)
    popMatrix()
