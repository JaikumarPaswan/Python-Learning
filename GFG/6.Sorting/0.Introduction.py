# sort() works only for list
l1 = [5, 10, 15, 1]
l1.sort()
print(l1)

#reverse parameter
l2 = [1,6,4,9]
l2.sort(reverse=True)
print(l2)

l3 = ["gfg", "ide", "courses"]
l3.sort()
print(l3)


def myFun(l):
    return len(l)

#key parameter
l = ["gfg", "idea", "courses"]
l.sort(key = myFun)
print(l)

#Both are optional
l.sort(key = myFun, reverse = True)
print(l)


#Sorting user defined Objects

# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def fun(p):
#         return p.x
    

# l = [point(1, 15), point(10, 5), point(3,8)]

# l.sort(key = fun)

# for i in l:
#     print(i.x, i.y)



# 1. Using __lt__ method  #less-than
# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __lt__(self, other):   #less-than function
#         return self.x < other.x


# l = [point(1, 15), point(10, 5), point(5,8)]
# l.sort()

# for i in l:
#     print(i.x, i.y)



# 2. Using __lt__method 

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):   #less-than function
        if self.x == other.x:
            return self.x < other.y
        else:
            return self.x < other.x


l = [point(1, 15), point(10, 5), point(1,8)]
l.sort()

for i in l:
    print(i.x, i.y)