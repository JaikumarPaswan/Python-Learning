# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1.lower()
name2.lower()

a1 = name1.count("t")
a2 = name1.count("r")
a3 = name1.count("u")
a4 = name1.count("e")

a5 = name2.count("t")
a6 = name2.count("r")
a7 = name2.count("u")
a8 = name2.count("e")


b1 = name1.count("l")
b2 = name1.count("o")
b3 = name1.count("v")
b4 = name1.count("e")

b5 = name2.count("l")
b6 = name2.count("o")
b7 = name2.count("v")
b8 = name2.count("e")

true_count = a1+a2+a3+a4+a5+a6+a7+a8

love_count = b1+b2+b3+b4+b5+b6+b7+b8

score = str(true_count) + str(love_count)

score = int(score)

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<=score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")