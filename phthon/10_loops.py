#while_loop

# i = 1
# while i<=10:
#     print("hello world")  #print HW 10 times
#     i = i+1


# total=0  #sum of 1-10
 
# n = input("enter a number") 
# n = int(n)
# total = 0
# i=1
# while i <= n:
#     total = total + i
#     i = i + 1
# print(total)




# #adding numbers by typing them
# number = input("enter a number")
# #"1256"
# #int(number[i])

# total = 0
# i = 0
# while i < len(number):
#     total += int(number[i])
#     i += 1
#     print(total)




# #count alphabets

# name = input("Please enter your name")
# temp_var = ""
# i=0
# while i < len(name):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#         i += 1




# #infite loop

# while True:
#     print("hello world")



# #for loop with range function

# for i in range(10):    # 0 to 9 tak print hoga
#   print("hello world")
#   print(f"hello world : {i}\n")

#   for i in range(1,11):
#       print(f"hello world : {i}")



# #for loop sum 
# #sum 1 to 10

# total = 0
# for i in range(1,10):
#       total += i
# print(total)

n=int(input("enter the number:"))
total =0
for i in range(1,n+1):
    total += i
    print(total)


