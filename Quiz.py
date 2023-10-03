import random
quiz_questions = [
    {
        'question': 'What is the primary purpose of pythons "if" statement?',
        'answer': 'To make a decision in code'
    },
    {
        'question': 'In python, how do you define a function?',
        'answer': 'def'
    },
    {
        'question': 'In python, which data type is used to store a sequence of values?',
        'answer': 'List'
    },
    {
        'question': 'In python, what is the purpose of the python "for loop"?',
        'answer': 'To iterate over a sequence'
    }
]

def run_quiz():
    score = 0

    print("\n*** Welcome to the Quiz Game! ***")
    print("Here are the rules: ...")
    print("1. You will be asked multiple-choice questions.")
    print("2. Give the answer corresponding to your question. ")
    print("3. You will receive feedback.")
    print("4. Your final score will be displayed at the end.")

    random.shuffle(quiz_questions)

    for question_data in quiz_questions:
        print("\nQuestion: " + question_data['question'])
        answer = input("Your answer: ").strip()

        if answer == question_data['answer']:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer. The correct answer is:", question_data['answer'])

    print("\nQuiz completed!")
    print("Final score:", score, "out of", len(quiz_questions))
    if score == len(quiz_questions):
        print("Congratulations! You got all questions right")
    else:
        print("Keep practicing! Better luck next time!")

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        run_quiz()
    else:
        print("*** exit ***")



run_quiz()
