rX1 = 0
rY1 = 0
rX2 = 0
rY2 = 0

def setup():
    blendMode(ADD)
    frameRate(60)
    noFill()
    rectMode(CENTER)
    size(200, 200)
    strokeWeight(20)

def draw():
    background(30)
    global rX1, rY1, rX2, rY2
    stroke(200, 100, 100)
    rect(width/2, height/2, rX1, rY1)
    stroke(200, 100, 200)
    rect(width/2, height/2, rX2, rY2)
    if rX1 >= width:
        rX1 = rX1 - width
        rY1 = rY1 - height
    if rX2 >= width:
        rX2 = rX2 - width
        rY2 = rY2 - height
    rX1 += 1
    rY1 += 1
    rX2 += 2.5
    rY2 += 2.5