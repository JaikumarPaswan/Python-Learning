a = 8

#if-elif-else ladder in python

if(a<3):
    print("The value of a is smaller than 3")
elif(a>13):
    print("The value of a is greater than 13")
elif(a>7):
    print("The value of a is greater than 7")
elif(a>6):
    print("The value of a is greater than 6")
else:
    print("The value of a is greater than 13")

#2. Multiple if statements(all ifs independent of each other)(non-nested)
if(a<3):
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")

if(a>17):
    print("The value of a is greater than 17")

else:
    print("The value of a is greater than 3 or smaller than 17")            
