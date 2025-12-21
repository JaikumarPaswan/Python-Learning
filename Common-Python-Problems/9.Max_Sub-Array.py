#T.C:- O(n^2)

# def maxSubArray(nums):
#     max=None
#     for i in range(len(nums)):
#         for j in range(i+1):
#             if sum(nums[i:j]) > max:
#                 max = sum(nums[i+j])

#     return max



#T.C:- O(n) #Kadane's Algo

def maxSubArray(nums):
        maxi = nums[0]

        cur_sum = 0

        for i in range(len(nums)):
            cur_sum = max(cur_sum, 0)
            cur_sum += nums[i]

            maxi = max(cur_sum, maxi)
        
        return maxi