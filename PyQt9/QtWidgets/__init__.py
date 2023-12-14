# class defination
class QApplication():
    #1. Property
    fullname = ' '
    
    #2. Constructor
    def __init__(self,name):
        self.fullname = name
    
    #3. Method/Function
    def exec (self):
        print(f"Exec {self.fullname}")
    pass
    
# class defination
class QWidget():
    #1. Property
    #2. Constructor
    #3. Method/Function
    def show(self):
        print("show Method")
    pass
