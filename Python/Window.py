from tkinter import *
import Board
import Direction
import GameObject
from Python import AI

img_size = 38
decal = 0
_window = Tk()
_window.title("Rasend Robot")
canvas = Canvas(_window, bg="black")
canvas.place(x=0, y=0)
canvas2 = Canvas(_window, bg="brown")
canvas2.place(x=16 * img_size + 300 + decal, y=0, anchor="ne", width=300, height=16 * img_size + decal)

BNorth = Button(canvas2, text="NORTH", bg="purple")
BSouth = Button(canvas2, text="SOUTH", bg="purple")
BEast = Button(canvas2, text="EAST", bg="purple")
BWest = Button(canvas2, text="WEST", bg="purple")
BRed = Button(canvas2, text="", bg="red", width=5)
BBlue = Button(canvas2, text="", bg="blue", width=5)
BGreen = Button(canvas2, text="", bg="green", width=5)
BYellow = Button(canvas2, text="", bg="yellow", width=5)
BSolve = Button(canvas2, text="VIEW NEXT STEP", bg="Brown")
BResolve = Button(canvas2, text="PLAY NEXT STEP", bg="Brown")
BResolveAll = Button(canvas2, text="RESOLVE SOLUTION", bg="Brown")
BReset = Button(canvas2, text="RESET", bg="Brown")
LColor = Label(canvas2, text="Color select", bg="Brown")
LCoups = Label(canvas2, text="Nombre de coups joués :", bg="Brown")
LNbCoups = Label(canvas2, text="solution en coups :", bg="Brown")

IMG_R_robot = PhotoImage(file="files/robots/RedRobot.png")
IMG_B_robot = PhotoImage(file="files/robots/BlueRobot.png")
IMG_G_robot = PhotoImage(file="files/robots/GreenRobot.png")
IMG_Y_robot = PhotoImage(file="files/robots/YellowRobot.png")

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

    def __init__(self, board):

        if board is None:
            b = Board.Board()
            b.generate_board()
            b.choose_objective()
            self._board = b
        else:
            self._board = board

        self._color = None
        self.R_robot = None
        self.B_robot = None
        self.G_robot = None
        self.Y_robot = None
        self._coups = 0
        self._coupsSolve = 0
        self._solFind = False
        self.IMG_Objective = canvas2.create_image(170, 250)
        self.lines = []
        Window.define_objective(self)
        Window.supp_coups_sol(self)
        Window.launch_fen()

    @staticmethod
    def launch_fen():

        _window.geometry(str(16 * img_size + 300 + decal) + "x" + str(16 * img_size + decal))
        _window.resizable(width=False, height=False)
        canvas.config(width=16 * img_size + (decal * 2), height=16 * img_size + (decal * 2))

        BNorth.place(x=150, y=80, anchor="center")
        BSouth.place(x=150, y=160, anchor="center")
        BEast.place(x=200, y=120, anchor="center")
        BWest.place(x=100, y=120, anchor="center")
        BRed.place(x=40, y=200, anchor="center")
        BBlue.place(x=110, y=200, anchor="center")
        BGreen.place(x=180, y=200, anchor="center")
        BYellow.place(x=250, y=200, anchor="center")
        BSolve.place(x=30, y=300, anchor="w")
        BResolve.place(x=30, y=340, anchor="w")
        BResolveAll.place(x=30, y=380, anchor="w")
        BReset.place(x=30, y=580, anchor="center")
        LColor.place(x=60, y=30, anchor="center")
        LCoups.place(x=130, y=30, anchor="w")
        LNbCoups.place(x=150, y=335, anchor="w")
        Label(canvas2, text="objective : ", bg="brown").place(x=100, y=250, anchor="center")

    def define_objective(self):

        if self._board.objective.game_object == GameObject.GameObject.VORTEX:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_VORTEX, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.BLUE_BALL:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_BLUE_BALL, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.RED_BALL:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_RED_BALL, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.GREEN_BALL:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_GREEN_BALL, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.YELLOW_BALL:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_YELLOW_BALL, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.BLUE_COIN:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_BLUE_COIN, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.RED_COIN:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_RED_COIN, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.GREEN_COIN:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_GREEN_COIN, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.YELLOW_COIN:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_YELLOW_COIN, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.BLUE_RING:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_BLUE_RING, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.RED_RING:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_RED_RING, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.GREEN_RING:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_GREEN_RING, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.YELLOW_RING:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_YELLOW_RING, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.BLUE_BEACON:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_BLUE_BEACON, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.RED_BEACON:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_RED_BEACON, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.GREEN_BEACON:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_GREEN_BEACON, anchor="center")
        if self._board.objective.game_object == GameObject.GameObject.YELLOW_BEACON:
            canvas2.itemconfig(self.IMG_Objective, image=IMG_YELLOW_BEACON, anchor="center")

    @staticmethod
    def launch():
        _window.mainloop()

    @staticmethod
    def setsize(height, width):
        _window.geometry(str(height) + "x" + str(width))

    def draw_board(self):
        for j in range(16):
            for i in range(16):
                Window.place_cell(i, j)
        for j in range(16):
            for i in range(16):
                Window.place_wall(i, j, self._board.case(i, j))
        for j in range(16):
            for i in range(16):
                if self._board.case(i, j).has_game_object():
                    Window.place_objective(i, j, self._board.case(i, j))
        for j in range(16):
            for i in range(16):
                if self._board.case(i, j).has_bot():
                    Window.place_robot(self, i, j, self._board.case(i, j))
        Window.button_config(self)

    def place_robot(self, x, y, case):
        if case.bot.color == "Red":
            self.R_robot = canvas.create_image(x * img_size + img_size / 2 + decal, y * img_size + img_size / 2 + decal,
                                               image=IMG_R_robot, anchor="center")
        if case.bot.color == "Blue":
            self.B_robot = canvas.create_image(x * img_size + img_size / 2 + decal, y * img_size + img_size / 2 + decal,
                                               image=IMG_B_robot, anchor="center")
        if case.bot.color == "Green":
            self.G_robot = canvas.create_image(x * img_size + img_size / 2 + decal, y * img_size + img_size / 2 + decal,
                                               image=IMG_G_robot, anchor="center")
        if case.bot.color == "Yellow":
            self.Y_robot = canvas.create_image(x * img_size + img_size / 2 + decal, y * img_size + img_size / 2 + decal,
                                               image=IMG_Y_robot, anchor="center")

    @staticmethod
    def place_cell(x, y):
        canvas.create_image(x * img_size + decal, y * img_size + decal, image=IMG_cell, anchor="nw")

    @staticmethod
    def place_wall(x, y, case):
        if case.has_walls_in_dir(Direction.Direction.NORTH):
            canvas.create_image(x * img_size, y * img_size - 4, image=IMG_H_Wall, anchor="nw")
        if case.has_walls_in_dir(Direction.Direction.SOUTH):
            canvas.create_image(x * img_size, y * img_size + 33, image=IMG_H_Wall, anchor="nw")
        if case.has_walls_in_dir(Direction.Direction.WEST):
            canvas.create_image(x * img_size - 4, y * img_size, image=IMG_V_Wall, anchor="nw")
        if case.has_walls_in_dir(Direction.Direction.EAST):
            canvas.create_image(x * img_size + 33, y * img_size, image=IMG_V_Wall, anchor="nw")

    @staticmethod
    def place_objective(x, y, case):
        if case.game_object() == GameObject.GameObject.VORTEX:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_VORTEX, anchor="center")
        if case.game_object() == GameObject.GameObject.BLUE_BALL:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_BLUE_BALL,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.RED_BALL:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_RED_BALL,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.GREEN_BALL:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_GREEN_BALL,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.YELLOW_BALL:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_YELLOW_BALL,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.BLUE_COIN:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_BLUE_COIN,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.RED_COIN:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_RED_COIN,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.GREEN_COIN:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_GREEN_COIN,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.YELLOW_COIN:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_YELLOW_COIN,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.BLUE_RING:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_BLUE_RING,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.RED_RING:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_RED_RING,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.GREEN_RING:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_GREEN_RING,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.YELLOW_RING:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_YELLOW_RING,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.BLUE_BEACON:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_BLUE_BEACON,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.RED_BEACON:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_RED_BEACON,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.GREEN_BEACON:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_GREEN_BEACON,
                                anchor="center")
        if case.game_object() == GameObject.GameObject.YELLOW_BEACON:
            canvas.create_image(x * img_size + img_size / 2 + decal,
                                y * img_size + img_size / 2 + decal, image=IMG_YELLOW_BEACON,
                                anchor="center")

    def move_n(self):
        if self._color is not None and self._solFind is False:
            Window.add_coup(self)
            cord = self._board.case(self._board.robot(self._color).pos.x,
                                    self._board.robot(self._color).pos.y).destination(
                Direction.Direction.NORTH).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            Window.sol_find(self)

    def move_s(self):
        if self._color is not None and self._solFind is False:
            Window.add_coup(self)
            cord = self._board.case(self._board.robot(self._color).pos.x,
                                    self._board.robot(self._color).pos.y).destination(
                Direction.Direction.SOUTH).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            Window.sol_find(self)

    def move_e(self):
        if self._color is not None and self._solFind is False:
            Window.add_coup(self)
            cord = self._board.case(self._board.robot(self._color).pos.x,
                                    self._board.robot(self._color).pos.y).destination(
                Direction.Direction.EAST).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            Window.sol_find(self)

    def move_w(self):
        if self._color is not None and self._solFind is False:
            Window.add_coup(self)
            cord = self._board.case(self._board.robot(self._color).pos.x,
                                    self._board.robot(self._color).pos.y).destination(
                Direction.Direction.WEST).case.coord
            self._board.move_bot(self._color, cord)
            if self._color == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if self._color == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            Window.sol_find(self)

    def pick_r(self):
        self._color = "Red"
        LColor.config(bg="Red")

    def pick_b(self):
        self._color = "Blue"
        LColor.config(bg="Blue")

    def pick_g(self):
        self._color = "Green"
        LColor.config(bg="Green")

    def pick_y(self):
        self._color = "Yellow"
        LColor.config(bg="Yellow")

    def solve(self):
        ai = AI.AI(self._board)
        ai.solve()
        col = ai.solution[0].robot_color  # récupère la couleur du robot à jouer
        dest = ai.solution[0].direction  # récupère la destination à appliquer
        x = self._board.robot(col).pos.x
        y = self._board.robot(col).pos.y
        cord = self._board.case(self._board.robot(col).pos.x,
                                self._board.robot(col).pos.y).destination(dest).case.coord
        Window.drawn_line(self, x, y, cord.x, cord.y, col)

    def resolve(self):
        ai = AI.AI(self._board)
        ai.solve()

        if ai.solution[0] is not None and self._solFind is False:
            Window.add_coup(self)
            col = ai.solution[0].robot_color  # récupère la couleur du robot à jouer
            dest = ai.solution[0].direction  # récupère la destination à appliquer
            x = self._board.robot(col).pos.x
            y = self._board.robot(col).pos.y
            cord = self._board.case(self._board.robot(col).pos.x,
                                    self._board.robot(col).pos.y).destination(dest).case.coord
            self._board.move_bot(col, cord)
            Window.drawn_line(self, x, y, cord.x, cord.y, col)
            if col == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if col == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if col == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if col == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            Window.sol_find(self)

    def resolve_all(self):
        ai = AI.AI(self._board)
        ai.solve()

        if ai.solution[0] is not None and self._solFind is False:
            Window.add_coup(self)
            col = ai.solution[0].robot_color  # récupère la couleur du robot à jouer
            dest = ai.solution[0].direction  # récupère la destination à appliquer
            x = self._board.robot(col).pos.x
            y = self._board.robot(col).pos.y
            cord = self._board.case(self._board.robot(col).pos.x,
                                    self._board.robot(col).pos.y).destination(dest).case.coord
            self._board.move_bot(col, cord)
            Window.drawn_line(self, x, y, cord.x, cord.y, col)
            if col == "Red":
                canvas.coords(self.R_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if col == "Blue":
                canvas.coords(self.B_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if col == "Green":
                canvas.coords(self.G_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            if col == "Yellow":
                canvas.coords(self.Y_robot, cord.x * img_size + img_size / 2 + decal,
                              cord.y * img_size + img_size / 2 + decal)
            Window.sol_find(self)
            Window.resolve_all(self)
            Window.add_coups_sol(self)


    def reset(self):
        Window.supp_lines(self)
        Window.supp_coups_sol(self)
        Window.supp_coup(self)
        self._solFind = False
        self._board.reset_bot()
        x = self._board.robot("Red").pos.x
        y = self._board.robot("Red").pos.y
        canvas.coords(self.R_robot, x * img_size + img_size / 2 + decal,
                      y * img_size + img_size / 2 + decal)
        x = self._board.robot("Blue").pos.x
        y = self._board.robot("Blue").pos.y
        canvas.coords(self.B_robot, x * img_size + img_size / 2 + decal,
                      y * img_size + img_size / 2 + decal)
        x = self._board.robot("Green").pos.x
        y = self._board.robot("Green").pos.y
        canvas.coords(self.G_robot, x * img_size + img_size / 2 + decal,
                      y * img_size + img_size / 2 + decal)
        x = self._board.robot("Yellow").pos.x
        y = self._board.robot("Yellow").pos.y
        canvas.coords(self.Y_robot, x * img_size + img_size / 2 + decal,
                      y * img_size + img_size / 2 + decal)

    def drawn_line(self, x1, y1, x2, y2, color):
        self.lines.append(canvas.create_line(x1 * img_size + img_size / 2, y1 * img_size + img_size / 2,
                                             x2 * img_size + img_size / 2 + decal,
                                             y2 * img_size + img_size / 2 + decal, width=2, fill=color))

    def supp_last_line(self):
        long = len(self.lines)
        canvas.delete(self.lines[long - 1])

    def supp_lines(self):
        long = len(self.lines)
        for i in range(long):
            canvas.delete(self.lines[i])

    def add_coup(self):
        self._coups = self._coups + 1
        LCoups.config(text="Nombre de coups joués : " + str(self._coups))

    def supp_coup(self):
        self._coups = 0
        LCoups.config(text="Nombre de coups joués : " + str(self._coups))

    def add_coups_sol(self):
        self._coupsSolve = self._coupsSolve + 1
        LNbCoups.config(text="solution trouvée en :\n" + str(self._coups) + " coups")

    def supp_coups_sol(self):
        self._coupsSolve = 0
        LNbCoups.config(text="")

    def sol_find(self):
        ai = AI.AI(self._board)
        self._solFind = ai.is_solution_find()

    def button_config(self):
        BNorth.config(command=self.move_n)
        BSouth.config(command=self.move_s)
        BWest.config(command=self.move_w)
        BEast.config(command=self.move_e)

        BRed.config(command=self.pick_r)
        BBlue.config(command=self.pick_b)
        BGreen.config(command=self.pick_g)
        BYellow.config(command=self.pick_y)

        BSolve.config(command=self.solve)
        BResolve.config(command=self.resolve)
        BResolveAll.config(command=self.resolve_all)
        BReset.config(command=self.reset)
