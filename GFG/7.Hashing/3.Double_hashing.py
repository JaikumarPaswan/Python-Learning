#Double hashing
# hash(key, i) = (h1(key) + i*h2(key))%m

#1) if h2(key) is relatively prime to m, then it always find a free slot
#   if there is one.

#2) Distributes skeysmore uniformly than linear probing and quadratic
#   hashing

#3) No clustering


#E.g

# hash(key, i) = (h1(key) + i*h2(key))%m

#m=7

#h1(key) = (key%7)
#h2(key) = 6-(key%6)  #6 is relatively prime to 7
