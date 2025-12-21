class RailwayForm:
    formType = "RailwayForm"
    def printData(self):       #method/function    #In Python, the 'self' parameter is a reference to the current instance of a class. It is used within class methods to access and modify the attributes and methods specific to that particular object, rather than the class as a whole. 
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

jaisApplication = RailwayForm()    #instance of the 'RailwayForm' class and assigns it to the variable 'jaisApplication'.
jaisApplication.name = "jai"
jaisApplication.train = "Rajdhani Express"
jaisApplication.printData()     