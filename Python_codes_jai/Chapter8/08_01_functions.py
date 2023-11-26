#            ↓ argument          
def percent(marks):
    return((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
     
    #OR_This can also be done
    #p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    #return p

marks1 = [45,78,63,22]
percentage1 = percent(marks1)
print(percentage1)

marks2 = [85,48,97,21]
percentage2 = percent(marks2)
print(percentage2)

