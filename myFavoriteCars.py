# myFavoriteCars
# Prints out my 3 favorite cars, using tuples and lists
# Nick Misuraca
# 9/3/22

favoriteCar1 = (2022, "Nissan", "GT-R", "Black")
favoriteCar2 = (2022, "Chevy", "Silverado TrailBoss", "Red")
favoriteCar3 = (2023, "BMW", "M8 Coupe", "Blue")

cars = [favoriteCar1, favoriteCar2, favoriteCar3]

for i in cars:
    alist = list(i) #Convert tuple to list
    alist.insert(1, alist.pop(3)) #Researched Insert method and used slice notation to rearrange the color
    print(*alist)
  




# like strings, tuples cannot have their values modified, appended, or removed
# one advantage to using a tuple is that it can be intended for that
# value not to change (can reduce accidental mistakes) and telling others devs that you dont 
# want it to change. 
# Also as stated, python can implement some optimizations that can
# make code using tuples slightly faster than code using lists.


