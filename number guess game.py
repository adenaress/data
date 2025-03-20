import random

highest_num = 100
lowest_num = 1
answer = random.randint(lowest_num, highest_num)
guesses = 0
whilerunning = True

print("------Python guessing game------")
print(f"----guess a number between {lowest_num}  {highest_num}----")

while whilerunning:
    guess = input("guess a number:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print(" number out of range")
            print(f"----guess a number between {lowest_num}  {highest_num}----")
        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("too high")
        else:
            print("correct")
            whilerunning = False
print(f"he correct answer is: {answer}")
print(f"you have tried {guesses} times")