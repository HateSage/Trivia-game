import random

SCORE = 0

QUESTIONS = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["Lagos", "Abuja", "Kano", "Ibadan"],
        "answer": "Abuja"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "What type of data is `[1, 2, 3]` in Python?",
        "options": ["String", "Tuple", "List", "Dictionary"],
        "answer": "List"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "func", "def", "define"],
        "answer": "def"
    }
]


def random_question():
    question = random.choice(QUESTIONS)
    return question["question"], question["options"], question["answer"]

def Display_multiple_choice_options(option):
    number = 1
    for item in option:
        print(f"{number}. {item}")
        number = number + 1

def Accept_user_answers():
    return input("> ")


def Check_answers(answer, user_input):
    if answer.lower() == user_input.strip().lower():
        return True
    else:
        return False


def Add_score(SCORE):
    SCORE = SCORE + 1
    return SCORE


def Display_final_results():
    if SCORE < 3:
        print(f"Sorry your performance was bad with a score of {SCORE}/5\nDo better next time.")
    else:
        print(f"Your performance was good with a score of {SCORE}/5.")


def main():
    global SCORE

    print("Welcome to the Trivia Challenge!\nTest your knowledge, answer the questions, and see how high you can score!\nGood luck, and have fun!")

    marked = []

    while len(marked) < len(QUESTIONS):

        quest, option, answer = random_question()

        if quest in marked:
            continue

        marked.append(quest)

        print("\n" + quest)

        Display_multiple_choice_options(option)

        user_input = Accept_user_answers()

        if user_input in ["1", "2", "3", "4"]:
            user_input = option[int(user_input) - 1]

        if Check_answers(answer, user_input):
            print("Correct!")
            SCORE = Add_score(SCORE)
        else:
            print("Your answer was wrong")
            print(f"The correct answer was {answer}")

    Display_final_results()


main()