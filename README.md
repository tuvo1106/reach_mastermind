<p align="center">
  <img src="https://miro.medium.com/max/700/0*4xohKyVpcqZPmT9y.png">
</p>

# Mastermind

This repository contains the Mastermind game written in Python3 for the command line.

## Table of Contents

- [Requirements](#requirements)
  - [Python](#python)
  - [Git](#git)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Development](#development)
  - [Class Diagram](#class-diagram)
  - [Activity Diagram](#activity-diagram)
- [Features](#features)
  - [Leaderboard](#leaderboard)
  - [Hints](#hints)
  - [Multiplayer](#multiplayer)
  - [Continuous Integration](#continuous-integration)
  - [Unit Testing](#unit-testing)
- [To Dos](#to-dos)
- [Special Thanks](#special-thanks)
- [Authors](#authors)

## Requirements

### Python

- Python 3.6 or above is required to run this application.
- [Download Python](https://www.python.org/downloads/)

### Git

- [Download Git](https://git-scm.com/downloads)

### Installation

- On your terminal, clone the repository with Git:

`git clone https://github.com/tuvo1106/reach_mastermind`

- In order to install all of the game dependencies, run this command from the root of the repo:

`pip install -r requirements.txt`

- To play the game, use the following command:

`python3 ./setup.py`

### Browser Options

- Alternatively, if you want to play on your browser, you can use the following link:
  - [![Run on Repl.it](https://repl.it/badge/github/tuvo1106/reach_mastermind)](https://repl.it/github/tuvo1106/reach_mastermind)
  - In the .replit file, make sure to configure the run command to be:
    `python3 ./setup.py`
  - Press "Run" to play!

## How to Play

In Mastermind, the player (aka the Codebreaker) has to guess a random
sequence of four numbers generated by the Codemaker, which can either be
the computer or another player. The Codebreaker wins when they guess both
the number and order correctly for all four numbers within a given amount
of turns. The breakdown of the different difficulties is shown below:

| Difficulty | Number Range | Number of Turns |
| :--------: | :----------: | :-------------: |
|    Easy    |    0 - 7     |       12        |
|   Normal   |    0 - 7     |       10        |
|    Hard    |    0 - 7     |        8        |
| Dark Souls |    0 - 9     |        6        |

Each guess is made by typing in 4 consecutive numbers in the terminal.
After each guess, the Codebreaker will get feedback on the previous
guess. The feedback is represented in the following symbols:

```
X = Correct number, correct location
O = Correct number, incorrect location
* = Incorrect number, incorrect location
```

For example, if the correct sequence is [1, 9, 0, 2] and the player guesses
[1, 2, 3, 4], the feedback that is given will be:

`X O * *`

- The (1) `X` represents the 1 being the right number in the right position.
- The (1) `O` represents the 2 being the right number, but in the wrong positon.
- The (2) `*` represents 3 and 4 both being incorrect numbers and therefore, not
  belonging on the board.

In another example, if the correct sequence is [3, 3, 6, 9] and the player
guesses [1, 3, 6, 9], the feedback that is given will be:

`X X X *`

- The (3) `X` represents 3, 6 and 9 being the right numbers in the right
  positions.
- The (1) `*` represents the remaining unmatched number 3 being compared with
  the only unmatched guess which is 1, therefore resulting in a mismatch of
  number and position.

## Development

### Class Diagram

![Class Diagram](/data/img/mastermind_class.png "Mastermind Class Diagram")

### Activity Diagram

![Activity Diagram](/data/img/mastermind_activity.png "Mastermind Activity Diagram")

## Features

### Leaderboard

Every time a player completes a game, their score is added to the high score.
This leaderboard is saved throughout sessions on the same machine. Many factors
contribute to a better score:

- Whether or not the player has won
- How many seconds it took the player to complete the game
- The difficulty
- Turns remaining after the last guess
- How many hints they used up

To reset the leaderboard to factory settings, run the following command:

`python3 ./data/reset_leaderboard.py`

### Hints

Players can ask for a hint by typing in 'h' when prompted for a guess. The
computer will then generate a random number and position on the board to
reveal.
Each hint, however, will cause the player to lose 25% of their total score.

### Multiplayer

Two players can play the game by taking turns creating a number sequence for the
other player has to guess. Whoever scores highest on the leaderboard wins!

### Continuous Integration

This repository is set up with a Github Actions workflow to test dependencies,
run a Pyflake8 linter and validate unit tests on every push.

[Check it out here!](./.github/workflows/mastermind.yml)

### Unit Testing

There is unit testing on various game objects. To administer the tests, enter
in the following command from the root of the repo:

`python -m unittest discover tests`

## To Dos

- Fully functional GUI on the browser, built with React or Vue
- Move local file storage to database for world-wide leaderboards
- Implement more unit tests

## Special Thanks

Thank you to the following people for beta-testing:
- [Ryuichi Miyazaki](https://github.com/rmiyazaki6499)
- [Farrukh Akhrarov](https://github.com/narnat)
- [Tim Assavarat](https://github.com/tassavarat)

## Authors

Created by:

- [Tu Vo](https://github.com/tuvo1106)
- Email: tuvo1106@gmail.com
