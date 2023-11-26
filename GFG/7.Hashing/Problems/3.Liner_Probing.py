#Code by author gfg

# def linearProbing(hashSize, arr, sizeOfArray):    
#         #storing -1 at all indexes in the hash table.
#         hash=[-1]*hashSize
        
#         #iterating over the array. 
#         for i in range(sizeOfArray):
            
#             #if the value of hash table at index (arr[i]%hashSize) is -1 
#             #which means empty then, we insert arr[i] at that place.
#             if(hash[arr[i]%hashSize]==-1): 
#                 hash[arr[i]%hashSize]=arr[i]
            
#             #else we move linearly from the filled position 
#             #to find an index with -1 in hash table.
#             else:
#                 k=(arr[i])%hashSize;
#                 counter=0
#                 flag = 0
#                 #using a loop which runs until we find an index with -1
#                 #in hash table which means empty.
#                 while(counter<hashSize and hash[k]!=-1):
#                     if(hash[k]==arr[i]):
#                         flag=1
#                         break
#                     k=(1+k)%hashSize;
#                     counter+=1
                
#                 if flag==1:
#                     continue
#                 #if we find a position where arr[i] can be inserted 
#                 #then we insert the element.
#                 if(counter<hashSize):
#                     hash[k]=arr[i]
                    
#         #returning the hash table.            
#         return hash



def linearProbing(hashSize, arr, sizeOfArray):
    hash_table = [-1] * hashSize

    for x in arr:
        position_x = x % hashSize

        if hash_table[position_x] == x:
            continue

        if hash_table[position_x] == -1:
            hash_table[position_x] = x
        else:
            counter = 0
            while hash_table[position_x] != -1 and counter < hashSize:
                if hash_table[position_x] == x:
                    break  # Skip insertion if duplicate is found
                position_x = (position_x + 1) % hashSize
                counter += 1
            if counter < hashSize and hash_table[position_x] != x:
                hash_table[position_x] = x

    return hash_table



hashSize = 10
sizeOfArray = 4
arr = [4,4,14,24,44]

print(linearProbing(hashSize, arr, sizeOfArray))