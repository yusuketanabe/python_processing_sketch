import math

theta = 0

def setup():
    size(200, 200)
    noFill()
    stroke(150, 100, 200)
    strokeWeight(4)
    
def draw():
    background(30)
    global theta
    theta += 0.15
    x = 50*math.sin(theta)+100
    y = 50*math.cos(theta)+100
    ellipse(100, 100, x, y)