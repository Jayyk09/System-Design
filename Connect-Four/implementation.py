# Connect 4 implementation
from enum import Enum
from types import _ReturnT_co
from typing import Optional

class gameState(Enum):
    WIN = 'WIN'
    IN_PROGRESS = 'IN_PROGRESS'
    DRAW = 'DRAW'

class CellState(Enum):
    P1 = 1
    P2 = 2


class Player:
    def __init__(self, name: str, id: CellState) -> None:
        self.name = name
        self.id = id

"""
How the methods in Board and Game will interact

Board:
    getCellState: get state of individual cells 
    dropDisk: when player chooses a column, the Game drops it with column. Go to the lowest position in column, and drop the disk 
            
Game:
    makeMove: player chooses a col, and it checks if the move is valid and then calls dropDisk. it returns the win/draw/invalid/continue
    checkWin/Draw: when dropDisk returns [row,col] it looks through the pattern to check if it won/draw

"""

class Board:
    def __init__(self, row: int = 6, col: int = 7) -> None:
        self.row = row
        self.col = col
        self.board: list[list[Optional[CellState]]] = [[None for _ in range(col)] for _ in range(row)]

    def getCellState(self, row: int, col: int) -> Optional[CellState]:
        return self.board[row][col]

    def checkBound(self, row: int, col: int) -> bool:
        if (row >= self.row) or (col >= self.col) or (row < 0) or (col < 0):
            return False
        return True

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col
    
    def dropDisk(self, col, player: Player):
        # we can go to 0 and check and place where it is available. O(m) lookup everytime
        # if we can use have a column height tracking it will be Player1

        # since 0 is the top row and we start from bottom we need to go 5,4,3,2,1,0
        for i in range(self.row - 1, -1, -1):
            if self.board[i][col] == None:
                self.board[i][col] = player.id
                return [i, col]
        return None
        
class Game:
    def __init__(self, Player1: Player, Player2: Player, ) -> None:
        self.Player1 = Player1
        self.Player2 = Player2
        self.Board = Board()
        self.winner: Optional["Player"] = None
        self.currentPlayer: Player = Player1
        self.state: gameState = gameState.IN_PROGRESS

    def makeMove(self, col: int):
            # we drop the disk and if we get the [row, col] then we check win and Draw

            if self.state != gameState.IN_PROGRESS:
                return

            if col < 0 or col >= self.Board.getCol():
                return

            pos = self.Board.dropDisk(col, self.currentPlayer)
            if pos == None:
                return

            if (self.checkWin(pos[0], pos[1])):
                self.state = gameState.WIN
                self.winner = self.currentPlayer
            elif (self.checkDraw()):
                self.state = gameState.DRAW

            self.switchCurrentPlayer()

    def checkDraw(self) -> bool:
        for i in range(0,self.Board.getRow()):
            for j in range(0, self.Board.getCol()):
                if self.Board.getCellState(i,j) == None:
                    return False
        return True

    def checkWin(self, row: int, col: int) -> bool:
        directions = [
                (0,1), # horizontal
                (1,0), # vertical
                (1,1), # diagonal ->
                (1,-1) # diagonal <-
                ]
        
        for dir in directions:
            count = 1 
            # count in directions and return total count and add it to count and check if it's > 4
            count += self.count_in_direction(row, col, dir)
            count += self.count_in_direction(row, col, tuple(map(lambda x: -x, dir)))
            if count >= 4:
                return True
        return False

    def count_in_direction(self, row, col, dir) -> int:
        count = 0
        nr = row + dir[0]
        nc = col + dir[1]
        player = self.Board.getCellState(row, col)

        while self.Board.checkBound(nr, nc) and self.Board.getCellState(nr, nc) == player:
            count += 1 
            nr += dir[0]
            nc += dir[1]

        return count

    def switchCurrentPlayer(self):
        if self.currentPlayer == self.Player1:
            self.currentPlayer = self.Player2
        else:
            self.currentPlayer = self.Player1
