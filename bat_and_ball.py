import tkinter
import time
from tkinter import messagebox
print("Keep the ball in the air!")

canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="white")

canvas.pack()
bat = canvas.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill="deep pink")
windowOpen = True
score = 0
leftPressed = 0
rightPressed = 0
batSpeed = 6
ballSpeed = 100
ballMoveX = ballSpeed
ballMoveY = -ballSpeed
setBatTop = canvasHeight-40
setBatBottom = canvasHeight-30


def main_loop():
    while windowOpen:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
        if windowOpen:
            check_game_over()


def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1


def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0


def move_bat():
    bat_move = batSpeed*(rightPressed - leftPressed)
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    if (batLeft > 0 or bat_move > 0) and (batRight < canvasWidth or bat_move < 0):
        canvas.move(bat, bat_move, 0)


def move_ball():
    global ballMoveX, ballMoveY, score
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballMoveX < 0 and ballLeft < 0:
        ballMoveX = -ballMoveX
        if ballMoveY < 0 and ballTop < 0:
            ballMoveY = -ballMoveY
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
        score += 1
    if ballMoveY > 0 and setBatTop < ballBottom < setBatBottom:
        (batLeft, ballTop, batRight, batBottom) = canvas.coords(bat)
        if ballRight > batLeft and ballLeft < batRight:
            ballMoveY = -ballMoveY
    canvas.move(ball, ballMoveX, ballMoveY)


def check_game_over():
    global score
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballTop > canvasHeight:
        tkinter.messagebox.askokcancel(message="Score=" + str(score))
        play_again = tkinter.messagebox.askyesno(message="Do you want to play again?")
        if play_again:
            reset()
        else:
            close()


def close():
    global windowOpen
    windowOpen = False
    window.destroy()


def reset():
    global leftPressed, rightPressed
    global ballMoveX, ballMoveY
    global score
    score = 0
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30,  setBatTop)


window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)
reset()
main_loop()