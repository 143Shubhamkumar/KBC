# KBC

This Python script is a simple quiz game that asks the user a series of questions. The user accumulates prize money for each correct answer and can choose to quit the game at any time, taking the accumulated prize money up to that point.

# Features

**Dynamic Greeting:** Greets the user based on the current time of day.

**Multiple Choice Questions:** Presents a series of questions with four possible answers.

**Prize Levels:** Prize money increases with each correct answer, with specific milestone amounts.

**Quit Option:** The user can quit the game at any time and keep the money they've won so far.

# How to Play
****Start the Game:****

The game will prompt you to enter your name.

It will greet you based on the current time of day.

**Answer Questions:**

You will be presented with a series of multiple-choice questions.

Enter the number corresponding to your answer (1-4).

If you want to quit the game, enter 0. You will win the prize money for the last correctly answered question.

**Winning Conditions:**

For each correct answer, you move to the next question and win the corresponding prize amount.

If you answer incorrectly, the game ends, and you lose all the accumulated prize money.

There are milestone prize amounts that you can secure by answering specific questions correctly.

# Code Structure
**Questions and Levels:**

questions: A list of questions, each with four possible answers and the index of the correct answer.

levels: A list of prize amounts corresponding to each question.

**Game Logic:**

Prompts the user for their name and greets them based on the current time.

Iterates through the list of questions, prompting the user for an answer.

Checks if the answer is correct and updates the prize money accordingly.

Allows the user to quit at any time by entering 0.

**Enjoy the game and see how much prize money you can win!**
