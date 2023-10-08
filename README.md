# Nebula Battlefront!
**Nebula Battlefront** is an interactive text-based game where the player and a computer opponent each have spaceships on a grid-based board. The player's goal is to sink all of the computer's spaceships before the computer does the same to the player's spaceships.

The game includes the following features:
- **Title Screen:** The game starts with a title screen where the player can choose to play or exit.
- **Board Setup:** The player chooses the board size and the number of spaceships they want to place on the board.
- **Spaceship Placement:** The player can choose to manually place their spaceships or have them placed randomly on the board.
- **Gameplay:** The player takes turns guessing the coordinates of the computer's spaceships on the grid. If they hit a spaceship, it is marked as "sunk," and the player earns a point. If they hit a planet, they get an extra turn. If they miss, it's marked as a miss. The computer also takes turns making guesses.
- **Win/Lose Conditions:** The game ends when either the player or the computer sinks all of the opponent's spaceships. A win or loss message is displayed in ASCII art.
- **Typewriter Effect:** The game uses a typewriter effect to display messages one character at a time, creating a dynamic and engaging user experience.

## How to play Nebula Battlefront
### Getting started
1. Navigate to the [Game](https://nebulabattlefront-5344b7c09f5f.herokuapp.com/)
2. If its not started upon loading hit the button **"RUN PROGRAM"** this will initialize the terminal with a new instance of the game.
3. Two otions now **"yes"** to play or **"no"** to end the game.
4. choose your option. All prompts must be followed by hitting **ENTER** key. **Invalid** enteries will be prompted to try again.
5. Now enter a username.
6. Now choose a board size 5 or greater. (eg. 5 is a 5x5 grid) **Recommendation** Keep board size udner 10 on the web version.
7. Now enter how many ships you want to have in the game minimum 5 and maximum is 30% of the grid size. (eg. 5x5 min 5 max 7)
8. Choose to place ships yourself or let the game pick randomly. choice 1 is manual (You place) and 2 is randomly where the game chooses.
9. If manually placed you are prompted for each ships x and y coordinates with a space between them. (Eg. "1 2")
10. Once all ships are placed the game will begin.
11. Now the player and computer will take turns guessing until either the player or the computer sink all their opponents ships.
12. If a ship is hit an explosion will appear on the board.
13. If a planet is hit a planet will appear on the board.
14. If nothing is hit a "M" will apprear on the board.
15. If all the players ships are sunk a **Loss** message will appear.
16. If all the computers ships are sunk a **Win** message will appear.
17. To play again relaunch the game with **"RUN PROGRAM"** button.

---
## User Stories
- As a **player**, I want to be able to see a title screen when I start the game, with the option to choose whether I want to play the game or not.
- As a **player**, I want to be able to input my name when starting the game so that the game can address me by my name during gameplay.
- As a **player**, I want to choose the size of the game board (minimum size of 5x5) so that I can have different levels of difficulty.
- As a **player**, I want to specify the number of spaceships I want to place on the board (between 5 and 30% of the board size) so that I can control the game's difficulty and challenge.
- As a **player**, I want to have the option to place my spaceships manually on the board, selecting the coordinates one by one, so that I can strategize and plan my placement.
- As a **player**, I want to have the option to place my spaceships randomly on the board, so that I can quickly start the game without manual placement.
- As a **player**, I want to see my own game board and the computer's game board during gameplay, with hidden spaceships on the computer's board, so that I can make informed guesses.
- As a **player**, I want to make guesses on the computer's game board by specifying X and Y coordinates, so that I can attempt to hit the computer's spaceships.
- As a **player**, I want the game to notify me when I hit a spaceship, so that I can keep track of my progress.
- As a **player**, I want the game to notify me when I hit a planet, giving me an extra turn to make another guess, so that I have a chance to continue playing.
- As a **player**, I want the game to notify me when I miss a target, so that I can keep track of my attempts.
- As a **player**, I want the game to keep track of the number of rounds played, so that I can see how long the game took.
- As a **player**, I want to be able to clear the terminal screen during gameplay for a better gaming experience.
- As a **player**, I want to enjoy typewriter-style text effects for an engaging and retro feel during the game.
- As a **player**, I want the game to end and display a win message when I have successfully sunk all of the computer's spaceships, so that I can celebrate my victory.
- As a **player**, I want the game to end and display a loss message when the computer has successfully sunk all of my spaceships, so that I can acknowledge defeat.
- As a **player**, I want to see ASCII art displayed for win and loss messages to add visual appeal to the game.

---
## Testing
### How I tested
| What test was completed | Passed? Y(yes)/N(no) |
|:-----------------------:|:-------------------:|
| Title screen displays correctly | Y |
| Player can choose to play or exit on Title screen | Y |
| Manual placement of spaceships | Y |
| Random placement of spaceships | Y |
| Valid input for coordinates | Y |
| Hit opponent's spaceship | Y |
| Sunk opponent's spaceship | Y |
| Hit a planet and received extra munitions | Y |
| Game ends when a player wins | Y |
| Game ends when all rounds are played | Y |
| Running the game at all playble stages | Y |

### bugs encountered

| Bugs/Issues Encountered | How problem was fixed | Fixed Y(yes)/N(no) |
|:-----------------------:|:---------------------:|:------------------:|
| Had numerious issues getting planets to work correctly | Took several itterations of code and testing to find one I was satisfied with which is called extra munitions now | Y |
| If a user types outside of a prompt, the terminal may inadvertently accept that input for the next prompt. | Was unable to find a good working solution that didn't hinder gameplay | N |
| Manual ship placement was causing issues as it seemed to be updating guessed locations | Fix was added a clear guessed locations for player and computer after ships have been placed| Y |
| While not a direct bug due to terminal size for launched version of the project you can make a large board thats difficult to guess on | Its intended but user discression advised | N/A |

---
## Validation testing
### Python

All Scripts checked with [PEP8 Code institute](https://pep8ci.herokuapp.com/)

| **Line** | **Errorrs or Warning** | **Does it affect game play Negativly?** |
|:----------:|:---------------:|:-------------:|
| 16 | E501 line too long (99 > 79 characters) | No |
| 31 | E501 line too long (114 > 79 characters) | No |
| 66 | E501 line too long (92 > 79 characters) | No |
| 89 | E501 line too long (92 > 79 characters) | No |
| 98 | E501 line too long (98 > 79 characters) | No |
| 123 | E501 line too long (92 > 79 characters) | No |
| 132 | E501 line too long (93 > 79 characters) | No |
| 135 | E501 line too long (88 > 79 characters) | No |
| 136 | E501 line too long (113 > 79 characters) | No |
| 151 | E501 line too long (83 > 79 characters) | No |
| 154 | E501 line too long (87 > 79 characters) | No |
| 181 | E501 line too long (90 > 79 characters) | No |
| 202 | E501 line too long (82 > 79 characters) | No |
| 203 | E501 line too long (94 > 79 characters) | No |
| 208 | E501 line too long (92 > 79 characters) | No |
| 209 | E501 line too long (122 > 79 characters) | No |
| 214 | E501 line too long (114 > 79 characters) | No |
| 215 | E501 line too long (80 > 79 characters) | No |
| 230 | E501 line too long (122 > 79 characters) | No |
| 234 | E501 line too long (96 > 79 characters) | No |
| 242 | E501 line too long (84 > 79 characters) | No |
| 246 | E501 line too long (99 > 79 characters) | No |
| 248 | E501 line too long (144 > 79 characters) | No |
| 250 | E501 line too long (113 > 79 characters) | No |
| 254 | E501 line too long (93 > 79 characters) | No |
| 256 | E501 line too long (92 > 79 characters) | No |
| 258 | E501 line too long (87 > 79 characters) | No |
| 278 | E501 line too long (84 > 79 characters) | No |
| 282 | E501 line too long (92 > 79 characters) | No |
| 284 | E501 line too long (88 > 79 characters) | No |
| 288 | E501 line too long (92 > 79 characters) | No |
| 289 | E501 line too long (90 > 79 characters) | No |
| 290 | E501 line too long (83 > 79 characters) | No |
| 293 | E501 line too long (94 > 79 characters) | No |
| 295 | E501 line too long (82 > 79 characters) | No |
| 303 | E501 line too long (101 > 79 characters) | No |
| 304 | E501 line too long (89 > 79 characters) | No |
| 305 | E501 line too long (92 > 79 characters) | No |
| 319 | E501 line too long (82 > 79 characters) | No |
| 329 | E501 line too long (82 > 79 characters) | No |
| 333 | E501 line too long (97 > 79 characters) | No |
| 335 | E501 line too long (82 > 79 characters) | No |
| 348 | E501 line too long (92 > 79 characters) | No |
| 355 | E501 line too long (119 > 79 characters) | No |
| 356 | E501 line too long (87 > 79 characters) | No |
| 357 | E501 line too long (86 > 79 characters) | No |
| 361 | E501 line too long (98 > 79 characters) | No |
| 364 | E501 line too long (112 > 79 characters) | No |
| 370 | E501 line too long (102 > 79 characters) | No |
| 373 | E501 line too long (82 > 79 characters) | No |
| 376 | E501 line too long (97 > 79 characters) | No |
| 378 | E501 line too long (80 > 79 characters) | No |
| 382 | E501 line too long (89 > 79 characters) | No |
| 390 | E501 line too long (97 > 79 characters) | No |
| 397 | E501 line too long (117 > 79 characters) | No |
| 398 | E501 line too long (84 > 79 characters) | No |
| 399 | E501 line too long (92 > 79 characters) | No |
| 412 | E501 line too long (85 > 79 characters) | No |
| 417 | E501 line too long (82 > 79 characters) | No |
| 418 | E501 line too long (80 > 79 characters) | No |
| 435 | E501 line too long (126 > 79 characters) | No |

---
## Deployment
Used GitHub and heroku to bring the site to life [View The Site Here](https://nebulabattlefront-5344b7c09f5f.herokuapp.com/)

## Technology used
- [Python](https://www.w3schools.com/python/)
- [Code Institute Python escentials template](https://github.com/Code-Institute-Org/python-essentials-template)
- [Visual Studios Code (VSCode)](https://visualstudio.microsoft.com/)
- [Github](https://github.com/)
- [Hypervisor (virtual enviorment)](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/)
- [Git](https://git-scm.com/)
- [Github Desktop App](https://desktop.github.com/)
- [ui.dev Am I Responsive](https://ui.dev/amiresponsive)

## Wireframes

## Credits
- [picsart ASCII Art generation tool](https://tools.picsart.com/text/font-generator/text-art/)

- [clear terminal code](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)

- [Typewriter effect code](https://stackoverflow.com/questions/20302331/typing-effect-in-python)

- [My wife](https://www.twitch.tv/flame_121) who’s been supper supportive of this change in career for me and just being out right amazing we will get her into this one way or another I am sure.

- [Code Institute](https://codeinstitute.net/) for providing an excellent accelerated learning platform worth every penny.
---
## Future feature ideas
| **Features to add** | **Added Y(yes)/N(no)** |
|:-------------------:|:--------------------:|
| Multiplayer Mode | N |
| Leaderboard | N |
| Sound effects | N |
| Other in game powerups/effects | N |