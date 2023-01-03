import random
import time
# Print a welcome message

print("Are you the fastest drawer in the west?\n Find out!")
print("When the screen says DRAW, press enter.")
#  use input() to wait for the user to press Enter
print(" ")
input("Press enter to start:\n ")
# Use time.time() again to get the time after the user pressed Enter
start= time.time()
# TODO 3: wait a random number of seconds, then print "DRAW!
print(" wait for it...")
wait=time.sleep(random.uniform(0,0.7))
print("DRAW!") 
# Get the current time with time.time()
current_time = time.time()

elapsed_time=current_time-start
# Print how long it took
print(elapsed_time)
# Print different results, based on how long it took
if elapsed_time > 0.3:
  print("Too slow! Try again next time. ")
elif elapsed_time < 0.1:
  print("You pressed enter too soon, didn't you? ")
else:
  print("You're the fastest draw in the west, congratulations! ")



 




