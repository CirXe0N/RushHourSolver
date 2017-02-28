## Rush Hour Solver
Rush Hour is a tiny sliding board game played on a board of 6x6 squares.
The goal of the game is to get the red car out of a six-by-six grid full of automobiles by moving the other vehicles out of its way. 
However, the cars and trucks (set up before play according to a puzzle card) obstruct the path which makes the puzzle harder.

### Getting Started

 **Note**: This application has been developed and tested on [Python 3.52](https://www.python.org/downloads/)
  
#### Usage

    1. Add a game board file (.txt) to the directory **boards**.
    2. Run the program:
    
        $ python3 rush_hour_solver.py
      
    3. Follow the instructions on the screen and let the magic happen.


#### Game Board File Format

*  **A** through **J** represent the cars.
*  **rr** is the red car that needs to be freed.
*  The file needs to be saved as **text** file with the extension **.txt**

```
....AA
..BBCC
rr..EF
GGHHEF
...IEF
...IJJ 
 ```
 
  
