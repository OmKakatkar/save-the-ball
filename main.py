import turtle
import time
import sys

# Set the default window properties
window = turtle.Screen()
window.bgcolor("Black")
window.setup(500, 500)
window.title("SAVE THE BALL")
window.tracer(0)

multiplier = 100
score = 0

# Create a board
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.shapesize(stretch_wid=1, stretch_len=3)  # Width = 10, Length = 30
board.pu()
board.goto(1.5, -230)  # Reference is bottom-right corner

# Create a ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.pu()
# delta change for ball
dx = 1
dy = -1

# Create a pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.ht()
pen.pu()
pen.goto((100, 200))
pen.pd()
pen.write(f"Score : {score}", font=("Arial", 16, "normal"))
pen.pu()


def board_left():
    """
    Moves the board to left
    """
    x = board.xcor()
    if x >= -210:
        x -= 20
        board.setx(x)


def board_right():
    """
    Moves the board to right
    """
    x = board.xcor()
    if x <= 210:
        x += 20
        board.setx(x)


# Keyboard binding
window.listen()
window.onkeypress(board_left, "Left")
window.onkeypress(board_right, "Right")

last_time = time.perf_counter()
try:
    while True:

        current_time = time.perf_counter()
        elapsed_time = current_time - last_time
        last_time = current_time

        window.update()

        ball.sety(ball.ycor() + dy*elapsed_time*multiplier)
        ball.setx(ball.xcor() + dx*elapsed_time*multiplier)

        if ball.ycor() > 240:
            ball.sety(240)
            dy *= -1

        elif ball.ycor() < -240:
            ball.goto(0, 0)
            score = 0
            multiplier = 100
            pen.goto((100, 200))
            pen.clear()
            pen.pd()
            pen.write(f"Score : {score}", font=("Arial", 16, "normal"))
            pen.pu()

            dy *= 1

        if ball.xcor() > 240:
            ball.setx(240)
            dx *= -1

        elif ball.xcor() < -240:
            ball.setx(-240)
            dx *= -1

        if (-220 > ball.ycor() > -240) and (
                (ball.xcor() < board.xcor() + 20) and (ball.xcor() > board.xcor() - 20)):
            ball.sety(-220)
            dy *= -1
            dx *= 1
            score += 1
            if score % 5 == 0:
                multiplier += 100
            else:
                multiplier += 50
            pen.goto((100, 200))
            pen.clear()
            pen.pd()
            pen.write(f"Score : {score}", font=("Arial", 16, "normal"))
            pen.pu()
except Exception as e:
    pass
sys.exit()
