# def isAnagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     s1_dict = {}
#     s2_dict = {}

#     for char in s1:
#         s1_dict[char] = s1_dict.get(char, 0)+1

#     for char in s2:
#         s2_dict[char] = s2_dict.get(char, 0)+1

#     return s1_dict == s2_dict

# print(isAnagram("apple", "apepl"))


# def isAnagram(s1, s2):
#     if len(s1)!=len(s2):
#         return False
    
#     sorted1 = sorted(s1)
#     sorted2 = sorted(s2)

#     return sorted1 == sorted2

# print(isAnagram("apple", "apepl"))    


def isAnagram(s1, s2):
    if len(s1)!=len(s2):
        return False
    
    count = [0]*256

    for i in range(len(s1)):
        count[ord(s1[i])] +=1
        count[ord(s2[i])] -=1

    for x in count:
        if x!= 0:
            return False
    return True

print(isAnagram("apple", "apepl")) 