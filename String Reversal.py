# Simple string reversal with user input, Enjoy!

print("""Welcome to the String Reversal Program!
------- """)


something = input("Reverse your sentence or word here: ")


def rev(word):
    return ' '.join([i[::-1] for i in word.split(' ')])


print(rev(something))

# Another way to reverse the input of a string, but doesn't keep them in the same position
# word = input("Reverse your sentence or word here: ")
# print(word[::-1])
