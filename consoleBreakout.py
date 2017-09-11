from msvcrt import getch
import random
import threading
import time
import sys

screenWidth=30
screenHeight=20
ballX=5
ballY=5
ballVX=1
ballVY=.5
brickX=random.randrange(5,25)
brickY=random.randrange(5,10)
brickWidth=random.randrange(3,5);
paddleX=(35/2)-2.5
paddleY=screenHeight-2
paddleWidth=5
control=''
run=False
threading1=None

def menu():
    # now threading1 runs regardless of user input
    input('Press ENTER to start.\nHold W-A-S-D to move. Q to quit.')
    threading1 = threading.Thread(target=background)
    threading1.daemon = True
    threading1.start()


def controls():
    global paddleX
    global screenWidth
    global screenHeight
    global ballX
    global ballY
    global ballVX
    global ballVY
    global brickX
    global brickY
    global brickWidth
    global paddleX
    global paddleY
    global paddleWidthX

    if getch():
        control=str(getch())
        if control=="b'a'" and paddleX>1:
            paddleX=paddleX-1
        if control=="b'd'" and paddleX<(screenWidth-2-paddleWidth):
            paddleX=paddleX+1
        if control=="b'w'" and paddleY>1:
            paddleY=paddleY-1
        if control=="b's'" and paddleY<screenHeight-2:
            paddleY=paddleY+1
        if control=="b'q'":
            sys.exit()
        control=''
        return True
    else:
        return False

def update():
    global paddleX
    global screenWidth
    global screenHeight
    global ballX
    global ballY
    global ballVX
    global ballVY
    global brickX
    global brickY
    global brickWidth
    global paddleX
    global paddleY
    global paddleWidthX

    #ball behavior
    if ballX<=1 or ballX>=screenWidth-2:
        ballVX=-ballVX

    if (ballX>paddleX and ballX<(paddleX+paddleWidth) and ballY==paddleY-1):
        ballVY=-ballVY
    if ballY<=1:
        ballVY=-ballVY
    if ballY>screenHeight:
        return False

    if ( ballX>=(brickX-1) and ballX<(brickX+brickWidth+1) ) and (ballY>=brickY-1 and ballY<=brickY+1):
        ballVY=-ballVY
        ballVX=-ballVX
        brickX=random.randrange(5,30)
        brickY=random.randrange(5,10)

    ballX=ballX+ballVX
    ballY=ballY+ballVY
    return True

def render():
    for i in range(0,99):
        print(' \n')
    line=''
    for i in range(0,screenHeight):
        if i==paddleY:
            line=line+'|'
            for j in range(1,screenWidth-1):
                if j>=paddleX and j<(paddleX+paddleWidth):
                    line=line+'I'
                else:
                    line=line+' '
            line=line+'|'
        else:
            for j in range(0,screenWidth):
                if (j>=brickX and j<(brickX+brickWidth)) and i==brickY:
                    line=line+'@'
                elif i==ballY and j==ballX :
                    line=line+'*'
                elif j==0 or j==screenWidth-1:
                    line=line+'|'
                elif i==0 or i==screenHeight-1:
                    line=line+'-'
                else:
                    line=line+' '
        line=line+'\n'
        print(line)

def background():
    while True:
        if update()==True:
            time.sleep(0.3)
            update()
            render()
        else:
            print('You lost. Hold Q to quit.')
            exit()

menu()
while True:
    if controls()==True:
        controls()
