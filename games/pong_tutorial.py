import turtle

win = turtle.Screen()
win.title("Pong by @rickyg3")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# play with these numbers for display
ball.dx = 0.09
ball.dy = 0.09


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

# Main Game Loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDER

    # Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # Bot
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
