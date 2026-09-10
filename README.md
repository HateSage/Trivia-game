# Quiz / Trivia Game 🎯

A simple terminal-based trivia game built with Python. The game presents multiple-choice questions, accepts answers from the user, checks the answers, keeps track of the score, and displays the final result.

## Features

* Display trivia questions
* Display multiple-choice options
* Accept user answers
* Check answers
* Keep track of score
* Randomize questions
* Prevent questions from repeating
* Validate user input
* Display final results

## Technologies Used

* Python
* Lists
* Dictionaries
* Functions
* `for` and `while` loops
* Conditional statements
* String manipulation
* Randomization
* User input

## How It Works

The questions are stored separately from the program logic using a list of dictionaries:

```python
QUESTIONS = [
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    }
]
```

Each question contains:

* `question` — The question displayed to the user
* `options` — The available multiple-choice answers
* `answer` — The correct answer

The program randomly selects questions and allows the user to answer them one at a time.

## Example

```text
Welcome to the Trivia Challenge!

What is the capital of Nigeria?

1. Lagos
2. Abuja
3. Kano
4. Ibadan

> 2

Correct!
```

At the end of the game:

```text
Your score: 4/5
Your performance was good.
```

## Project Structure

```text
quiz-trivia/
│
├── main.py
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd quiz-trivia
```

Run the program:

```bash
python main.py
```

## Learning Objectives

This project was created to practice:

* Working with lists and dictionaries
* Creating and using functions
* Using loops
* Using conditional statements
* Handling user input
* Validating input
* Working with strings
* Using Python's `random` module
* Managing program flow
* Separating data from program logic

## Author

**HATE**

A Python learning project focused on building practical programming skills.
