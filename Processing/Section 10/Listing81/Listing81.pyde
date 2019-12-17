def setup():
    global drawingSVG
    background(100)
    smooth()
    strokeWeight(1)
    size(600,600)
    drawingSVG = loadShape("data/drawing3.svg")
    
def draw():
    global drawingSVG
    fill(10, 0)
    rect(0,0,width, height)
    mCursor = map(mouseX, 0, width, 100, 155)
    fill(10, 15)
    drawingSVG.disableStyle()
    shape(drawingSVG,0,0)
    
    border = drawingSVG.getChild("path900")
    for i in range (border.getVertexCount()):
        vx = border.getVertexX(i) +100
        vy = border.getVertexY(i) +75
        lx = vx + random(-150, 150)
        ly = vy + random(-150, 150)
        lineColor = mCursor + random(-100, 100)
        stroke(lineColor, 100)
        line(vx, vy, lx, ly)
        fill(200, 50)
        noStroke()
        ellipse(vx, vy, 3 ,3 )
        
    border1 = drawingSVG.getChild("path902")
    for i in range(border1.getVertexCount()):
        vx = border1.getVertexX(i) +100
        vy = border1.getVertexY(i) +75
        lx = vx + random(-150, 150)
        ly = vy + random(-150, 150)
        lineColor = mCursor + random(-100, 100)
        stroke(lineColor, 100)
        line(vx, vy, lx, ly)
        fill(200, 50)
        noStroke()
        ellipse(vx, vy, 3 ,3 )
        
    border2 = drawingSVG.getChild("path904")
    for i in range(border2.getVertexCount()):
        vx = border2.getVertexX(i) +100
        vy = border2.getVertexY(i) +75
        lx = vx + random(-150, 150)
        ly = vy + random(-150, 150)
        lineColor = mCursor + random(-100, 100)
        stroke(lineColor,100)
        line(vx, vy, lx, ly)
        fill(200, 50)
        noStroke()
        ellipse(vx, vy, 3 ,3 )
        
    border3 = drawingSVG.getChild("path906")
    for i in range(border3.getVertexCount()):
        vx = border3.getVertexX(i) +100
        vy = border3.getVertexY(i) +75
        lx = vx + random(-150, 150)
        ly = vy + random(-150, 150)
        lineColor = mCursor + random(-100, 100)
        stroke(lineColor, 100)
        line(vx, vy, lx, ly)
        fill(200, 50)
        noStroke()
        ellipse(vx, vy, 3 ,3 )
