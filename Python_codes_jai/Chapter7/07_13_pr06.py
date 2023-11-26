num = int(input("Enter the number: "))

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
    print(f"{i} <-")
    print(factorial)
print(f"The value of {num} if {factorial}")    
    