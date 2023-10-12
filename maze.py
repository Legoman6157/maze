"""Defines maze class"""

import random
import numpy as np
from disjoint_set import DisjointSet

class Maze:
    '''Basic maze class'''
    def __init__(self, rows: int, cols: int):
        self.board = []
        self.rows = rows
        self.b_rows = self.rows*2-1
        self.cols = cols
        self.b_cols = self.cols*2-1
        
        self.reset()

    def reset(self):
        '''Resets the maze board'''
        self.board = []
        for i in range(self.rows):
            self.board.append([bool(True)]*(self.cols-1))
            if i != self.rows-1:
                self.board.append([bool(True)]*self.cols)

    def print_maze(self):
        '''Prints the maze board'''
        walls = ["|", "-"]
        between = [" ", "+"]

        i = 0

        print("+" + "-+"*self.cols)

        for row in self.board:
            if i%2 == 0:
                print("|", end="")

            print(between[i%2], end="")

            for col in row:
                print(walls[i%2] if col else " ", end=between[i%2])

            if i%2 == 0:
                print("|", end="")

            i += 1
            print()

        print("+" + "-+"*self.cols)



if __name__ == "__main__":
    maze = Maze(3, 3)
    maze.randomize()
    maze.print_maze()