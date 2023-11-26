#https://www.youtube.com/watch?v=GcW4mgmgSbw&list=WL&index=2&t=1s&ab_channel=BytebyByte

# Q) Given an array, find sum of all subarrays of length k

def fixed_sliding_window(list, k):
    #Sum up the first subarray and add it to the result
    curr_subarray = sum(list[:k])
    result = [curr_subarray]

    #To get each subsequent subarray ,add the next value in
    #the list and remove the first value

    for i in range(1, len(list)-k+1):
        curr_subarray = curr_subarray - list[i-1]
        curr_subarray = curr_subarray + list[i+k-1]

        result.append(curr_subarray)

    return result




#Q Find the shortest subarray with the sum that is greater or equal to x.

def dynamic_sliding_window(list, x):
    #Track our min value
    min_length = float("inf")

    #The current range and sum of our sliding window
    start = 0
    end = 0
    current_sum = 0

    #Extend the sliding window until our criteria is net
    while end<len(list):
        current_sum = current_sum + list[end]
        end = end + 1

        #Then contract the sliding window until it
        #no longer meets our condition
        while start < end and current_sum >= x:
            current_sum = current_sum - list[start]
            start = start + 1

            #Update the min_length if this is shorter
            #then the current min
            min_length = min(min_length, end-start+1)

    return min_length


print(fixed_sliding_window([1,2,3,4,5,6], 3))