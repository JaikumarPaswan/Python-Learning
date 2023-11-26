left_or_right = input(''' You're at a crossroad. Where do you want to go? Type "left" or "right"''').lower()
swim_or_wait = input().lower()
choose_color = input().lower()

if left_or_right == "right":
  print(''' You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.''')
elif left_or_right == "left":   
    print("You fell into a hole. Game Over.")
  
if swim_or_wait == "swim" :
  print("You get attacked by an angry trout. Game Over.")
elif swim_or_wait == "wait":
  print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")

if choose_color == "red":
  print("It's a room full of fire. Game Over.")
elif choose_color == "yellow":
  print("You enter a room of beasts. Game Over.")
elif choose_color == "blue":
  print("You found the treasure! You Win!")