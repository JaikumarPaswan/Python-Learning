#Python provides the assert statement to check if a given logical 
# expression is true or false. Program execution proceeds only 
# if the expression is true and raises the AssertionError 
# when it is false.

# num = 10
# assert num>10   #This gives AssertionError


try:
    num=int(input("Enter the number "))
    assert num%2==0
    print("This number is even")
except AssertionError:                    # the AssertionError in the except block is used to catch and handle the specific error raised by the assert, if any different kind of error is raised like valueError or indexError then it will return an error, If we don't write AssertionError, it will still work same as our written code can provide 
    print("Please enter even number")

