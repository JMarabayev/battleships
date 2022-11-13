# Welcome to my Python Battleships game!
## The rules of the game are quite simple:
1. You start the game by running the file
2. The computer generates 5 ships randomly in an 8x8 Grid
3. You are given X and Y coordinates in terms of letters (A-H) and Numbers (1-8) respectively
4. When you load the game, the output will display the grid and prompt you to select a number coordinate (1-8)
    * If you select a coordinate outside the grid the terminal would reset that selection and make you choose again
    * If you select an invalid coordinate, the terminal would reset your selection and let you choose again
5. Following the number coordinate, you would ave to select a letter coordinate (A-H)
    *  If you select a coordinate outside the grid the terminal would reset that selection and make you choose again
    * If you select an invalid coordinate, the terminal would reset that selection and let you choose again
6. If it is a hit, the computer would confirm it by printing the "Hit" statement and mark the ship as an X on your guess board
7. If it is a miss the computer would confirm it by printing the "Miss" statement and mark the ship as an - on your guess board
8. If you select the same coordinate you already chose before, the computer will display a "You already chose that" statement and let you choose again
    * No board would be printed in that case
9. After a shot, your "Tries" counter goes from 10 to 0 by incriments of 1 and when you reach 0 with enemy ships still remainig, it is game over
10. If you manage to destroy all enemy ships, Congratulations, You Win!

__When Making selections please make sure you wait for the input to prompt the selection, otherwise you might encounter an error!__

## Screenshots 
![Game Board](../battleships/screenshots/Screenshot%202022-11-13%20233457.png)
<br/>

![Gameplay](../battleships/screenshots/Screenshot%202022-11-13%20233525.png)
<br/>

![PEP8 Check](../battleships/screenshots/Screenshot%202022-11-13%20223355.png)
## Future additions to the code
* Allow the player to select the board size
* Different ship sizes
* Have the computer guess player ships (would probably be random at first and then implement AI)
* 2 Player Game
* Online multiplayer functionaity

## Bugs 
* The game runs into a critical error if selection is done before the input prompt
* System would recognise an empty input or an input like 12 as a viable input... Fixed with the help from stack overflow.

## Credits and References
* This game was created under the tutorial from "Knowledge Mavens" from [YouTube](https://www.youtube.com/watch?v=alJH_c9t4zw).
* System would recognise an empty input or an input like 12 as a viable input... Fixed with the help from stack overflow. user - [Samwise](https://stackoverflow.com/users/3799759/samwise)

## Checks
* This app passes through the relevant PEP8 without any major errors (Errors such as Whitespace and double lines between functions are visible as well as an error for a line that is too long.) in many cases I have chosen to ignore the small error due to maintaining the readability of the code.

## Challenges
* Biggest Challenge was checking  for empty strings. 
* Spent a lot of time to fix the issue in which user input beyond first would crash the game
