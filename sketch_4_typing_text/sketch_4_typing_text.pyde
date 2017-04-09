letter = ''

def setup():
    size(200, 200)
    stroke(200, 100, 100)
    strokeWeight(2)
    textSize(32)
    frameRate(8)
    
def draw():
    global letter
    background(30)
    if keyPressed == True:
        if key == BACKSPACE:
            if len(letter) > 0:
                letter = letter[0:len(letter)-1]
        elif textWidth(letter+key) < width:
            letter = letter + key
            lCount = letter.count('p')
            if lCount % 2 == 0:
                fill(200, 200, 100)
            else:
                fill(100, 200, 200)
    cursorPosition = textWidth(letter) + 3
    line(cursorPosition, height/2-textAscent(), cursorPosition, height/2+textDescent())
    text(letter, 0, 100)
    