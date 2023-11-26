#Find maximum of 3 numbers
#code by me

# def maximum(num1, num2, num3):
#     if (num1>num2 and num1>num3):
#         return num1
#     elif(num2>num1 and num2>num3):
#         return num2
#     else:
#         return num3

# m = maximum(45,955,86)
# print(m)


#code by harry

def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3

m = maximum(455, 86, 96)
print(m)
