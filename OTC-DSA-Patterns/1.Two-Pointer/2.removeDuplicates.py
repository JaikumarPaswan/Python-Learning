#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicate(nums):
    i=0
    j=1
    count=1
    while j<len(nums):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
            j+=1
            count+=1
        else:
            j+=1
    return count


print(removeDuplicate([0,0,1,1,1,2,2,3,3,4]))

