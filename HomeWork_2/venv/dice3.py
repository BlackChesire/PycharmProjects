"""
Student: Asaf Ben Shabat
ID: 312391774
Assignment no. 2
Program: dice3
"""
from random import randint
n = int(input("Please number of rolls:"))
k = int(input("Please enter amount of same number series at leaset"))
roller = 0
target = 0
times = 0
sarel = 0 #תשנה לאיזה שם שבא לך
loop = 0 #תשנה לאיזה שם שבא לך
while   roller < n :
    dice_1, dice_2, dice_3 = randint(1, 6), randint(1, 1), randint(1, 1)
    roller +=1
    print(dice_1, dice_2, dice_3)
    if dice_1 == dice_2 == dice_3:
        target += 1
        times += 1
        if target >= k:
              sarel = loop
              break
    loop +=1
if target >= k:
      print("Target reached")
      print("reached",k,"equal series after" ,sarel+1 , "games")