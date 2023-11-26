class RailwayForm:            #class (template/blueprint)
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

jaisApplication = RailwayForm()   #object
jaisApplication.name = "Jai"      #method
jaisApplication.train = "Rajdhani express"
jaisApplication.printData()