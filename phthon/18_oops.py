class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

jaisApplication = RailwayForm()
jaisApplication.name = "jai"
jaisApplication.train = "Rajdhani Express"
jaisApplication.printData()        