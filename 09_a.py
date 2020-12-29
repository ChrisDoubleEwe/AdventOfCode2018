import re

num_players = 413
last_marble = 71082

game = [0, 4, 2, 1, 3]
current_marble_pos = 1
current_marble_val = 4
current_turn = 4

score= []
for i in range(0, num_players+1):
  score.append(0)

def game_out():
  if current_marble_val % 10000 == 0:
    print current_marble_val

def xgame_out():
  print "[" + str(current_turn) + "] ",

  for i in range(0, len(game)):
    if i == current_marble_pos:
      print "(" + str(game[i]) + ")",
    else:
      print str(game[i]) + ' ',
  print ' ' 

while current_marble_val <= last_marble:
  current_turn += 1
  if current_turn > num_players:
    current_turn = 1

  this_marble_val = current_marble_val + 1

  if this_marble_val % 23 == 0:
    # Do something different
    score[current_turn] += this_marble_val
    this_marble_pos = current_marble_pos - 7
    if this_marble_pos < 0:
      this_marble_pos = len(game) + this_marble_pos
    score[current_turn] += game[this_marble_pos]
    if this_marble_pos == len(game)-1:
      game.pop(this_marble_pos)  
      this_marble_pos = 0
    else:
      game.pop(this_marble_pos)

  else:
    # Do usual
    this_marble_pos = current_marble_pos + 2 
    if this_marble_pos > (len(game)):
      this_marble_pos = this_marble_pos - len(game)
    game.insert(this_marble_pos, this_marble_val)

  current_marble_val = this_marble_val
  current_marble_pos = this_marble_pos 
    

  


  game_out()

winning_score = 0
winning_player = 0
for i in range(0, num_players):
  if i > 0:
    if score[i] > winning_score:
      winning_score = score[i]
      winning_player = i
 
print "Marbles = " + str(last_marble) + " : Player " + str(winning_player) + " wins with a score of " + str(winning_score)

