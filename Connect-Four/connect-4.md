## What is Connect 4?

It is a two player game where players take turns dropping discs into a 7-column, 6-row board. The first to align four of their own discs vertically, horizontally, or diagonally wins

## Requirements scope

We only need to implement the logic here, no UI. This simplies the problem such that we need not worry about public paths for now.

Player Interaction: the Player chooses a column and if it is valid, the disk falls down to the lowest position

Win Requirements: If the pattern matches for 4, it's a win. If the board fills up, it is a draw. 

If in an interview, I might ask additional questions like do we need to track history and support undo? Is the board configurable?


## Schema Definition

Before we define schema there is a need to define which states need to be tracked. Some may be obvious, some not. 

#### States to track: 
    Progress of game
    players and their turn
    Winner
    Board

 So based on this this we need three classes:

```py
Class Game:
    state = GameState
    player1
    player2
    Winner
    Board

class GameState(Enum):
    winner = auto(),
    draw = auto(),
    in_progress = auto()
```

```py
class CellState(Enum):
    EMPTY = 0
    P1 = 1
    P2 = 2

Class Board:
    column: int = 7
    row: int = 6
    board: CellState[row][col]
```

```py 
Player:
    name: string
    state : CellState
```

This is a high level implementation detail of how the Connect4 should work. There are some design choice I have made and I will explain them below:

1. I have used enums in GameState. The other option is to use multiple boolean values like in_progress = true, has_won = true, is_draw = true. The problem with this approach is that the three states are very tightly coupled, so at every move there is a need to update all of them. 
```
# the game is won, we would need to update every single value for synchronization
{
    has_won = true,
    in_progress = false
    is_draw = false
}
```

2. I used enums for CellState - The Board only cares about which player owns a cell, not who the player is. CellState is a lightweight representation of ownership. Player simply carries which CellState it corresponds to
