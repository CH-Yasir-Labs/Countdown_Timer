#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     04/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import winsound  # Windows only
import time


def countdown_timer():
  print("Welcome to Countdown Timer App")
  while True:
        try:
            my_time = int(input("Enter the time in seconds to count: "))
            if my_time < 0:
                print("Please enter a positive number!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
  print("Time's Start")
  time.sleep(1)

  for x in range(my_time,0,-1):

    seconds= x%60
    mints=int(x/60)%60
    hours=int(x/3600)
    print(f"\r⏳{hours:02}:{mints:02}:{seconds:02}")
    time.sleep(1)

  winsound.Beep(1000, 1000)
  print("\n Time's Up!")

countdown_timer()

