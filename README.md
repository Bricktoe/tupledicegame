# Tuple Dice Game - README

## Overview
The Tuple Dice Game is a simple Python program that simulates rolling three dice. The game tracks the player's cumulative score and high score as they roll the dice repeatedly. Players can decide when to stop rolling and view their final scores or roll three of the same dice and "Tuple Out" and score 0.

This program uses the Python `random` module to simulate the randomness of dice rolls and demonstrates the use of tuples for managing related data.

---

## Features
- Simulates rolling three dice with random values between 1 and 6.
- Displays individual dice rolls and their total score.
- Keeps a **history of all dice rolls**, displayed at the end of the game.
- Uses **time tracking** to calculate and display the total playtime.
- Includes a feature where players can "tuple out" (when all three dice show the same value), causing the game to end.
- Interactive gameplay with prompts for continuing or ending the game.

---

## Installation
1. Ensure you have Python installed on your computer.
2. Download or copy the `tuple_dice_game.py` file.
3. Open a terminal or command prompt in the directory where the file is saved.

---

## How to Play
1. Run the program:
   ```bash
   python tuple_dice_game.py

2. Press Enter to roll the dice. The program will show the values of the three dice and their total score.
3. Continue rolling the dice until you decide to stop or until you roll the same value on all three dice ("tuple out").
4. At the end of the game, the program will display:
- Your final score.
- Your high score.
- Total playtime.
- A history of all dice rolls.

## Example Gameplay
```bash
🎲🎉 Welcome to the Tuple Dice Game! 🎉🎲
Try to get the highest score possible! 🚀

👉 Press Enter to roll the dice... 🎲
🎲 You rolled: 3, 5, and 6 (Total: 14) 🎲
Your current score is: 14

Do you want to roll again? (yes/no): yes

🎲 You rolled: 4, 4, and 4 (Total: 12) 🎲
Your current score is: 26

Do you want to roll again? (yes/no): no

🎲 Your Dice Roll History:
   Die 1  Die 2  Die 3  Total
0      3      5      6     14
1      4      4      4     12

⏱️ Total playtime: 30.45 seconds

🎮 Game Over! 🎮
Your final score: 26
🏅 Your high score: 90
🎲 Thanks for playing!
