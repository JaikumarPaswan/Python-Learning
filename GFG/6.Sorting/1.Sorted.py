#1. Works for any iterable( List,Tuple,Dictionary, String,Set,etc)
#2. Does not modify Original List, returns a new list with sorted items
#3. Parameters like reverse and key works same way as sort()

t = (10, 12, 5, 1)
print(sorted(t))

s = {"gfg", "courses", "python"}
print(sorted(s))

st = "gfg"
print(sorted(st))

d = {10:"gfg", 15:"ide", 5:"couurses"}
print(sorted(d))

l = [(10, 15), (1,3), (2,3)]
print(sorted(l))