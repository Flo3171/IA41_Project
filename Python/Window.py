from tkinter import *
from Case import Case
from Board import Board
from Wall import Wall

_window = Tk()
_window.title("Rasend Robot")
canvas = Canvas(_window,bg = "black")
canvas.place(x=0, y=0)
img_size =38

IMG_cell = PhotoImage ( file = "files/board/CaseX38.png" )

def place_cell(x, y):
        CAN_Zone_Image = canvas.create_image ( x*img_size , y*img_size , image = IMG_cell , anchor = "nw" )


class Window:

    def __init__(self, height,width):
        _window.geometry(str(height)+"x"+str(width))
        _window.resizable(width=False, height=False)
        canvas.config(width=width, height=height)


    def __init__(self):
        _window.geometry(str(16*img_size)+"x"+str(16*img_size))
        _window.resizable(width=False, height=False)
        canvas.config(width=16*img_size, height=16*img_size)



    def launch(self):
        _window.mainloop()

    def setsize(self, height, width):
        _window.geometry(str(height)+"x"+str(width))

    def place_wall(self, x, y, orient):
        fichierimg = PhotoImage(file="files/board/Case.png")



    def draw_board(self, board):
        for i in range(16):
            for j in range(16):
                place_cell(i,j)
                z = 0
                n_wall = len(board._cases[i][j]._walls)
                while z < n_wall:
                    board._cases[i][j]._walls[z].dir
                    z = z +1




