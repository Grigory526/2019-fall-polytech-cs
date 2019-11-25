PShape[] borders;
3 int vertexCount
4 float sinCounter = 0
5 float eSize = 15

def setup():
8 size(600, 300)
9 smooth()
10 background(0)
11 noStroke()
12 PShape drawingSVG = loadShape("m1.svg ")
13 borders = new PShape[6]
14 borders[0] = drawingSVG.getChild(" path4166 ")
15 borders[1] = drawingSVG.getChild(" path4168 ")
16 borders[2] = drawingSVG.getChild(" path4170 ")
17 borders[3] = drawingSVG.getChild(" path4172 ")
18 borders[4] = drawingSVG.getChild(" path4174 ")
19 borders[5] = drawingSVG.getChild(" path4176 ")

defraw(){
23 background(0);
24 for (int j = 0; j < 6; j++){
25 vertexCount = borders[j].getVertexCount();
26 for (int i = 0; i < vertexCount; i+=1){
27 float vx = borders[j].getVertexX(i) + 50;
203
28 float vy = borders[j].getVertexY(i) - 750;
29 float ellipseColor = map(sin(sinCounter) ,-1,1,0,255);
30 fill(ellipseColor);
31 float ellipseSize = map(i,0,vertexCount ,eSize ,eSize
+40);
32 ellipse(vx, vy , ellipseSize , ellipseSize);
33
34 if(sinCounter < TWO_PI){
35 float cv = map(mouseX ,0,width ,0,1);
36 sinCounter+=cv;
37 } else {
38 sinCounter = 0;
39 }
40 }
41 }
42 // filter (BLUR , 1)
