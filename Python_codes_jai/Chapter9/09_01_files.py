# use open function to read the content ofa file
#   ("file name")↓      ↓("mode")
f = open("sample.txt", "r")
# f = open("sample.txt")  #by default the mode is "r"

data = f.read()
# data = f.read(5) #reads first 5 characters from the file
print(data)
f.close()