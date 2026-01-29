# Elevator Problem

This is the second problem in the series of me trying to improve my writing and learning system design. Today I am tackling the Elevator problem. 

### Elevator System for a Multi Storey Problem
Design an elevator control system for a building. The system should handle multiple elevators, floor requests, and move elevators efficiently to service requests. 

### Requirements

The first step of the solution will be define the requirements of the system. Let's say for example we have 3 elevators and 10 floors.

We would have to define the scope of the different actors involved before we can start coding. Here, the actors are `elevator` and `floor`. 

`Elevator`:
- needs to go up and down
- has three state: stationary, moving and out of order
- can only pick people up if in stationary
- can be called from internally (someone pressing the button) or externally (by a floor) 

Out of scope:
- Weight or maximum capacity requirement 
- door mechanics
- continuous time implementation or discrete steps

Floor:
- only needs to request elevators

### Class Design and Schemas

```py
class Elevator:
    currentFloor: int 
    direction: Direction 
    requests: Set<Request>

class Direction(enum):
    UP: 'UP'
    DOWN: 'DOWN'
    STATIONARY: 'STATIONARY'
```

```py
class ElevatorOrchestrator:
    elevators: List[Elevator]
```

Something that I did not initially think about but is important is thinking type of Request. It can just be an intger with type up/down but it really is not ideal. Let's say multiple people want to get to go to floor 7 so the elevator stops at floor 7 and removes it from the set. It works, but real life can't be that simple, can it? 
