name = "         jai    paswan     "
dots = "..........."

#lstrip method

print(name+dots)
print(name.lstrip() + dots)
print(name.rstrip()+ dots)
print(name.strip()+ dots)
print(name.replace(" ","") + dots)

# replace() method 
#find method

para = "She is beautiful and she is a good dancer"
print(para.replace(" ","_"))

print(para.replace("is","was" , 2))  #2 is replace hoga


#find method

print(para.find("is",2))
is_pos1 = para.find("is")
is_pos2 = para.find("is", is_pos1+1)


#centre method

name = "jai"
#**jai**
print(name.center(7,"*"))

name= input("Enter your name:")
print(name.center(len(name) + 8, "*"))





