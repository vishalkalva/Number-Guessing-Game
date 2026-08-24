# 🎮 Task 1 - Number Guessing Game

## 📌 About the Project

This project was developed as part of my **Software Development Internship at Cognifyz Technologies**.

It is a simple text-based **Number Guessing Game** developed using Python. The computer generates a random number between 1 and 100, and the user has to guess the number.

The program provides feedback after every valid guess and displays the total number of attempts when the correct number is guessed.

## 🎯 Objective

The objective of this task is to develop a basic text-based game using:

- Conditional statements
- Loops
- User input
- Random number generation
- Exception handling

## ⚙️ Features

- 🎲 Generates a random number between 1 and 100
- 🔢 Accepts guesses from the user
- 📈 Displays "Too high!" when the guess is greater than the target
- 📉 Displays "Too low!" when the guess is smaller than the target
- 🏆 Displays a success message when the correct number is guessed
- 🔢 Counts the number of valid attempts
- ⚠️ Handles invalid non-numeric input using `try-except`
- 🔄 Continues the game until the correct number is guessed

## 🛠️ Technologies Used

- **Python**
- `random` module
- `try-except` exception handling

## 🧠 Python Concepts Used

- Variables
- `random.randint()`
- `input()`
- Type conversion using `int()`
- `while` loop
- `if`, `elif`, `else`
- `try-except`
- `ValueError`
- `break`
- `continue`

A simple output:
Enter a number between 1 and 100: 2
User number: 2
Attempts: 1
Too low!

Enter a number between 1 and 100: 10
User number: 10
Attempts: 2
Too low!

Enter a number between 1 and 100: 20
User number: 20
Attempts: 3
Too low!

Enter a number between 1 and 100: 60
User number: 60
Attempts: 4
Too low!

Enter a number between 1 and 100: 80
User number: 80
Attempts: 5
Too high!

Enter a number between 1 and 100: 60
User number: 60
Attempts: 6
Too low!

Enter a number between 1 and 100: 70
User number: 70
Attempts: 7
Too low!

Enter a number between 1 and 100: 75
User number: 75
Attempts: 8
Too low!

Enter a number between 1 and 100: 79
User number: 79
Attempts: 9
Too high!

Enter a number between 1 and 100: 78
User number: 78
Attempts: 10
Too high!

Enter a number between 1 and 100: 77
User number: 77
Attempts: 11
It's correct!

You guessed it in 11 attempts!

## ▶️ How to Run

1. Clone or download this repository.
2. Open the project in **VS Code**.
3. Open the terminal.
4. Run the following command:

```bash
python number_guessing_game.py


