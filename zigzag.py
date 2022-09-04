# zigzag.py
# This program will create a back-and-forth, zigzag pattern from the users inputted number
# until the user stops it by pressing the Mu editor’s Stop button or by pressing ctrl-C.
# Nick Misuraca
# 8/29/22


import time, sys

def runZigzag(numOfAsteriks):

    indent = 0 # How many spaces to indent.
    indentIncreasing = True # Whether the indentation is increasing or not.


    try:
           while True: # The main program loop.
              print(' ' * indent, end='')
              print (number * "*")

              time.sleep(0.1) # Pause for 1/10 of a second.


              if indentIncreasing:
                 # Increase the number of spaces:
                 indent = indent + 1
                 if indent == 20:
                     # Change direction:
                    indentIncreasing = False

              else:
                  # Decrease the number of spaces:
                  indent = indent - 1
                  if indent == 0:
                     # Change direction:
                     indentIncreasing = True


    except KeyboardInterrupt:
           sys.exit()


while True:
    try:
        print("Enter an Integer between 5 and 25: ")
        number = int(input())

        if number < 5 or number > 25:
            continue
        else:
            break

    except ValueError:
        print("You must enter an Integer.")
        continue

runZigzag(number)


# Summer
# Winter
# Summer
# Summer
# >>>
























