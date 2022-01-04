import Board
import PathSolver as ps
from Window import Window
from tkinter import *
import GameObject
import Board
import CostMap
import Objective
import Coord
import Direction
import Window
import Wall
import Robot
import AI

c = [Coord.Coord(7, 0),
     Coord.Coord(0, 15),
     Coord.Coord(15, 0),
     Coord.Coord(3, 4)]

colors = ["Blue", "Green", "Red", "Yellow"]

b = Board.Board()
b.generate_default_wall()
b.generate_template(True)

for i in range(4):
    r = Robot.Robot(colors[i], c[i])
    b.robots.append(r)
    b.case_coord(c[i]).place_bot(r)

b.choose_objective(GameObject.GameObject.YELLOW_COIN)
b.update_destination()



ai = AI.AI(b)
solution = ai.solve()

for m in solution:
    print(m.robot_color + " " + m.direction.__str__())

"""m = CostMap.CostMap(b)

m.update_cost_map()
print(b.objective.coord)
print(b.objective.game_object)
print(b.target_robot.pos)
print(m)

print(m.get_next_move().direction)"""

fen = Window.Window(b)
fen.draw_board()
fen.launch()





"""
TKI_Principal = Tk ( )

IMG_Image = PhotoImage ( file = "files/board/Case.png" )

CAN_Zone = Canvas ( TKI_Principal , bg = "black" , height = 130 , width = 220 )
CAN_Zone.grid ( row = 0 , column = 0 , sticky = "nesw" )
CAN_Zone_Image = CAN_Zone.create_image ( 30 , 10 , image = IMG_Image , anchor = "nw" )

TKI_Principal.mainloop ( )"""