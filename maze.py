'''
Author: fbs
Date: 07/27/2025
Description: This python code will solve a maze problem using states, BFS and DFS
'''

class Node():
    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent

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
                   for j, col in enumerate(row):
                       if self.content.split('\n')[i][j] == "S":
                            self.start = (i, j)
                            wall_row.append(True)
                       elif self.content.split('\n')[i][j] == "E":
                            self.stop = (i, j)
                            wall_row.append(True)
                       elif self.content.split('\n')[i][j] == "#":
                            wall_row.append(True)
                       else:
                            wall_row.append(False)
                       self.is_wall.append(wall_row)
            

if __name__ == "__main__":
    mymaze = Maze('./assets/maze.txt')


    
