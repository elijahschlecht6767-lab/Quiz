def main():
    """ this is the main function"""
    questions=(
        "Which collection type is unable to be changed?",
        "Which collection type is unable to be ordered?",
        "What is the name of this loop --> [ for i in range(7): ] ?",
        "What is the name of this loop --> [ while 1+1==2: ] ?",
        "What is the name of this statement --> [ if 1+1==2: ] ?"
    )
    options=(
        ("A. list", "B. tuple", "C. set", "D. string"),
        ("A. tuple", "B. variable", "C. list", "D. set"),
        ("A. for loop", "B. if statement", "C. while loop", "D. dictionary"),
        ("A. set", "B. for loop", "C. while loop", "D. integer"),
        ("A. while loop", "B. tuple", "C. try and except", "D. if statement")
    )
    answers=("b", "d", "a", "c", "d")
    guesses=[]
    score=0
    question=0
    for i in range(len(questions)):
        question+=1
        print(f"Question {question}: {questions[i]}")
        for j in range(4):
            print(options[i][j])
        guesses.append(input("Enter A, B, C, or D: ").lower())
        print("")
        if guesses[i]==answers[i]:
            print("Correct!")
            score+=1
        else:
            print(f"Incorrect! The correct answer was {answers[i]}")
        print("")
    print("")
    print("----- RESULTS -----")
    print(f"Answers: {str(answers).upper()}")
    print(f"Guesses: {str(guesses).upper()}")
    print(f"Your score is {(score/len(questions))*100}%")


if __name__=="__main__":
    main()