# Simple Pong game - Tutorial by freeCodeCamp.org 

import turtle
import winsound

#Configuraciones de la ventana

Window = turtle.Screen()
Window.title("Pong Game")
Window.bgcolor("black")
Window.setup(width = 800, height = 600)
Window.tracer(0)




#Goals
goalsA = 0
goalsB = 0


#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")    
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5,stretch_len=0.5)
paddle_A.penup()
paddle_A.goto(-350,0)

#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")    
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5,stretch_len=0.5)
paddle_B.penup()
paddle_B.goto(350,0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")    
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

#Pen 

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {goalsA}   Player B: {goalsB}", align = "center", font = ("Courier",24,"normal"))

#Function

def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)



#Keyboar biding
Window.listen()
Window.onkeypress(paddle_A_up,"w")
Window.onkeypress(paddle_A_down,"s")
Window.onkeypress(paddle_B_up,"Up")
Window.onkeypress(paddle_B_down,"Down")
#Main game loop

while True:
    Window.update()
  

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if paddle_A.ycor() > 240:
        paddle_A.sety(240)

    if paddle_A.ycor() < -240:
        paddle_A.sety(-240)

    if paddle_B.ycor() > 240:
        paddle_B.sety(240)       

    if paddle_B.ycor() < -240:
        paddle_B.sety(-240)        
         
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=1
        goalsA = goalsA + 1 #Goal A
        pen.clear()
        pen.write(f"Player A: {goalsA}   Player B: {goalsB}", align = "center", font = ("Courier",24,"normal"))
        winsound.PlaySound("festejo.wav",winsound.SND_ASYNC)
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=1
        goalsB = goalsB + 1 #Goal B
        pen.clear()
        pen.write(f"Player A: {goalsA}   Player B: {goalsB}", align = "center", font = ("Courier",24,"normal"))
        winsound.PlaySound("festejo.wav",winsound.SND_ASYNC)
    

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 

    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 