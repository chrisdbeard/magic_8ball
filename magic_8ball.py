import random

name = input("Hello! Your name? ")
question = input("What would you like to ask the Magic 8-Ball? ")
random_number = random.randint(1, 9)


if random_number == 1:
    answer = "Yes"
elif random_number == 2:
    answer = "It is certain."
elif random_number == 3:
    answer = "Most likely."
elif random_number == 4:
    answer = "Outlook good."
elif random_number == 5:
    answer = "It is decidedly so."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "Ask again later."
elif random_number == 8:
    answer = "Very doubtful."
elif random_number == 9:
    answer = "Don't count on it."
else:
    answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball: " + answer)