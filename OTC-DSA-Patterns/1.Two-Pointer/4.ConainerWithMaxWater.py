#https://leetcode.com/problems/container-with-most-water/

#1)Calculate area by squaring min height among 2 pointers
#2)Move pointer with min height to get max area
#3)Compare area(store the largest area)

def maxArea(height):
    left = 0
    right = len(height)-1
    max=0

    while left<right:
        current = (min(height[left], height[right]))*(right-left)
        if current>max:
            max=current
        if height[left]>=height[right]:
            right-=1
        else:
            left+=1
    return max

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))