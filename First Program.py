import random

print("Guess some of my favorite things!"
      "-----")

favorite_animal = input("Guess my favorite animal: ")
if favorite_animal == "Lion":
    print("Correct!")
elif favorite_animal == "lion":
    print("Correct!")
else:
    print("Nope!")

favorite_food = input("Guess my favorite food: ")
if favorite_food == "bbq":
    print("Correct!")
elif favorite_food == "BBQ":
    print("Correct!")
else:
    print("Nope!")

favorite_color = input("Guess my favorite color: ")
if favorite_color == "Blue":
    print("Correct!")
elif favorite_color == "blue":
    print("Correct!")
else:
    print("Nope!")

print("""-----""")

print("That's the end of the game!")
question_one = input("How many did you get wrong?: ")

if int(question_one) == 3:
    print("You did pretty terrible.. Try the game again")
elif int(question_one) == 2:
    print("You did pretty terrible.. Try the game again")
elif int(question_one) == 1:
    print("Nice! not bad..")
elif int(question_one) == 0:
    print("Good Job! You know me a little!")
else:
    print("I only asked 3 questions.. play the game again")
