#My Code
# a = int(input("Enter marks for physics: "))
# b = int(input("Enter marks for chemistry: "))
# c = int(input("Enter marks for maths: "))

# p = (a+b+c)/300*100

# if(p>=40 and a>=33 and b>=33 and c>=33):
#     print("You are Pass")
# else:
#     print("You are Fail")

sub1 = int(input("Enter marks for physicsubject 1: "))
sub2 = int(input("Enter marks for chemistrsubject 2: "))
sub3 = int(input("Enter marks for subject 2: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33 marks in one or more subject")
elif(sub1+sub2+sub3)/3<40:
    print("You are fail due to total percentage less than 40")
else:
    print("You are passed")

