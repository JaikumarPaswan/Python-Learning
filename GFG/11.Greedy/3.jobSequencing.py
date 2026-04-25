#The job sequencing problem aims to maximize total profit by 
# scheduling jobs with specific deadlines and profits. Each 
# job takes 1 unit of time, and only one job can be performed 
# at a time. The optimal approach is a greedy algorithm: 
# sort jobs by descending profit and assign each to the latest 
# available time slot before its deadline.

#we made array of boolean False value of size equal to total num of jobs,
#Then we sorted according to profit and started assigning 
# slots from end whose profit is maximum. 't' is total num of jobs.

def jobScheduling(arr, t):
    n=len(arr)
    arr.sort(key=lambda x:x[1], reverse=True)
    result = [False]*t

    res=0

    for i in range(n):
        for j in range(min(t-1,arr[i][0]-1),-1,-1):
            if result[j]==False:
                result[j]=True
                res+=arr[i][1]
                break
    return res

arr=[(4,50),(1,5),(1,20),(5,10),(5,80)]
t=5

print(jobScheduling(arr, t))