from tkinter import *
import Direction
import GameObject
import Board

img_size =38
decal = 0
_window = Tk()
_window.title("Rasend Robot")
canvas = Canvas(_window,bg = "black")
canvas.place(x=0, y=0)
canvas2 = Canvas(_window,bg = "brown")
canvas2.place(x=16*img_size+300+decal, y=0 , anchor = "ne",width=300,height=16*img_size+decal)


IMG_cell = PhotoImage ( file = "files/board/CaseX38.png" )
IMG_H_Wall = PhotoImage ( file = "files/board/VWallX38.png" )
IMG_V_Wall = PhotoImage ( file = "files/board/HWallX38.png" )
IMG_VORTEX = PhotoImage ( file = "files/items/Vortex.png" )
IMG_BLUE_BALL =PhotoImage ( file = "files/items/BlueBall.png" )
IMG_RED_BALL =PhotoImage ( file = "files/items/RedBall.png" )
IMG_GREEN_BALL =PhotoImage ( file = "files/items/GreenBall.png" )
IMG_YELLOW_BALL =PhotoImage ( file = "files/items/YellowBall.png" )
IMG_BLUE_COIN =PhotoImage ( file = "files/items/BlueCoin.png" )
IMG_RED_COIN =PhotoImage ( file = "files/items/RedCoin.png" )
IMG_GREEN_COIN =PhotoImage ( file = "files/items/GreenCoin.png" )
IMG_YELLOW_COIN =PhotoImage ( file = "files/items/YellowCoin.png" )
IMG_BLUE_RING =PhotoImage ( file = "files/items/BlueRing.png" )
IMG_RED_RING =PhotoImage ( file = "files/items/RedRing.png" )
IMG_GREEN_RING =PhotoImage ( file = "files/items/GreenRing.png" )
IMG_YELLOW_RING =PhotoImage ( file = "files/items/YellowRing.png" )
IMG_BLUE_BEACON =PhotoImage ( file = "files/items/BlueBeacon.png" )
IMG_RED_BEACON =PhotoImage ( file = "files/items/RedBeacon.png" )
IMG_GREEN_BEACON =PhotoImage ( file = "files/items/GreenBeacon.png" )
IMG_YELLOW_BEACON =PhotoImage ( file = "files/items/YellowBeacon.png" )

def place_cell(x, y):
    CAN_Zone_Image = canvas.create_image ( x*img_size +decal, y*img_size+decal , image = IMG_cell , anchor = "nw" )

def place_wall(x, y, case):
    if case.has_walls_in_dir(Direction.Direction.NORTH):
        CAN_Zone_Image = canvas.create_image (x*img_size , y*img_size -4, image = IMG_H_Wall , anchor = "nw" )
    if case.has_walls_in_dir(Direction.Direction.SOUTH):
        CAN_Zone_Image = canvas.create_image (x*img_size , y*img_size +33, image = IMG_H_Wall , anchor = "nw" )
    if case.has_walls_in_dir(Direction.Direction.WEST):
        CAN_Zone_Image = canvas.create_image (x*img_size -4, y*img_size , image = IMG_V_Wall , anchor = "nw" )
    if case.has_walls_in_dir(Direction.Direction.EAST):
        CAN_Zone_Image = canvas.create_image (x*img_size +33, y*img_size , image = IMG_V_Wall , anchor = "nw" )

def place_objective(x, y,case):
    if case.game_object()==GameObject.GameObject.VORTEX:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_VORTEX, anchor = "center" )
    if case.game_object()==GameObject.GameObject.BLUE_BALL:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_BLUE_BALL, anchor = "center" )
    if case.game_object()==GameObject.GameObject.RED_BALL:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_RED_BALL, anchor = "center" )
    if case.game_object()==GameObject.GameObject.GREEN_BALL:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_GREEN_BALL, anchor = "center" )
    if case.game_object()==GameObject.GameObject.YELLOW_BALL:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_YELLOW_BALL, anchor = "center" )
    if case.game_object()==GameObject.GameObject.BLUE_COIN :
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_BLUE_COIN, anchor = "center" )
    if case.game_object()==GameObject.GameObject.RED_COIN:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_RED_COIN, anchor = "center" )
    if case.game_object()==GameObject.GameObject.GREEN_COIN:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_GREEN_COIN, anchor = "center" )
    if case.game_object()==GameObject.GameObject.YELLOW_COIN :
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_YELLOW_COIN, anchor = "center" )
    if case.game_object()==GameObject.GameObject.BLUE_RING:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_BLUE_RING, anchor = "center" )
    if case.game_object()==GameObject.GameObject.RED_RING:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_RED_RING, anchor = "center" )
    if case.game_object()==GameObject.GameObject.GREEN_RING:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_GREEN_RING, anchor = "center" )
    if case.game_object()==GameObject.GameObject.YELLOW_RING:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_YELLOW_RING, anchor = "center" )
    if case.game_object()==GameObject.GameObject.BLUE_BEACON:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_BLUE_BEACON, anchor = "center" )
    if case.game_object()==GameObject.GameObject.RED_BEACON:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_RED_BEACON, anchor = "center" )
    if case.game_object()==GameObject.GameObject.GREEN_BEACON:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_GREEN_BEACON, anchor = "center" )
    if case.game_object()==GameObject.GameObject.YELLOW_BEACON:
        CAN_Zone_Image = canvas.create_image ( x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_YELLOW_BEACON, anchor = "center" )


class Window:

    def __init__(self, height,width):
        _window.geometry(str(height)+"x"+str(width))
        _window.resizable(width=False, height=False)
        canvas.config(width=width, height=height)


    def __init__(self):
        _window.geometry(str(16*img_size+300+decal)+"x"+str(16*img_size+decal))
        _window.resizable(width=False, height=False)
        canvas.config(width=16*img_size+(decal*2), height=16*img_size+(decal*2))



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
                place_wall(i, j, board.case(i, j))
        for i in range(16):
            for j in range(16):
                if board.case( i, j).has_game_object():
                    place_objective(i,j,board.case( i, j))




