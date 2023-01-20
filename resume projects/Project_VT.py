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
COLOURS = ['blue', 'white']
player_gifs = ['red_dot.gif', 'blue_dot.gif']
list_players = []
ices = [] #broken/unbroken pieces
#initial_moves is a list of all valid moves a player can make at the start of the game
initial_moves = [[[0, 2],[0, 3],[1, 2],[1, 3],[1, 4],[0, 4],],
          [[9, 2],[8, 2],[8, 3],[8, 4],[9, 4],[9, 3],], 
          [[0, 3], [9, 3]]]
win, point, move, ice = None,None,None,None  #main screen; mouse click; while loops 

#-------------------------------------------------------------------------------

def start_menu():
 global win
 
 win_beg = GraphWin('ICEBREAKER', WIN_W, 400)
 win_beg.setBackground('light blue')  
 
 start = Rectangle(Point(40, 120), Point(160, 70))
 start_txt = Text(Point(100, 95), 'START GAME')
 start.draw(win_beg)
 start_txt.draw(win_beg)
 
 name = Text(Point(WIN_W - 100, 75), 'NAME: VICTOR TADROS')
 name.draw(win_beg)
 title = Text(Point(WIN_W - 100, 50), 'ICE BREAKER GAME')
 title.draw(win_beg)
 
 start = True
 while start == True:
  begin = win_beg.getMouse()
  if 80 < begin.x < 140 and 70 < begin.y < 120:
   win_beg.close()
   break 

#-------------------------------------------------------------------------------
def square(x, y):
 """
 Purpose: Function creates board for game using variables listed above
 Parameters: x, y; coordinates of each square
 Return: N/A
 """
 global ices
 
 left = GAP + x * (WIN_S + GAP)
 top = GAP + y * (WIN_S + GAP)
 rect = Rectangle(Point(left, top), Point(left + WIN_S, top + WIN_S))
 ices[x][y].append(rect)
 ices[x][y].append(COLOURS[1])
 ices[x][y][0].setFill(COLOURS[1])
 ices[x][y][0].draw(win)

#-------------------------------------------------------------------------------

def squares():
 """
 Purpose: Function makes rows and columns of squares to complete icebreaker board
 Parameters: N/A
 Return: N/A
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
 """
 Purpose: Function will display messages as game is played
 Parameters: N/A
 Returns: N/A
 """
 global message, in_text, player_text, player_msg
 
 in_text = ''
 message = Text(Point(150, 375), in_text)
 message.draw(win)
 
 player_text = ''
 player_msg = Text(Point(150, 360), player_text)
 player_msg.draw(win) 
 

#-------------------------------------------------------------------------------

def quit_button():
 """
 Purpose: Function will create quit button which will exit game once clicked on
 Parameters: N/A
 return: N/A
 """
 global win
 
 quit = Rectangle(Point(322, 400), Point(378, 420))
 quit.setFill('white') 
 text_q = Text(Point(350, 410), 'QUIT')
 quit.draw(win)
 text_q.draw(win)
 
#-------------------------------------------------------------------------------

def reset_button():
 """
 Purpose: Function will create reset button which will reset game once clicked on
 Parameters: N/A
 Returns: N/A
 """ 
 global win
 
 reset = Rectangle(Point(322, 425), Point(378, 445))
 reset.setFill('white')
 text_re = Text(Point(350, 435), 'RESET') 
 reset.draw(win)
 text_re.draw(win)

#-------------------------------------------------------------------------------

def board_game():
 """
 Purpose: Function will set up board display
 Parameters: N/A
 Returns: N/A
 """
 board = squares()
 quit_button()
 reset_button()
 get_players()
 display_msg()
 
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
 """
 Purpose: Function will draw players and append initial coordinates to list
 Parameters: N/A
 Returns: N/A
 """
 global red_p, blue_p, list_players, red_point, blue_point, player_points
 
 red_point = Point(25, 160)
 red_p = Image(red_point, player_gifs[0])
 red_p.draw(win)
 list_players.append(red_p)
 
 blue_point = Point(WIN_W - 24, 160)
 blue_p = Image(blue_point, player_gifs[1])
 blue_p.draw(win)
 list_players.append(blue_p)
 print(list_players)
 
 player_points = [red_point, blue_point]
 
 return

#-------------------------------------------------------------------------------

def convert_to_grid(point):
 """
 Purpose: Function will use click coordinates and if on the board, return coloumn and row.
 else, display x and y coordinates
 Parameters: point; click coordinates
 Returns: coord_grid; list of coordinates 
 """
 global message, in_text, coloumn, row, ices, x, y
 coord_grid = []
 x = int(point.x)
 y = int(point.y) 
 coloumn = int((x - 5) / 45) 
 row = int((y - 5) / 45) 

 if y >= 317:
  in_text = f"COORDINATE: {x}, {y}"
  message.setText(in_text)

 else: 
  point1 = ices[coloumn][row][0].getP1()
  point2 = ices[coloumn][row][0].getP2()
  coord_grid.append([x, y, point1, point2, [coloumn, row]]) 
  in_text = f"COORDINATE: {coloumn + 1}, {row + 1}"
  message.setText(in_text)

 return coord_grid 

#-------------------------------------------------------------------------------

def first_move():
 """
 Purpose: Function will pick randomly b/w 0 and 1. Depending on the value, red or blue will make a move
 Parameters: N/A
 Returns: player
 """
 global red_p, blue_p, player_text, player_msg
 
 player = random.randint(0, 1)
 
 if player == 0:
  for i in range(7):
   red_p
  player_text = 'PLAYER: 0'
  player_msg.setText(player_text)
  
 elif player == 1:
  for i in range(7):
   blue_p
  player_text = 'PLAYER: 1'
  player_msg.setText(player_text)    
 
 return player
        
#-------------------------------------------------------------------------------

def check_click():
 '''
 Purpose: Function will check where mouse clicks
 Parameters: N/A
 Return: True; board clicked
 '''
 global point, coloumn, row, x, y
    
 point = win.getMouse() 
 if 322 < point.x < 378 and 425 < point.y < 445:
  in_text = "RESET"
  message.setText(in_text)
  win.getMouse()
  restart()
  
 elif 322 < point.x < 378 and 400 < point.y < 420:
  in_text = "BYE BYE!"
  message.setText(in_text)
  win.getMouse()
  point = 0
  
 elif point.y <= 317:
  return True
 
 else:
  convert_to_grid(point)

#-------------------------------------------------------------------------------

def move_valid():
 '''
 Purpose: function will check if player can move their piece. valid moves are up, down, left, right or diagonally on white ices.
 Parameters: N/A
 Return: True; move is valid
 '''
 global win, ices, player, point
    
 player = convert_to_grid(point)
 #check if move is valid
 if ices[player[0][4][0]][player[0][4][1]][1] != COLOURS[0] and player[0][4] in initial_moves[player_turn] and player[0][4] not in initial_moves[2]:                    
  move_piece(player, player_turn)
  return True
    
#-------------------------------------------------------------------------------
    
def move_piece(player, player_turn):
 '''
 Purpose: Function will make player perform a move 
 Parameters: player; coordinate of player from click
             player_turn; 0 or 1, deciding which players turn it is
 Return: N/A
 '''
 global win, ices, list_players, player_text, player_msg, x, y
    
 list_players[player_turn].undraw()
 
 #draw player gifs into middle of ice
 list_players[player_turn] = Image(Point((player[0][2].x + player[0][3].x) / 2, (player[0][2].y + player[0][3].y)/ 2), player_gifs[player_turn])
 list_players[player_turn].draw(win)
 
 player_text = f'PLAYER: {player_turn} --> ({coloumn + 1}, {row + 1})'
 player_msg.setText(player_text)

 update_initial_moves(player, player_turn)

#-------------------------------------------------------------------------------

def calc_range(player):
 '''
 Purpose: Function will calculate the min. and max. range for valid moves.
 Used by update_initial_moves() to calculate the values in between min. and max.
 Parameters: player; coordinate of player from click
 Return: range_
 '''
 i_beg, i_end = int(player[0][4][0]) - 1, int(player[0][4][0]) + 2
 x_beg, x_end = int(player[0][4][1]) - 1, int(player[0][4][1]) + 2
 
 if int(player[0][4][1]) == 0 and int(player[0][4][0]) == 0:
  i_beg, x_beg = int(player[0][4][0]), int(player[0][4][1])
  
 elif int(player[0][4][0]) == 0 and int(player[0][4][1]) == 6:
  i_beg, x_end = int(player[0][4][0]), int(player[0][4][1]) + 1
  
 elif int(player[0][4][0]) == 9 and int(player[0][4][1]) == 6:
  i_end, x_end = int(player[0][4][0]) + 1, int(player[0][4][1]) + 1
  
 elif int(player[0][4][0]) == 9 and int(player[0][4][1]) == 0:
  i_end, x_beg = int(player[0][4][0]) + 1, int(player[0][4][1])
  
 elif int(player[0][4][1]) == 0:
  x_beg = int(player[0][4][1])
 
 elif int(player[0][4][0]) == 0:
  i_beg = int(player[0][4][0])
 
 elif int(player[0][4][1]) == 6:
  x_end = int(player[0][4][1]) + 1
 
 elif int(player[0][4][0]) == 9:
  i_end = int(player[0][4][0]) + 1
 
 range_ = i_beg, i_end, x_beg, x_end
 return range_

#-------------------------------------------------------------------------------

def update_initial_moves(player, player_turn):
 '''
 Purpose: function will update initial_moves with valid moves
 Parameters: player; coordinate of player from click
             player_turn; 0 or 1, deciding which players turn it is
 Return : initial_moves; list of valid moves
 '''
 global initial_moves, ices

 initial_moves[player_turn] = []
 initial_moves[2][player_turn] = player[0][4]
 range_ = calc_range(player)
    
 for i in range(range_[0], range_[1]):
  for x in range(range_[2], range_[3]):
   #check the square beside if blue and if other player is there
   if ices[i][x][1] != COLOURS[0]:
    initial_moves[player_turn].append([i, x])
    
    #initial_moves ubdate: remove occupied squares from the list for both players
 if initial_moves[2][player_turn] in initial_moves[player_turn]:
  initial_moves[player_turn].remove(initial_moves[2][player_turn])
 
 if initial_moves[2][not player_turn] in initial_moves[not player_turn]:
  initial_moves[not player_turn].remove(initial_moves[2][not player_turn]) 
 
 if initial_moves[2][player_turn] in initial_moves[not player_turn]:
  initial_moves[not player_turn].remove(initial_moves[2][player_turn]) 
 
 if len (initial_moves[player_turn]) == 1 and initial_moves[2][not player_turn] in initial_moves[player_turn]:
  initial_moves[player_turn].remove(initial_moves[2][not player_turn]) 
    
  return initial_moves

#-------------------------------------------------------------------------------

def ice_crash_valid():
 '''
Purpose: function will check and see if ice is white or i a player is on it already. 
Parameters: N/A
Return: True; valid move
'''
 global win, ices, player_turn, initial_moves, point
    
 point_ = point
 shatter = convert_to_grid(point_)                        
                            
 if ices[shatter[0][4][0]][shatter[0][4][1]][1] == COLOURS[1] and initial_moves[2][0] != shatter[0][4] and initial_moves[2][1] != shatter[0][4]:
  crash_ice(shatter)  
  if shatter[0][4] in initial_moves[not player_turn]:
   initial_moves[not player_turn].remove(shatter[0][4])
  player_turn = change_players(player_turn)
  return True
    
#-------------------------------------------------------------------------------
    
def crash_ice(shatter):
 '''
 Purpose: Break the ice; change the color of the square to blue. A square 
 cannot be 'broken' twice.
 Parameters: break_ice; turn ice to blue on click
 Return: N/A
 '''
 global player, initial_moves, ices, player_turn
    
 ices[shatter[0][4][0]][shatter[0][4][1]][0].setFill(COLOURS[0])
 ices[shatter[0][4][0]][shatter[0][4][1]][1] = COLOURS[0]

 update_initial_moves(player, player_turn)

#-------------------------------------------------------------------------------
    
def change_players(player_turn):
 '''
 Purpose: function will determine who plays next
 Parameters: player_turn: 0 or 1, previous player
 Return: player_turn: 0 or 1, next player
 '''
 global in_text, message
 
 if player_turn == 0:
  player_turn = 1
  player_text = 'PLAYER: 1'
  player_msg.setText(player_text)
   
 else:
  player_turn = 0
  player_text = 'PLAYER: 0'
  player_msg.setText(player_text)
  
 return player_turn

#-------------------------------------------------------------------------------

def restart():
 '''
  Purpose: Restart the game: change the color of squares from blue to white; 
  reset initial_moves, undraw players
  Parameters: N/A
  Return: N/A
  '''
 global ices, initial_moves, player_turn, point, list_players
 
 for x in range(ROW):
  for y in range(COLOUMN):
   if ices[x][y][1] == COLOURS[0]:
    ices[x][y][0].setFill(COLOURS[1])
    ices[x][y][1] = COLOURS[1]
    
 list_players[0].undraw()
 list_players[1].undraw()
 get_players()
 
 initial_moves = [[[0, 2],[0, 3],[1, 2],[1, 3],[1, 4],[0, 4],],
           [[9, 2],[8, 2],[8, 3],[8, 4],[9, 4],[9, 3],], 
           [[0, 3], [9, 3]]]
 
 point = 1
 player_turn = first_move() 
 
#-------------------------------------------------------------------------------
    
def winner():
 '''
 Purpose: The function will see if a player is not be able to move, meaning the player loses the game. If after the move neither player has available moves, nobody wins. 
 Parameters: N/A
 Return: N/A
 '''    
 global initial_moves, message, in_text
     
    
 if len(initial_moves[0]) == 0 and len(initial_moves[1]) == 0:
  in_text = "DRAW!"
  message.setText(in_text)
  initial_moves = []
  return True
 elif len(initial_moves[1]) == 0:
  in_text = "PLAYER 0 WINS!"
  message.setText(in_text)  
  initial_moves = []
  return True
 elif len(initial_moves[0]) == 0:
  in_text = "PLAYER 1 WINS!"
  message.setText(in_text)    
  initial_moves = []
  return True

#-------------------------------------------------------------------------------

def after_winner():
 ''' Purpose: Display options in a new GraphWindow if there is a winner: Quit or Restart
 Parameters: N/A
 Return: True; if quit is clicked 
               False; if quit not clicked 
 '''    
 global win
 
 if_winner = winner()
 if if_winner:                   
  
  win_end = GraphWin('ICEBREAKER', 200, 200)
  win_end.setBackground('light blue')  
  
  choice = Text(Point(100, 50), 'RESTART OR QUIT?')
  choice.draw(win_end)
  
  reset = Rectangle(Point(40, 120), Point(160, 70))
  reset.draw(win_end)
  reset.setFill('white')
  text_re = Text(Point(100, 95), 'RESET') 
  text_re.draw(win_end)
  
  quit = Rectangle(Point(40, 180), Point(160, 130))
  quit.draw(win_end)
  quit.setFill('red') 
  text_q = Text(Point(100, 155), 'QUIT')
  text_q.draw(win_end)
    
  while True: 
   if_winner_point = win_end.getMouse()
   if 40 < if_winner_point.x < 160 and 70 < if_winner_point.y < 120:
    restart()
    win_end.close()
    if_winner = False
    break
   elif 40 < if_winner_point.x < 160 and 130 < if_winner_point.y < 180:
    win_end.close()
    return True 
   
#-------------------------------------------------------------------------------

def play_game_player():
 '''
 Purpose: Function will perform in order of: make valid move, move player; check for winner
 Parameters: N/A
 Return: True; if quit is clicked
 '''
 global win, point, move, ice
    
 move = -1
 while move == -1: 
  click = check_click()
  if point == 0:         #if clicked on "QUIT"   
   return True
  elif click:         #if clicked on board
   player_move = move_valid()  #check move is valid
   if player_move:
    move, ice = point, -1
    winner = after_winner()   #if there's a winner
    if winner:                #if clicked on "QUIT"      
     return True
    play_game_ice()
   else:
    move = -1

#-------------------------------------------------------------------------------

def play_game_ice():
 '''
 Purpose: Function will perform in order of; make valid move, break an ice; check for winner
 Parameters: N/A
 Return: True; if quit is clicked
 '''                           
 global win, point, ice, in_text, message
    
 while ice == -1:
  in_text = "BREAK ICE"
  message.setText(in_text)
  click_2 = check_click()    
  if point == 0:                  #if clicked on "QUIT"   
   return True
  elif point == 1:                
   ice = point            
   break
  elif click_2:                #if clicked on the board
   shatter = ice_crash_valid()
   if shatter:           #if the square can be broken
    point_ = point                            
    ice = point_
    winner = after_winner()  #if there's a winner
    if winner:               
     point = 0 
   else:
    ice = -1  

#-------------------------------------------------------------------------------
                
def single_game():
 '''
 Purpose: Function will perform a game
 Parameters: N/A
 Return: N/A
 '''    
 global win, player_turn, point 
 
 board_game()
 player_turn = first_move()
 OK = True
 while OK == True: 
  quit = play_game_player()
  if quit or point == 0:            
   OK = False
   win.close()                            
   break

#-------------------------------------------------------------------------------
       
def main():
 """
 Purpose: function will call start_menu() and open new GraphWin, then call single_game()
 Parameters: N/A
 Return: N/A
 """
 global win
 
 start_menu()

 win = GraphWin('ICEBREAKER', WIN_W, WIN_H)
 win.setBackground('light blue')
 
 single_game()
 
#------------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()
