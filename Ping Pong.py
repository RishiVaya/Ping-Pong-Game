import turtle

wn = turtle.Screen()
wn.title("New Game!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)                          #Stops the window from updating. Improves game speed.


## Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

## Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

## Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("red")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

## Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))

score_a = 0
score_b = 0


## Functions

def pad_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def pad_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def pad_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def pad_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    
### KEYBOARD BINDING

wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

## Main game loop

while True:
    wn.update()

    ## Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ## Border Check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor()>390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor()<-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))



    ## Paddle and ball collision
    if ball.xcor()>332 and ball.xcor()<348 and (ball.ycor() < (paddle_b.ycor() + 40)) and (ball.ycor() > (paddle_b.ycor() - 40)):
        ball.dx *= -1

    if ball.xcor()<-332 and ball.xcor()>-348 and (ball.ycor() < (paddle_a.ycor() + 40)) and (ball.ycor() > (paddle_a.ycor() - 40)):
        ball.dx *= -1



