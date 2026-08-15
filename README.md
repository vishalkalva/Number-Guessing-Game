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

## ▶️ How to Run

1. Clone or download this repository.
2. Open the project in **VS Code**.
3. Open the terminal.
4. Run the following command:

```bash
python number_guessing_game.py
