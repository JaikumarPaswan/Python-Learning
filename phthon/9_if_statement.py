# age = input("enter your age :")
# age = int(age)
# if age >= 14:
#        print("you are above 14")


# #  #pass statement
# #  x = 18
# #  if x > 18:
# #      pass


# #else statement

# age = input("enter your age :")
# age = int(age)
# if age >= 14:
#        print("you are above 14")
# else:
#        print("Sorry you can't play")


# #Exercise -> number guessing game

# winning_number = 27
# user_input = input("guesss a number b/w 1 and 100")
# user_input = int(user_input)
# if user_input == winning_number:
#     print("YOU WIN !!!")
# else:  #nested if else
#     if user_input < winning_number:
#        print("too low")
#     else:
#        print("too high")


# #and, or operator 

# name="abc"
# age=19
# if name == "abc" and age==19:
#     print("condition true")
# else:
#     print("condition false")


#     name="abc"
# age=19
# if name == "abc" or age==23:
#     print("condition true")
# else:
#     print("condition false")


# #if_elif_else

# age = input("please enter age")
# age = int(age)

# if 0<=age<3:
#     print("Ticket price: Free")
# elif 3<age<=10:
#      print("Ticket price: 150")
# elif 10<age<=60:
#      print("Ticket price: 250")
# else:
#     print("Ticket price : 200")


#in_keyword

# name ="Jai"
# if "a" in name:
#     print("a is present in a")
# else:
#     print("Not present")


#check_empty_or_not 

# name= "abc"
# if name:   # true if string is not empty
#     print("string is not empty")
# else:
#     print("string is empty")    


name = input("enter your name")

if name:   # true if string is not empty
    print(f"Your name is {name}")
else:
    print("You did'nt type anything")  

