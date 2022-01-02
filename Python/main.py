import Board
import Game
import PathSolver as ps
from Window import Window
from tkinter import *
import GameObject
import Coord
import Direction


b = Board.Board()
fen = Window(b)
fen.draw_board()
fen.launch()

"""ia=ps.PathSolver(None,None,b)
ia.choose_next_state()
state=ia
while state != None:
    fen.draw_board(state.board())
    state = state._nextState"""
    




"""TKI_Principal = Tk ( )

IMG_Image = PhotoImage ( file = "files/board/Case.png" )

CAN_Zone = Canvas ( TKI_Principal , bg = "black" , height = 130 , width = 220 )
CAN_Zone.grid ( row = 0 , column = 0 , sticky = "nesw" )
CAN_Zone_Image = CAN_Zone.create_image ( 30 , 10 , image = IMG_Image , anchor = "nw" )

TKI_Principal.mainloop ( )"""



"""f = Tk()
IMG_Image = PhotoImage ( file = "files/board/Case.png" )
canvas = Canvas(f, height=500, width=500)
canvas.grid ( row = 0 , column = 0 , sticky = "nesw" )
CAN_Zone_Image = canvas.create_image ( 30 , 10 , image = IMG_Image , anchor = "nw" )
f.mainloop()"""




