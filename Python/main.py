import Board
import Game
from Window import Window
from tkinter import *
import GameObject

fen = Window()

b = Board.Board()
b.generate_board()
fen.draw_board(b)
fen.launch()



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




