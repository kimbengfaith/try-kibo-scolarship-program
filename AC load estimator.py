# Write your AC Load Estimator solution here
#input the width of the room
width=float(input("enter the width of the room: "))
# input the height of the room
height=float(input("enter the height of the room: "))
# input the number of people in the room
number_of_people=int(input("enter the number of people in the room: "))
# calculating the horse power
horse_power=width*height*0.1+number_of_people*0.06
# print the horse power
print(f"the horse power is: {round(horse_power,2)}")