questions = ("1. main? ",
            "2. subject? ",
             "3. love? ",
             "4. who? ")
options = (
    ("A. ace", "B. bollocks", "C. Tentative"),
    ("A. ace", "B. bollocks", "C. Tentative"),
    ("A. ace", "B. bollocks", "C. Tentative"),
    ("A. ace", "B. bollocks", "C. Tentative")
)

answers = ("A", "A", "A", "A")
guesses = []
score = 0
quiz_num = 0

for question in questions:
    print(question)
    print("________")
    for option in options[quiz_num]:
        print(option)
    answer = input("answer: ").upper()
    if answer == answers[quiz_num]:
        score += 1
        print("correct")
        guesses.append(answer)
    else:
        print("incorrect answer")
        
print(guesses)
score = int(score)/4 * 100
print(score)