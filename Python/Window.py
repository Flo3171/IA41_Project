from tkinter import *
import Direction
import GameObject
import Board

img_size = 38
decal = 0
_window = Tk()
_window.title("Rasend Robot")
canvas = Canvas(_window, bg="black")
canvas.place(x=0, y=0)
canvas2 = Canvas(_window, bg="brown")
canvas2.place(x=16*img_size+300+decal, y=0, anchor="ne", width=300, height=16*img_size+decal)

BNorth = Button(canvas2, text="NORTH", bg ="purple" )
BSouth = Button(canvas2, text="SOUTH", bg="purple")
BEast = Button(canvas2, text="EAST", bg="purple")
BWest = Button(canvas2, text="WEST", bg="purple")
BRed = Button(canvas2, text="", bg="red", width=5)
BBlue = Button(canvas2, text="", bg="blue", width=5)
BGreen = Button(canvas2, text="", bg="green", width=5)
BYellow = Button(canvas2, text="", bg="yellow", width=5)

IMG_R_robot = PhotoImage(file="files/robots/RedRobot.png" )
IMG_B_robot = PhotoImage(file="files/robots/BlueRobot.png" )
IMG_G_robot = PhotoImage(file="files/robots/GreenRobot.png" )
IMG_Y_robot = PhotoImage(file="files/robots/YellowRobot.png" )

"""R_robot = canvas.create_image (0*img_size +img_size/2 +decal , 0*img_size +img_size/2+decal, image = IMG_R_robot , anchor = "center" )
B_robot = canvas.create_image (0*img_size +img_size/2 +decal , 0*img_size +img_size/2+decal, image = IMG_B_robot , anchor = "center" )
G_robot = canvas.create_image (0*img_size +img_size/2 +decal , 0*img_size +img_size/2+decal, image = IMG_G_robot , anchor = "center" )
Y_robot = canvas.create_image (0*img_size +img_size/2 +decal , 0*img_size +img_size/2+decal, image = IMG_Y_robot , anchor = "center" )"""

IMG_cell = PhotoImage(file="files/board/CaseX38.png")
IMG_H_Wall = PhotoImage(file="files/board/VWallX38.png")
IMG_V_Wall = PhotoImage(file="files/board/HWallX38.png")
IMG_VORTEX = PhotoImage(file="files/items/Vortex.png")
IMG_BLUE_BALL = PhotoImage(file="files/items/BlueBall.png")
IMG_RED_BALL = PhotoImage(file="files/items/RedBall.png")
IMG_GREEN_BALL = PhotoImage(file="files/items/GreenBall.png")
IMG_YELLOW_BALL = PhotoImage(file="files/items/YellowBall.png")
IMG_BLUE_COIN = PhotoImage(file="files/items/BlueCoin.png")
IMG_RED_COIN = PhotoImage(file="files/items/RedCoin.png")
IMG_GREEN_COIN = PhotoImage(file="files/items/GreenCoin.png")
IMG_YELLOW_COIN = PhotoImage(file="files/items/YellowCoin.png")
IMG_BLUE_RING = PhotoImage(file="files/items/BlueRing.png")
IMG_RED_RING = PhotoImage(file="files/items/RedRing.png")
IMG_GREEN_RING = PhotoImage(file="files/items/GreenRing.png")
IMG_YELLOW_RING = PhotoImage(file="files/items/YellowRing.png")
IMG_BLUE_BEACON = PhotoImage(file="files/items/BlueBeacon.png")
IMG_RED_BEACON = PhotoImage(file="files/items/RedBeacon.png")
IMG_GREEN_BEACON = PhotoImage(file="files/items/GreenBeacon.png")
IMG_YELLOW_BEACON = PhotoImage(file="files/items/YellowBeacon.png")


class Window:

    def __init__(self):
        self._board = Board.Board()
        self._board.generate_board()
        _window.geometry(str(16*img_size+300+decal)+"x"+str(16*img_size+decal))
        _window.resizable(width=False, height=False)
        canvas.config(width=16*img_size+(decal*2), height=16*img_size+(decal*2))

        self._color = None
        self.R_robot = None
        self.B_robot = None
        self.G_robot = None
        self.Y_robot = None


        BNorth.place(x=150 , y=80, anchor= "center")
        BSouth.place(x=150 , y=160, anchor= "center")
        BEast.place(x=200 , y=120, anchor= "center")
        BWest.place(x=100 , y=120, anchor= "center")
        BRed.place(x=40 , y=200, anchor= "center")
        BBlue.place(x=110 , y=200, anchor= "center")
        BGreen.place(x=180 , y=200, anchor= "center")
        BYellow.place(x=250 , y=200, anchor= "center")



    def launch(self):
        _window.mainloop()

    def setsize(self, height, width):
        _window.geometry(str(height)+"x"+str(width))

    def draw_board(self):
        for i in range(16):
            for j in range(16):
                Window.place_cell(i, j)
        for i in range(16):
            for j in range(16):
                Window.place_wall(i, j, self._board.case(i, j))
        for i in range(16):
            for j in range(16):
                if self._board.case( i, j).has_game_object():
                    Window.place_objective(i,j,self._board.case( i, j))
        for i in range(16):
            for j in range(16):
                if self._board.case(i,j).has_bot():
                    Window.place_robot(self, i, j, self._board.case(i, j))
        Window.button_config(self)

    def place_robot(self, x, y, case):
        if case.bot().color() == "Red":
            self.R_robot = canvas.create_image (x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_R_robot , anchor = "center" )
        if case.bot().color() == "Blue":
            self.B_robot = canvas.create_image (x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_B_robot , anchor = "center" )
        if case.bot().color() == "Green":
            self.G_robot = canvas.create_image (x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_G_robot , anchor = "center" )
        if case.bot().color() == "Yellow":
            self.Y_robot = canvas.create_image (x*img_size +img_size/2 +decal , y*img_size +img_size/2+decal, image = IMG_Y_robot , anchor = "center" )

    @staticmethod
    def place_cell(x, y):
        CAN_Zone_Image = canvas.create_image ( x*img_size +decal, y*img_size+decal , image = IMG_cell , anchor = "nw" )

    @staticmethod
    def place_wall(x, y, case):
        if case.has_walls_in_dir(Direction.Direction.NORTH):
            CAN_Zone_Image = canvas.create_image (x*img_size , y*img_size -4, image = IMG_H_Wall , anchor = "nw" )
        if case.has_walls_in_dir(Direction.Direction.SOUTH):
            CAN_Zone_Image = canvas.create_image (x*img_size , y*img_size +33, image = IMG_H_Wall , anchor = "nw" )
        if case.has_walls_in_dir(Direction.Direction.WEST):
            CAN_Zone_Image = canvas.create_image (x*img_size -4, y*img_size , image = IMG_V_Wall , anchor = "nw" )
        if case.has_walls_in_dir(Direction.Direction.EAST):
            CAN_Zone_Image = canvas.create_image (x*img_size +33, y*img_size , image = IMG_V_Wall , anchor = "nw" )

    @staticmethod
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


    def move_N(self):
        if self._color is not None:
            cord =self._board.case(self._board.robot(self._color).pos().x, self._board.robot(self._color).pos().y).destination(Direction.Direction.NORTH).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
        self._color = None

    def move_S(self):
        if self._color is not None:
            cord =self._board.case(self._board.robot(self._color).pos().x, self._board.robot(self._color).pos().y).destination(Direction.Direction.SOUTH).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
        self._color = None

    def move_E(self):
        if self._color is not None:
            cord =self._board.case(self._board.robot(self._color).pos().x, self._board.robot(self._color).pos().y).destination(Direction.Direction.EAST).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
        self._color = None

    def move_W(self):
        if self._color is not None:
            cord =self._board.case(self._board.robot(self._color).pos().x, self._board.robot(self._color).pos().y).destination(Direction.Direction.WEST).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size/2 + decal, cord.y * img_size + img_size/2 + decal)
        self._color = None

    def pick_R(self):
        self._color = "Red"
    def pick_B(self):
        self._color = "Blue"
    def pick_G(self):
        self._color = "Green"
    def pick_Y(self):
        self._color = "Yellow"

    def solve(self):
        ia = ps.PathSolver(None, None, b)
        ia.choose_next_state()
        state = ia
        while state != None:
            fen.draw_board(state.board())
            state = state._nextState


    def button_config(self):
        BNorth.config(command=self.move_N)
        BSouth.config(command=self.move_S)
        BWest.config(command=self.move_W)
        BEast.config(command=self.move_E)

        BRed.config(command=self.pick_R)
        BBlue.config(command=self.pick_B)
        BGreen.config(command=self.pick_G)
        BYellow.config(command=self.pick_Y)

