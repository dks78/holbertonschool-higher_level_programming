#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastNumber = int(str(number)[-1]) 


if LastNumber < 5 :
    print(f"Last digit of {number} is {LastNumber} and is greater than 5")
elif LastNumber == 0 : 
    print(f"Last digit of {number} is {LastNumber} is 0 and is 0")
elif LastNumber > 6 or LastNumber != 0:
    print(f"Last digit of {number} is {LastNumber} and is less than 6 and not 0")
