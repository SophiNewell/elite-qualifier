import random
from colored import fg

user = input("Fav color?(violet, red, yellow, white, green, blue, cyan, magenta) ")
color = fg(user)
print (color + 'Surprise!!')
choice = input(color + 'do you like it?(yes/no) ')
if choice.lower() == "yes":
  print("Great! \\(^v^)/")
else:
  color = fg('white')
  print(color + "Sorry... (>n<)")
  
topics = [
"anime",
"sports",
"harry potter",
"games",
"music",
]

def decide_topic(user_input, topics):
  if user_input.lower() == "anime":
    topic = "anime"
  elif user_input.lower() == "sports":
    topic = "sports"
  elif user_input.lower() == "harry potter":
    topic = "harry potter"
  elif user_input.lower() == "games":
    topic = "games"
  elif user_input.lower() == "music":
    topic = "music"
  return topic
def generate_response(user_input, topic):
  
    if topic == "anime":
      responses = [
        "Who's you're favorite?",
        "What about Given?",
        "What are you're thought's on Sword Art Online?",
        "That's pretty awesome!",
        "What all have you seen?",
        "Me too!"
      ]
    elif topic == "sports":
      responses = [
        "What's you're team?",
        "Thought's on Soccer?",
        "Soccer is my favorite",
        "Did you see the game?",
        "Awesome, right?!",
        "Me too!"
      ]
    elif topic == "harry potter":
      responses = [
        "Who's you're favorite?",
        "My favorite is George...Weasely, of course",
        "That deleted scene where Draco helps Harry is awesome",
        "That's pretty awesome!",
        "What's you're favorite book?",
        "Me too!"
      ]
    elif topic == "games":
      responses = [
        "What's you're favorite?",
        "What systems do you use?",
        "I disagree",
        "That's pretty awesome!",
        "Thoughts on Genshin Impact?",
        "Me too!"
      ]
    elif topic == "music":
      responses = [
        "Who's you're favorite artist?",
        "I don't like rap much",
        "They're pretty good",
        "Awesome",
        "I like For King and Country right now, but it switches",
        "Me too!"
      ]
    return random.choice(responses)
 
for topic in topics:
  print(topic.capitalize())
user_input = input("What do you wanna talk about?\n")
if user_input.lower() in topics:
  actual_topic = decide_topic(user_input, topics)
  while user_input != "q":
      print(generate_response(user_input, actual_topic))
      user_input = input()

else:
    print("I know nothing on that topic, sorry.")
