# def fun(n):
#     return n*(n+1)/2

# print(fun(3))

def sum(n):
    sum=0
    for i in range(1, n+1):
        sum = sum + i
    
    return sum

print(sum(3))



def salary(day): #when every day your salary is doubled
    pay = 1
    for i in range(0,day):
        pay = pay * 2
    
    return pay

print(salary(30))

