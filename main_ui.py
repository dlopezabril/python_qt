from PyQt5 import QtWidgets, uic

Form, Window = uic.loadUiType("dialog.ui")

app = QtWidgets.QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()
