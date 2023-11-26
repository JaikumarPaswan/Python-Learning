# No.of slots in hash table(m) >= No.of keys to be inserted(n)
# Cache Friendly

#1.Linear Proabing (creates primary cluster):-
# Linear search for nextempty slot when there is a collision

#Search:- we compute hash function, we go to that index and compare if
# we find, we return true. Otherwise we linearlysearch. we stop when one 
# of the cases arises i)Empty slot, ii)Key Found, 
#                     iii)Traversed through the whole table.


#Deletion:- we replace the empty slot after deletion with any keyword 'deleted'
# So that while searching condition i) does not occur.


#2.Quadratic probing (creates secondary cluster):-
# hash(key,i)= (h(key) + i^2) % m

#works only when:- i) α<0.5
#                 ii) m is prime number

#3.Double hashing
# hash(key, i) = (h1(key) + i*h2(key))%m
         

