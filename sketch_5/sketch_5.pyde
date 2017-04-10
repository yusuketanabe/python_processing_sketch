x = 0
y = 5
counter = 0
r = 50
g = 50
b = 50

def setup():
    size(100, 100)
    noStroke()
    background(210)

def draw():
    pass

def keyPressed():
    global x, y, counter, r, g, b
    if key == 'r':
        r = 200
        g = 100
        b = 100
    elif key == 'g':
        r = 100
        g = 200
        b = 100
    elif key == 'b':
        r = 100
        g = 100
        b = 200
    else:
        r = 50
        g = 50
        b = 50
    fill(r, g, b)
    rect(x, y, 20, 10)
    x += 10
    y += 10
    counter += 1
    if counter == 10:
        x = 0
        y = 5
        counter = 0
        background(210)