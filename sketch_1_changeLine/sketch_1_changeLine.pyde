cR = 100
cG = 30
cB = 40
y = 0

def setup():
    size(200, 200)
    strokeWeight(3)

def draw():
    global cR, cG, cB, y
    background(30)
    stroke(cR, cG, cB)
    line(0, y, 200, y)
    y += 1
    print 'Y=', y, 'R=', cR, 'G=', cG, 'B=', cB
    if y >= 200:
        y = 0
        cR += 30
        cG += 30
        cB += 40
        if cR >= 200:
            cR = cR - 200 + 100
        if cG >= 100:
            cG = cG - 100 + 30
        if  cB >= 100:
            cB = cB - 100 + 40