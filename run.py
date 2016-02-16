# -*- coding: utf-8 -*-
import sys
sys.path.append("../")

from PyQt5 import QtWidgets

from main.CaseModel import Ui_Form_Main
from main.SublevelHelp import Ui_Form_Help
from main.EditModule import Ui_Form_EditModule
from util.logger import logger


class Run(QtWidgets.QWidget):
    def __init__(self):
        super(Run, self).__init__()
        self.ui = Ui_Form_Main()
        self.ui.setupUi(self)
        self.ui.pushButton_sublevel_help.clicked.connect(self.sublevel_help)
        self.ui.pushButton_edit.clicked.connect(self.edit_module)

    # 打开次层元素帮助方法
    def sublevel_help(self):
        try:
            self.help_widget = QtWidgets.QWidget()
            self.window_help = Ui_Form_Help()
            self.window_help.setupUi(self.help_widget)
        except:
            logger.exception("发现错误:")

    def edit_module(self):
        try:
            self.edit_widget = QtWidgets.QWidget()
            self.ui_edit_module = Ui_Form_EditModule()
            self.ui_edit_module.setupUi(self.edit_widget)
            # 添加模块
            self.ui_edit_module.pushButton_add_module.clicked.connect(self.add_modules)
            self.ui_edit_module.pushButton_delete_module.clicked.connect(self.del_modules)
        except:
            logger.exception("加载编辑页面错误：")

    def add_modules(self):
        self.ui_edit_module.add_to_module()
        self.ui.comboBox_module.clear()
        self.ui.comboBox_module_handle()

    def del_modules(self):
        self.ui_edit_module.delete_module()
        self.ui.comboBox_module.clear()
        self.ui.comboBox_module_handle()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Run()
    window.show()
    sys.exit(app.exec_())

