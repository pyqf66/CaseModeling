# -*- coding: utf-8 -*-
import sys
sys.path.append("../")

from PyQt5 import QtWidgets

from main.CaseModel import Ui_Form_Main
from main.SublevelHelp import Ui_Form_Help
from util.logger import logger


class Run(QtWidgets.QWidget):
    def __init__(self):
        super(Run, self).__init__()
        self.ui = Ui_Form_Main()
        self.ui.setupUi(self)
        self.ui.pushButton_sublevel_help.clicked.connect(self.sublevel_help)

    # 打开次层元素帮助方法
    def sublevel_help(self):
        try:
            self.help_widget = QtWidgets.QWidget()
            self.window_help = Ui_Form_Help()
            self.window_help.setupUi(self.help_widget)
        except:
            logger.exception("发现错误:")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Run()
    window.show()
    sys.exit(app.exec_())

