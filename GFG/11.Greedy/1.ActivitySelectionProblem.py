#Q)Maximum no. of activities that can happen on single tasking machine.
#First element of pair is start time, second element of pair is end time
#We are given only 1 one machine which can do 1 task at a time, 
#find the count of maximum number of tasks can be done by the machine

#We sort the arr according to end time and then check for overlaps, we set res=1
#at start because we always consider first pair to be part of solution count.
 
def maxActivities(arr):
    n=len(arr)

    arr.sort(key=lambda x:x[1])

    prev=0
    res=1

    for curr in range(1, n):
        if arr[curr][0] >= arr[prev][1]:
            res += 1
            prev=curr
    return res


arr = [(12,25), (10,20), (20,30)]

print(maxActivities(arr))
