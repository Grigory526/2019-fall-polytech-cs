def setup():
    size (700,700)
    
ballX = 0
ballY = 0
speedX = random(0,10)
speedY = random(0,10)
hit = 0
miss = 0


def draw():
    
    global ballX,ballY,speedX,speedY,hit,miss
    
    paddle = 1000/(hit+10)
    if(ballX < 0 or ballX > width):
        speedX = -speedX
    if(ballY > height):    
        speedY = -speedY
        distance =abs(mouseX - ballX)
        if(distance < paddle):
            hit +=1
        else:
            miss +=1
    else:
        speedY +=1
            
    ballX += speedX
    ballY += speedY
            
    background(100,200,50)
    fill(200,100,50)
    ellipse(ballX, ballY, 50, 50)
    fill(50, 100, 200)
    rect(mouseX-paddle, height-10, 2*paddle, 10)
        
    fill(0)
    text("Hit: " +str(hit),10,20)
    text("Miss: " +str(miss),10,40)
        
