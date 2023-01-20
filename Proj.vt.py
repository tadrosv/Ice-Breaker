"""
This program is my own work. I have not copied from anyone or anywhere 
nor have I allowed anyone to copy my work.

Author:	Victor Tadros

This program will build a board game called 'Icebreaker', it will create a board 
with squares, display text, and buttons. The goal of game is to trap a player in
blue squares('water') by clicking on a square. If player has no valid moves(ice) 
left game is over.
"""

from graphics import *
import math
import random


COLOUMN, ROW = 7, 10
WIN_W, WIN_H = 455, 450
WIN_S, GAP = 40, 5
COLOURS = ['light blue', 'white']
RECTANGLE, COLOUR = range(2)
player_gifs = ['red_dot', 'blue_dot']
ices = [] #broken/unbroken pieces
#initial_moves is a list of all valid moves a player can make at the start of the game
initial_moves = [[[0, 2],[0, 3],[1, 2],[1, 3],[1, 4],[0, 4],],
          [[9, 2],[8, 2],[8, 3],[8, 4],[9, 4],[9, 3],], 
          [[0, 3], [9, 3]]]

def square(x, y):
 """
 function creates board for game using variables listed above
 parameters: x, y; coordinates of each square
 return: N/A
 """
 global ices
 
 left = GAP + x * (WIN_S + GAP)
 top = GAP + y * (WIN_S + GAP)
 rect = Rectangle(Point(left, top), Point(left + WIN_S, top + WIN_S))
 ices[x][y].append(rect)
 ices[x][y].append(COLOURS[1])
 ices[x][y][0].setFill(COLOURS[1])
 ices[x][y][0].draw(win)
 #ices[x][y] = [rect]
 #return ices[x][y]

#-------------------------------------------------------------------------------

def squares():
 """
 function makes rows and columns of squares to complete icebreaker board
 parameters: N/A
 return: N/A
 """
 global ices
 
 for i in range(ROW):
  ices.append([])
  for x in range(COLOUMN):
   ices[i].append([])
   board = square(i, x)
 return board


#-------------------------------------------------------------------------------

def display_msg():
 in_text = "ICE BREAKER GAME"
 message = Text(Point(150, 350), in_text)
 message.draw(win)
 return in_text, message

#-------------------------------------------------------------------------------

def options(win):
 """
 function will create two buttons that will perform a task. both buttons will
 have labels
 parameters: win, windows
 return: quit, reset; buttons
 """
 quit = Rectangle(Point(322, 400), Point(378, 420))
 quit.setFill('white') 
 text_q = Text(Point(350, 410), 'QUIT')
 quit.draw(win)
 text_q.draw(win)
 
 reset = Rectangle(Point(322, 425), Point(378, 445))
 reset.setFill('white')
 text_re = Text(Point(350, 435), 'RESET') 
 reset.draw(win)
 text_re.draw(win)
 
 return quit, reset

#-------------------------------------------------------------------------------

def in_box(point, rectangle):
 """
 function gets points of P1 and P2 and stores them in variables, returns specified action for where point is clicked on object or not.
 parameter: point, coordinate
            rectangle, object
 return: Ll.getX() < point.getX() < Ur.getX() and Ll.getY() < point.getY() < Ur.getY()
              specified area where click happens
 """
 Ll = rectangle.getP1() # lower left
 Ur = rectangle.getP2() # upper right
 
 return Ll.getX() < point.getX() < Ur.getX() and Ll.getY() < point.getY() < Ur.getY()

#-------------------------------------------------------------------------------

def get_players():
 global red_p, blue_p
 red_point = Point(25, 160)
 red_p = Image(red_point, "red_dot.gif")
 red_p.draw(win)

 blue_point = Point(WIN_W - 24, 160)
 blue_p = Image(blue_point, "blue_dot.gif")
 blue_p.draw(win)

 list_players = [red_p, blue_p]

 return red_p, blue_p, list_players

#-------------------------------------------------------------------------------

def convert_to_grid(point):
 global x, y, message, in_text
 coord_grid = []

 if point.y >= 317:
  in_text = f"COORDINATE: {x}, {y}"
  message.setText(in_text)

 else: 
  coloumn = int((x - 5) / 45) 
  row = int((y - 5) / 45) 
  point1 = ices[coloumn][row][0].getP1()
  point2 = ices[coloumn][row][0].getP2()
  coord_grid.append([x, y, point1, point2, [coloumn, row]]) 
  in_text = f"COORDINATE: {coloumn + 1}, {row + 1}"
  message.setText(in_text)

 return coord_grid 

#-------------------------------------------------------------------------------

def first_move():
 global player, red_p, blue_p, in_text, message
 
 player = random.randint(0, 1)
 #win.getMouse()
 
 if player == 0:
  for i in range(7):
   red_p
  in_text = 'Red makes first move!'
  message.setText(in_text)
  
 elif player == 1:
  for i in range(7):
   blue_p
  in_text = 'Blue makes first move!'
  message.setText(in_text)    
 
 #return player
        
#-------------------------------------------------------------------------------

def move_valid(point, ices):
 global in_text, message, player
 
 coord_grid = convert_to_grid(point)
 player = coord_grid

 if ices[player[0][4][0]][player[0][4][1]][1] != COLOURS[0] and player[0][4] in initial_moves[player_turn] and player[0][4] not in initial_moves[2]:
  
  move_piece(player, player_turn)
  return True
 
 else:
  in_text = 'INVALID MOVE'
  message.setText(in_text)
  
#-------------------------------------------------------------------------------

def move_piece(player, player_turn):
 global ices, list_players, in_text, message
 
 in_text = 'MAKE A MOVE!'
 message.setText(in_text)
 
 list_players[player].undraw()
 
 list_players[player] = Image(Point((player[0][2].x + player[0][3].x) / 2, (player[0][2].y + player[0][3].y) / 2))
 list_player[player].Image(player_gifs[player])
 list_player[player].draw(win)
 
 update_moves(player, player_turn)

#-------------------------------------------------------------------------------

def caluclate_range_movement(player):
 
 i_beg, i_end = int(player[0][4][0]) - 1, int(player[0][4][0]) + 2
 j_beg, j_end = int(player[0][4][1]) - 1, int(player[0][4][1]) + 2

 if int(player[0][4][1]) == 0 and int(player[0][4][0]) == 0:
     i_beg, j_beg = int(player[0][4][0]), int(player[0][4][1])
     
 elif int(player[0][4][0]) == 0 and int(player[0][4][1]) == 6:
     i_beg, j_end = int(player[0][4][0]), int(player[0][4][1]) + 1
                       
 elif int(player[0][4][0]) == 9 and int(player[0][4][1]) == 6:
     i_end, j_end = int(player[0][4][0]) + 1, int(player[0][4][1]) + 1
     
 elif int(player[0][4][0]) == 9 and int(player[0][4][1]) == 0:
     i_end, j_beg = int(player[0][4][0]) + 1, int(player[0][4][1])
 
 elif int(player[0][4][1]) == 0: j_beg = int(player[0][4][1])
     
 elif int(player[0][4][0]) == 0: i_beg = int(player[0][4][0])
     
 elif int(player[0][4][1]) == 6: j_end = int(player[0][4][1]) + 1
     
 elif int(player[0][4][0]) == 9: i_end = int(player[0][4][0]) + 1

 move_range = (i_beg, i_end, j_beg, j_end)
 return move_range

#-------------------------------------------------------------------------------

def update_moves(player, player_turn):
 global initial_moves, ices
 
 initial_moves[player] = []
 initial_moves[2][player] = player[0][4]
 movements = calculate_range_movement(player)
 
 for i in range(movements[0], movements[1]):
     for j in range(movements[2], movements[3]):
          #check if the square beside the player is blue and another if player is on it
         if square_list[i][x][1] != ICE_COLORS[1]:
             initial_moves[player_turn].append([i, x])
 
 #initial_moves cleanup: remove occupied squares from the list for both players
 if initial_moves[2][player_turn] in initial_moves[player_turn]:
     initial_moves[player_turn].remove(initial_moves[2][player_turn])
 
 if initial_moves[2][not player_turn] in initial_moves[not player_turn]:
     initial_moves[not player_turn].remove(initial_moves[2][not player_turn]) 
 
 if initial_moves[2][player_turn] in initial_moves[not player_turn]:
     initial_moves[not player_turn].remove(initial_moves[2][player_turn]) 
 
 if len(initial_moves[player_turn]) == 1 and initial_moves[2][not player_turn]\
            in initial_moves[player_turn]:
     
     initial_moves[player_turn].remove(initial_moves[2][not player_turn]) 
 
 return initial_moves 

#-------------------------------------------------------------------------------

def break_ice_valid():
 global ices, initial_moves, player_turn, point
 
 shatter = convert_to_grid(x, y, point)
 
 if ices[shatter[0][4][0]][shatter[0][4][1]][1] == COLOURS[1] and initial_moves[2][0] != shatter[0][4] and initial_moves[2][1] != shatter[0][4]:
  break_ice(shatter)
  if break_ice[0][4] in initial_moves[not player_turn]:
   initial_moves[not player_turn].remove(shatter[0][4])
  player_turn = change_players(player_turn)
  return True
 #ices[shatter[0][4][0]][shatter[0][4][1]][0].setFill(COLOURS[0])
 
 #ices[shatter[0][4][0]][shatter[0][4][1][1]] = COLOURS[0]
 #ices[x][y][COLOUR] = not ices[x][y][COLOUR]
 #ices[x][y][RECTANGLE].setFill(COLOURS[ices[x][y][COLOUR]]) 
 

#-------------------------------------------------------------------------------

def break_ice(shatter):
 global initial_moves, ices, player, player_turn, in_text, message
 
 in_text = 'BREAK ICE'
 message.setText(in_text)
 
 ices[shatter[0][4][0]][shatter[0][4][1]][0].setFill(COLOURS[0])
 
 ices[shatter[0][4][0]][shatter[0][4][1]][1] = COLOURS[0]
 
 update_moves(player, player_turn)
 
#-------------------------------------------------------------------------------

def change_players(player_turn):
 global in_text, message
 
 if player == 0:
  player = 1
  in_text = 'Its your turn Blue!'
  message.setText(in_text)
 
 else:
  player = 0
  in_text = 'Its your turn Red!'
  message.setText(in_text)
  
 return player

#-------------------------------------------------------------------------------

def restart():
 global ices, initial_moves, player_turn, point
 
 for x in range(ROW):
  for y in range(COLOUMNS):
   if ices[x][y][1] == COLOURS[0]:
    ices[x][y][0].setFill(COLOURS[1])
    ices[x][y][1] = COLOURS[0]
    
 list_players[0].undraw()
 list_players[1].undraw()
 
 initial_moves = [[[0, 2],[0, 3],[1, 2],[1, 3],[1, 4],[0, 4],],
           [[9, 2],[8, 2],[8, 3],[8, 4],[9, 4],[9, 3],], 
           [[0, 3], [9, 3]]]
 
 point = 1
 get_players()
 player_turn = first_move()

#-------------------------------------------------------------------------------

def game():
 global point, x, y, message, in_text
 """
 function displays title and opens player gifs. Calls squares() and options() 
 to set up board game and buttons. while loop is set up that based on location 
 of click displayed title will change and display different message. If button 
 is clicked, action will be performed.
 parameters: N/A
 return: N/A
 """
 board = squares()
 quit, reset = options(win)
 in_text, message = display_msg()
 red_p, blue_p, list_player = get_players()
 player_turn = first_move()
 
 while True:
  point = win.getMouse()
  x = int(point.x)
  y = int(point.y)


  coord_grid = convert_to_grid(point)
  move_valid(point, ices)
  #move_piece(player, player_turn)
  #caluclate_range_movement(player)
  #update_moves(player, player_turn)
  #break_ice_valid()
  #break_ice(shatter)
  #change_players(player_turn)
  
  #if y >= 317:
   #message.setText(in_text) 

  if in_box(point, reset):
   in_text = "RESET"
   message.setText(in_text)
   win.getMouse()
   red_p
   blue_p
   player = first_move()
   
  
  elif in_box(point, quit):
   in_text = "BYE BYE!"
   message.setText(in_text)
   win.getMouse()
   break
   
 win.close()

win = GraphWin("ICE BREAKER GAME", WIN_W, WIN_H)
win.setBackground('gray')

game()

