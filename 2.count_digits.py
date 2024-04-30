# sum all the digits in integer

# def count(n):
#     string = str(n)
#     sum = 0
#     for i in range(len(string)):
#       sum = sum + int(string[i])

#     return sum

# print(count(114))


# Count digits of given integer

def count(n):
    result = 0
    while n>0:
        n = n//10
        result = result + 1
    return result

print(count(25094))
