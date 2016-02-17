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
        # 下拉框变更事件
        self.ui.comboBox_module.currentTextChanged.connect(self.ui.comboBox_module_change_handle)
        # 下拉框变更事件
        self.ui.comboBox_toplevel.currentTextChanged.connect(self.ui.listWidget_sublevel_handle)
        # 次层元素选择与选项联动事件
        self.ui.listWidget_sublevel.itemSelectionChanged.connect(self.ui.listWidget_thirdlevel_handle)
        # 重新设定按钮事件
        self.ui.pushButton_addThirdlevel.clicked.connect(self.ui.add_thirdlevel)
        self.ui.pushButton_resetAll.clicked.connect(self.ui.clear_all)
        self.ui.pushButton_deleteThirdlevel.clicked.connect(self.ui.delete_thirdlevel)
        self.ui.pushButton_addToCaseModel.clicked.connect(self.ui.add_to_casemodel)
        self.ui.pushButton_deleteSelection.clicked.connect(self.ui.delete_selection)
        self.ui.pushButton_toExcel.clicked.connect(self.ui.to_excel)

    # 打开次层元素帮助方法
    def sublevel_help(self):
        try:
            self.help_widget = QtWidgets.QWidget()
            self.window_help = Ui_Form_Help()
            self.window_help.setupUi(self.help_widget)
        except:
            logger.exception("发现错误:")

    #模块编辑
    def edit_module(self):
        try:
            self.edit_widget = QtWidgets.QWidget()
            self.ui_edit_module = Ui_Form_EditModule()
            self.ui_edit_module.setupUi(self.edit_widget)
            # 添加模块
            self.ui_edit_module.pushButton_add_module.clicked.connect(self.add_modules)
            #删除模块
            self.ui_edit_module.pushButton_delete_module.clicked.connect(self.del_modules)
        except:
            logger.exception("加载编辑页面错误：")

    #添加模块函数
    def add_modules(self):
        #添加模块数据
        self.ui_edit_module.add_to_module()
        #清空主页面模块数据
        self.ui.comboBox_module.clear()
        #查询主页面模块数据并显示
        self.ui.comboBox_module_handle()

    #删除模块函数
    def del_modules(self):
        #删除模块数据
        self.ui_edit_module.delete_module()
        #清空主页面模块数据
        self.ui.comboBox_module.clear()
        #查询主页面模块数据并显示
        self.ui.comboBox_module_handle()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Run()
    window.show()
    sys.exit(app.exec_())

