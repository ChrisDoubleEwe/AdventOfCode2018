import re

num_players = 13
last_marble = 7999

game = [0, 4, 2, 1, 3]
current_marble_pos = 1
current_marble_val = 4
current_turn = 4

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
 
class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
        self.items = 0
 
    def get_len(self):
        return self.items

    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current

    def get_next_node(self, ref_node):
        return ref_node.next

    def get_previous_node(self, ref_node):
        return ref_node.prev

 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
        self.items += 1
 
    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)

 
    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.items += 1
        else:
            self.insert_after(self.first.prev, new_node)

 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node

 
    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next
        self.items -= 1

 
    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print str(current.data) + ' ' ,
            current = current.next
            if current == self.first:
                break
        print ' ' 
 
 
game = CircularDoublyLinkedList()

new_node = Node(0)
game.insert_at_beg(new_node)

current_node = Node(4)
game.insert_at_end(current_node)

new_node = Node(2)
game.insert_at_end(new_node)

new_node = Node(1)
game.insert_at_end(new_node)

new_node = Node(3)
game.insert_at_end(new_node)


score= []
for i in range(0, num_players+1):
  score.append(0)

def game_out():
  if current_marble_val % 10000 == 0:
    print current_marble_val


while current_marble_val <= last_marble:
  game_out()
  current_turn += 1
  if current_turn > num_players:
    current_turn = 1

  this_marble_val = current_marble_val + 1

  if this_marble_val % 23 == 0:
    # Do something different
    score[current_turn] += this_marble_val
    current_node = game.get_previous_node(current_node)
    current_node = game.get_previous_node(current_node)
    current_node = game.get_previous_node(current_node)
    current_node = game.get_previous_node(current_node)
    current_node = game.get_previous_node(current_node)
    current_node = game.get_previous_node(current_node)
    remove_node = game.get_previous_node(current_node)
    score[current_turn] += remove_node.data
    game.remove(remove_node)
  else:
    # Do usual
    current_node = game.get_next_node(current_node)
    new_node = Node(this_marble_val)
    game.insert_after(current_node, new_node)
    current_node = new_node

  current_marble_val = this_marble_val
    

winning_score = 0
winning_player = 0
for i in range(0, num_players):
  if i > 0:
    if score[i] > winning_score:
      winning_score = score[i]
      winning_player = i
 
print "Marbles = " + str(last_marble) + " : Player " + str(winning_player) + " wins with a score of " + str(winning_score)

