import numpy as np
import random

class Game2048:
    def __init__(self, size=4):
        self.size = size
        self.reset()
        
    def reset(self):
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.add_random_tile()
        self.add_random_tile()
        
    def add_random_tile(self):
        available_positions = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if available_positions:
            i, j = random.choice(available_positions)
            self.board[i][j] = 2 if random.random() < 0.9 else 4
            
    def move(self, direction):
        # direction can be: 0 (up), 1 (right), 2 (down), 3 (left)
        original_board = self.board.copy()
        
        if direction == 0:  # up
            for j in range(self.size):
                column = self.board[:, j].tolist()
                new_column = self._merge(column)
                self.board[:, j] = new_column
        elif direction == 1:  # right
            for i in range(self.size):
                row = self.board[i, :][::-1].tolist()
                new_row = self._merge(row)
                self.board[i, :] = new_row[::-1]
        elif direction == 2:  # down
            for j in range(self.size):
                column = self.board[:, j][::-1].tolist()
                new_column = self._merge(column)
                self.board[:, j] = new_column[::-1]
        elif direction == 3:  # left
            for i in range(self.size):
                row = self.board[i, :].tolist()
                new_row = self._merge(row)
                self.board[i, :] = new_row
                

        if not np.array_equal(original_board, self.board):
            self.add_random_tile()
            
    def _merge(self, line):

        non_zeros = [num for num in line if num != 0]
        zeros = [0] * (len(line) - len(non_zeros))
        merged_line = non_zeros + zeros

        i = 0
        while i < len(merged_line) - 1:
            if merged_line[i] == merged_line[i+1] and merged_line[i] != 0:
                merged_line[i] *= 2
                merged_line.pop(i+1)
                merged_line.append(0)
                i += 2
            else:
                i += 1
        return merged_line
    
    def game_over(self):

        if 0 in self.board:
            return False
        # Check for possible merges in rows and columns
        for i in range(self.size):
            for j in range(self.size-1):
                if self.board[i, j] == self.board[i, j+1] or self.board[j, i] == self.board[j+1, i]:
                    return False
        return True
    
    def get_score(self):
        return np.sum(self.board)
    
    def get_board(self):
        return self.board.copy()

# Test the game logic
game = Game2048()
print("Initial board:")
print(game.get_board())

game.move(3) 
print("\nBoard after moving:")
# print(game.get_board())
