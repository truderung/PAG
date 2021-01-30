import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from firstDesignerGui import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
        self.show()  


app = QApplication(sys.argv)
w = AppWindow()
w.show()
app.exec_()
app.aboutToQuit.connect(app.deleteLater)
