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

Elevator class take requests and handle which floor to go to next. The types seem to be direction, current floor and set of Requets. For now, i'd keep requests to a set of floor numbers. When somebody requests it, it gets added to the step and gets visited till hightest req is needed.

How would the function step would look like? check which direction we're going and check if there is a number in that direction. if yes keep going, else stop and remove it from the list.  stop there, and then remove it from the requests and then processe the next one?

if any other requests in that direction, then keep going else reverse and change direction. if no requests

```py
class Elevator:
    current_floor: int 
    requests: Set()
    direction: enum (up, down, idle) 

    step():
        if requests.contains(current_floor):
            requests.remove(current_floor)

        
        if dir == up and max(request > current_floor:
            keep going. increment current_floor
        else:
            dir =  down and current_floor -= 1

        if dir == down and min_requests < current_floor:
            keep going. decrement current floor
        else:
            dir = up and current_floor += 1

```
