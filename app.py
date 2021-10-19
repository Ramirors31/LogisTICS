import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('login.ui',self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main= VentanaPrincipal()
    main.show()