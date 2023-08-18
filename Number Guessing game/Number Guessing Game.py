import random
lower_bound = int(input("Enter the lower limit of your range:"))
upper_bound = int(input("Enter the upper limit of your range:"))
if lower_bound>=upper_bound:
    upper_bound = int(input("Enter the upper limit of your range again:"))
answer = random.randint(lower_bound,upper_bound)
guess_no = 0
user_response = 0
while user_response != answer:
    guess_no +=1
    user_response = int(input("Guess the number:"))
    if user_response>upper_bound or user_response<lower_bound:
        print("This number is not in the range. Try guessing again.")
    if user_response == answer:
        print(f"{user_response} is the correct guess. You guessed it right in total of {guess_no} tries.")
    else:
        if user_response>answer:
            print("This number is greater than the answer. Try guessing again.")
        else:
            print("This number is smaller than the answer. Try guessing again.")