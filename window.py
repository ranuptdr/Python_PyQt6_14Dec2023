# Specific Import
from mypackage.mysubmodule import Parent,Child
from PyQt9.QtWidgets import QApplication,QWidget

#2.  create class object
co = Parent()
co.sayHello()

co = Child()
co.hi()
#2.  create class object
app = QApplication("Ranu")
app.exec()

Window = QWidget()
Window.show()
