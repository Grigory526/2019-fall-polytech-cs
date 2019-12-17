def setup():
    global drawingSVG
    background(100)
    smooth()
    strokeWeight(1)
    stroke(600,600)
    drawingSVG = loadShape("data/drawing3.svg")
    size(800, 400)
    
def shapeDraw(my):
    global drawingSVG 
    
    for i in range(0, my.getVertexCount()):
        vx = my.getVertexX(i) + 10
        vy = my.getVertexY(i) + 30
        lx1 = vx + random(-150, 150)
        ly1 = vy + random(-150, 150)
        lx = mouseX + random(-150, 150)
        ly = mouseY + random(-150, 150)
        mCursor = map(mouseX, 0, width, 0, 255)
        stroke(mCursor, 10)
        noFill()
        bezier(vx, vy, lx, ly, lx1, ly1, vx, vy)
    

def draw():
    global drawingSVG
    fill(10, 10)
    drawingSVG.disableStyle()
    shape(drawingSVG, 0, 0)
    
    border = drawingSVG.getChild("path1057")
    shapeDraw(border)
    
    border1 = drawingSVG.getChild("path1059")
    shapeDraw(border1)
    
    border2 = drawingSVG.getChild("path1061")
    shapeDraw(border2)
    
    border3 = drawingSVG.getChild("path1063")
    shapeDraw(border3)
