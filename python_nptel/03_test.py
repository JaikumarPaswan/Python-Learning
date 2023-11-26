# def max3bad(x,y,z):
#   maximum = 0
#   if x >= y:
#     if x >= z:
#         maximum = x
#     else: 
#         maximum = z

#   else:
#     if y>=z:
#         maximum = y
#     else:
#         maximum = z
    
#   return(maximum)

# m = max3bad(99,858,10)
# print(m)

# def min3(x,y,z):
#   if x <= y:
#     if x <= z:
#       minimum = x
#     else:
#       minimum = z
    
#   else:
#       if y<= z:
#           minimum = y
#       else:
#           minimum = z
#   return(minimum)


# m = min3(2255555,3555555555555553,45554)
# print(m)
  # Your code below this line


  # Your code above this line
 

def min3(x,y,z):
  if x <= y:
    if x <= z:
      minimum = x
    else:
      minimum = z
    
  elif(y<=z and y<=x):
    minimum = y
  else:
      minimum = z
  return(minimum)

m = min3(5,33,45554)
print(m)