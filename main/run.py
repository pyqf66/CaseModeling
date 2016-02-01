# -*- coding: utf-8 -*-
import sys
sys.path.append("../")

from PyQt5 import QtWidgets

from main.CaseModel import Ui_Form


class Run(QtWidgets.QWidget):
    def __init__(self):
        super(Run, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Run()
    window.show()
    sys.exit(app.exec_())
