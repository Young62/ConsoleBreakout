from msvcrt import getch
import random
import os

screenWidth=35
screenHeight=20

ballX=5
ballY=5
ballVX=1
ballVY=1

brickX=random.randrange(5,30)
brickY=random.randrange(5,10)
brickWidth=random.randrange(3,5);

paddleX=(35/2)-2.5
paddleY=screenHeight-2
paddleWidth=5
control=''

print("Hold W-A-S-D to move the paddle. \nThe @-bricks will spawn randomly as you hit them. \nBeing too aggressive will cause you to miss. \nPress the controls to start.")
while 1==1:
    #update
    #######

    #controls
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
        exit()
    control=''

    #ball behavior
    if ballX<=1 or ballX>=screenWidth-1:
        ballVX=-ballVX

    if (ballX>paddleX and ballX<(paddleX+paddleWidth) and ballY==paddleY-1):
        ballVY=-ballVY
    if ballY<=1:
        ballVY=-ballVY
    if ballY>screenHeight:
        exit()

    if ( ballX>=(brickX-1) and ballX<(brickX+brickWidth+1) ) and (ballY>=brickY-1 and ballY<=brickY+1):
        ballVY=-ballVY
        ballVX=-ballVX
        brickX=random.randrange(5,30)
        brickY=random.randrange(5,10)

    ballX=ballX+ballVX
    ballY=ballY+ballVY



    #render
    #######
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

    #capture key input for next loop
    ################################
    #control=str(getch())
