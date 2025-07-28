'''
Author: fbs
Date: 07/27/2025
Description: This python code will solve a maze problem using states, BFS and DFS
'''

import sys

class Node():
    def __init__(self, state, actions, parent):
        self.state = state
        self.actions = [] 
        if actions:
            self.actions.append(actions)
        self.parent = parent

    def get_state(self):
        return self.state
    def get_actions(self):
        return self.actions
    def set_actions(self, actions):
        self.actions.append(actions)
    def get_parent(self):
        return self.parent   

class StackFrontier():
    def __init__(self):
        self.frontier = []
    def add(self, node):
        self.frontier.append(node)
    def remove(self):
         ret_value = self.frontier[-1]
         self.frontier = self.frontier[:-1]
         return ret_value
class QueueFrontier(StackFrontier):
    def remove(self):
         ret_value = self.frontier[0]
         self.frontier = self.frontier[1:]
         return ret_value

class Maze():
     def __init__(self, filename):
          with open(filename, 'rt') as fn:
               self.content = fn.read()

               #Make sure their is only one starting point and destination point
               if self.content.count('S') > 1 or self.content.count('S') <= 0:
                   raise Exception("Only 1 starting point allowed")
               if self.content.count('E') > 1 or self.content.count('E') <= 0:
                   raise Exception("Only 1 destination point allowed")
                   
               # Prints the Maze board
               print(f'\n{"The board": ^50}\n')
               for line in self.content.split('\n'):
                   line = line.strip()
                   print(*[x.replace('0', '-') for x in line])
            
               # Set various attributes of the Maze class
               self.height = len(self.content.split('\n'))
               self.width = max([len(row) for row in self.content.split('\n')])
               self.is_wall = []

               for i, row in enumerate(self.content.split('\n')):
                   wall_row  = []
                   for j in range(len(row)):
                       if self.content.split('\n')[i][j] == "S":
                            self.start = (i, j)
                            wall_row.append(True)
                       elif self.content.split('\n')[i][j] == "E":
                            self.stop = (i, j)
                            wall_row.append(False)
                       elif self.content.split('\n')[i][j] == "#":
                            wall_row.append(True)
                       else:
                            wall_row.append(False)
                   self.is_wall.append(wall_row)

     def actions(self, node):
         current_row, current_col = node.get_state()
         values = []
         for i, row in enumerate(self.content.split('\n')):
             for j in range(len(row)):
                 if i == current_row and j == current_col:
                    if (i - 1) >= 0 and not (self.is_wall[i - 1][j]):
                        values.append((("up", (i - 1, j)), node))
                    if (i + 1) < len(self.content.split('\n')) and not (self.is_wall[i + 1][j]):
                        values.append((("down", (i + 1, j)), node)) 
                    if (j + 1) < len(row) and not (self.is_wall[i][j + 1]):                 
                        values.append((("right", (i, j + 1)), node))
                    if (j - 1) >= 0 and not (self.is_wall[i][j - 1]):
                        values.append((("left", (i, j - 1)), node))
         node.set_actions(values)
         return values
     
     def solve(self, algo):
         start_node = Node(self.start, None, None)
         explored = []
         self.solution = []

         if algo == "dfs":
             frontier = StackFrontier()
         else:
             frontier = QueueFrontier()
        
         #start by adding start_node to frontier
         frontier.add(start_node)

         while frontier.frontier:
            if not frontier.frontier:
                raise Exception("Ops! no solution I must say")
            else:
                current_node = frontier.remove()

                if current_node.get_state()[0] == self.stop[0] and current_node.get_state()[1] == self.stop[1] :
                    print("Hurray! We have found path to your stop")
                    while current_node.get_parent():
                        self.solution.append(current_node.get_state())
                        current_node = current_node.get_parent()
                    self.solution = self.solution[::-1]
                    print(self.solution)
                    sys.exit()
                else:
                    actions = self.actions(current_node)
                    for action in actions:
                        #print(action)
                      
                        if action[0][1] not in [node.get_state() for node in explored] and action[0][1] not in [node.get_state() for node in frontier.frontier]:
                            node = Node(action[0][1], action[0], action[1])
                            if action[0][1][0] == self.stop[0] and action[0][1][1] == self.stop[1]:
                                print("Hurray! We have found path to your stop")
                                while current_node.get_parent():
                                    self.solution.append(current_node.get_state())
                                    current_node = current_node.get_parent()
                                self.solution = self.solution[::-1]
                                print(self.solution)
                                sys.exit()
                            else:
                                frontier.add(node)

                    # Current node will be appended to explored list
                    explored.append(current_node)
                    #print(f'Frontier after: {frontier.frontier}')
                    #print(f'Explored: {explored}\n')


if __name__ == "__main__":
    mymaze = Maze('./assets/maze.txt')
    mymaze.solve('dfs')


    
