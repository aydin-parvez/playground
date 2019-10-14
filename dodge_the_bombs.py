import tkinter
import fun
gameOver = False
score = 0
squaresToClear = 0


def play_bombdoger():
    create_bombfeild(bombfeild)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()