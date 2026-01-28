# Connect 4 implementation
from enum import Enum
from typing import Optional

class gameState(Enum):
    WIN = 'WIN',
    IN_PROGRESS = 'IN_PROGRESS',
    DRAW = 'DRAW'

class CellState(Enum):
    P1 = 1,
    P2 = 2,


class Player:
    def __init__(self, name: str, id: CellState) -> None:
        self.name = name,
        self.id = id

class Board:
    def __init__(self, row: int = 6, col: int = 7) -> None:
        self.row = row
        self.col = col
        self.board: list[list[Optional[CellState]]] = [[None for _ in range(col)] for _ in range(row)]
    
    def getCellState(self, row: int, col: int) -> Optional[CellState]:
        return self.board[row][col]
    
    def dropDisk(self, col, player: Player):
        # see if col is available. 

        # we can go to 0 and check and place where it is available. O(m) lookup everytime
        # if we can use have a column height tracking it will be Player1
        for i in range(self.row, -1, -1):
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




