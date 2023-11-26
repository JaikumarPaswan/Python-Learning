f = open('another.txt', 'w')
f.write("I am writting")
f.write("two time using .write will add the given content")
f.close()

g = open('another.txt', 'a')
g.write("this will be added to the last")
g.close()  #Will append the content every time after running program,If and Only if Append mode is open in the program


i = open('another.txt', 'r')
data = i.read()
print(data)
i.close()