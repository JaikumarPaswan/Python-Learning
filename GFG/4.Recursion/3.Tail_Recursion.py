#A recursive function is called Tail Recursive if the function does not 
# do any thing after the last recursive call

# def fun(n):
#     if (n==0):
#         return
#     print(n)
#     fun(n-1)

# Above is a Tail Recursive function which can be optimised by programmers
# We can [1] Replace if with while
#        [2] Change values of parameters at the end of the loop

def fun(n):
    while (n!=0):
        print(n)
        n = n-1

print(fun(4))