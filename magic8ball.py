# magic8ball.py
# the following program defines a function that returns a different
# string depending on what number is passed in the argument
# Nick Misuraca
# 8/29/22

import random


print("What is your name?:")
yourName = input()

print("What is your Yes/No Question?:")
question = input()


def getAnswer(answerNumber):
    if answerNumber == 1:
        return yourName + "it is certain"
    elif answerNumber == 2:
        return yourName + "It is decidedly so"
    elif answerNumber == 3:
        return "yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return yourName + ", " + "Ask again later"
    elif answerNumber == 6:
        return yourName + ", " + "Concentrate and ask again"
    elif answerNumber == 7:
        return yourName + ", " + "My reply is no"
    elif answerNumber == 8:
        return yourName + ", " + "Outlook not so good"
    elif answerNumber == 9:
        return yourName + ", " + "Very doubtful"
    elif answerNumber == 10:
        return yourName + ", " + "Not a chance!"

r = random.randint(1, 10)
fortune = getAnswer(r)
print(fortune)


# Pythons two levels of scope is Global and Local. parameters and variables that are assigned in a called function
# is a local scope. and a global scope is variables that are assigned outside of all functions.
