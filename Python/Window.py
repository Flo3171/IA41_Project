from tkinter import *
from Case import Case
from Board import Board
import Direction
from Wall import Wall

_window = Tk()
_window.title("Rasend Robot")
canvas = Canvas(_window,bg = "black")
canvas.place(x=0, y=0)
img_size =38

IMG_cell = PhotoImage ( file = "files/board/CaseX38.png" )
IMG_H_Wall = PhotoImage ( file = "files/board/VWallX38.png" )
IMG_V_Wall = PhotoImage ( file = "files/board/HWallX38.png" )

def place_cell(x, y):
    CAN_Zone_Image = canvas.create_image ( x*img_size , y*img_size , image = IMG_cell , anchor = "nw" )

def place_wall(x, y, orient):
    if orient == Direction.Direction.NORTH:
        CAN_Zone_Image = canvas.create_image (x*img_size , y*img_size -4, image = IMG_H_Wall , anchor = "nw" )
    if orient == Direction.Direction.SOUTH:
        CAN_Zone_Image = canvas.create_image (x*img_size , y*img_size +34, image = IMG_H_Wall , anchor = "nw" )
    if orient == Direction.Direction.WEST:
        CAN_Zone_Image = canvas.create_image (x*img_size -4, y*img_size , image = IMG_V_Wall , anchor = "nw" )
    if orient == Direction.Direction.EAST:
        CAN_Zone_Image = canvas.create_image (x*img_size +34, y*img_size , image = IMG_V_Wall , anchor = "nw" )

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

    def draw_board(self, board):
        for i in range(16):
            for j in range(16):
                place_cell(i,j)
        for i in range(16):
            for j in range(16):
                print(board._cases[i][j]._walls)
                z = 0
                n_wall = len(board._cases[i][j]._walls)
                while z < n_wall:
                    place_wall(i, j, board._cases[i][j]._walls[z].dir)
                    z = z +1




