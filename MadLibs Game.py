# Follow the instructions in the tab to the right
# Write your mad libs program here
# importing libaries in python which would be used to read the story in a computer voice
from gtts import gTTS # gTTs = Google-text-to-speech
import os   # os= operating system
language='en'  # language is English

print("       PLAYING THE MAD LIBS GAME         ")
print()
print(
    "Hi!! there welcome to the Mad Libs game you are required to give examples of the following bellow. Enjoy the game and most importantly have Fun!!! "
)
print()   # print an empty line

# Assigning the various inputs to the various variables respectively
adjective=input("Adjective: ")
noun=input("pural Noun: ")
verb=input("verb Ending with ing: ")
noun_1=input("Noun: ")
celeb=input("Celebrity: ")
person=input("Person: ")
silly=input("Silly Word: ")
verb_1=input("Verb: ")
food=input("Type of Food(plural): ")
shoe=input("Type of shoe(plural): ")
some_thing=input("Some thing alive: ")


print()

print("*"*6+"     PARTY TIME!!     "+"*"*6)
print()
# Storing the story in the text variable
text = (
   f"One of the most {adjective} things about graduating is {noun} are {verb} in a huge party!!. I decided to have a backyard barbecure for all my family and {noun_1}. I invited my bestfriends,{celeb},{person} and of course my teacher Mrs {silly}.\n My dad is going to {verb_1} hambugers and {food} on his shiny new {noun_1}. He always thinks,his {food},taste really {adjective} but,I thing it taste like {adjective} {shoe}.\n My mom is going to make her famous {some_thing} salad, which is my favourite {noun_1} ever!! Mom said after we finish {verb},we can go swimming in our new {noun}."
)
# print the text on the screen for the reader to read the story
print(text)
print()
print("            THE END             ")
# converting the story stored in the text variable to an mp3 player
#  the mp3 player is bellow the main.py on the left hand side 
speech=gTTS(text=text, lang=language, slow=False)
speech.save("text.mp3")
os.system("start text.mp3")