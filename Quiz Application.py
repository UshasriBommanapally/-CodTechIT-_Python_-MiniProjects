# Quiz questions stored in a dictionary where the key is the question and the value is a tuple of options and the correct answer
quiz_questions = {
    "What is the capital of France?": (["A. London", "B. Paris", "C. Rome", "D. Berlin"], "B"),
    "What is the largest planet in our solar system?": (["A. Venus", "B. Jupiter", "C. Mars", "D. Earth"], "B"),
    "Who wrote 'Romeo and Juliet'?": (["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"], "A")
}

def display_question(question, options):
    print(question)
    for option in options:
        print(option)
    answer = input("Enter your answer (A, B, C, or D): ").upper()
    return answer

def check_answer(question, user_answer):
    correct_answer = quiz_questions[question][1]
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def main():
    print("Welcome to the Quiz Application!")
    print("Let's test your knowledge.\n")

    score = 0
    for question, (options, _) in quiz_questions.items():
        user_answer = display_question(question, options)
        score += check_answer(question, user_answer)
        print()

    print("Quiz completed!")
    print("Your score:", score, "out of", len(quiz_questions))

if __name__ == "__main__":
    main()
