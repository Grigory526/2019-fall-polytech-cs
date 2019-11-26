lg_diam = 500 * 0.55
lg_rad = lg_diam/2
lg_circ = PI * lg_diam
cx = 500/2
cy = 400/2

def setup():
    background(100)
    smooth()
    size(500,400)
    colorMode(HSB)
    
def draw():
    global lg_rad
    fill(0,10)
    rect(0,0,width,height)
    nbr_circles =int( map(mouseX, 0, width,6,50))
    sm_diam = (lg_circ/nbr_circles)
    myColor = map(mouseY,0,height, 150, 255)
    
    filter(BLUR, 3)
    fill(myColor,180, 190, 100)
    
    for i in range (1, nbr_circles+1):
        angle = i * TWO_PI / nbr_circles
        x = cx + cos(angle) * lg_rad
        y = cy + sin(angle) * lg_rad
        ellipse(x,y,sm_diam, sm_diam)
        
def keyPressed():
    if (key== "s"):
        saveFrame("myProcessing " + str(frameCount) + ".jpg ")
