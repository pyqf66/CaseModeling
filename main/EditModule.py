# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditModule.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main.DBManager import DBManager
from  util.logger import logger

class Ui_Form_EditModule(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 306)
        self.listWidget_module = QtWidgets.QListWidget(Form)
        self.listWidget_module.setGeometry(QtCore.QRect(10, 80, 201, 201))
        self.listWidget_module.setObjectName("listWidget_module")
        self.pushButton_add_module = QtWidgets.QPushButton(Form)
        self.pushButton_add_module.setGeometry(QtCore.QRect(240, 20, 81, 31))
        self.pushButton_add_module.setObjectName("pushButton_add_module")
        self.pushButton_delete_module = QtWidgets.QPushButton(Form)
        self.pushButton_delete_module.setGeometry(QtCore.QRect(240, 250, 81, 31))
        self.pushButton_delete_module.setObjectName("pushButton_delete_module")
        self.textEdit_module = QtWidgets.QTextEdit(Form)
        self.textEdit_module.setGeometry(QtCore.QRect(10, 20, 201, 31))
        self.textEdit_module.setObjectName("textEdit_module")
        # 默认选中第一个
        self.listWidget_module_handle()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "模块编辑"))
        self.pushButton_add_module.setText(_translate("Form", "添加"))
        self.pushButton_delete_module.setText(_translate("Form", "删除"))

    # 模块加载数据方法
    def listWidget_module_handle(self):

        try:
            self.listWidget_module.clear()
            module_element = DBManager().query("modules", "module")
            for i in module_element:
                self.listWidget_module.addItem(i)
                logger.debug("加载数据成功："+i)
            self.listWidget_module.setCurrentRow(0)
        except:
            logger.exception("查询模块数据错误：")

    # 添加模块数据方法
    def add_to_module(self):
        modules = self.textEdit_module.toPlainText()
        module_element = DBManager().query("modules", "module")
        if ":" in modules or "：" in modules or "-" in modules:
                msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "错误输入提示", "不允许输入冒号或横线！")
                msg_box.exec_()
                self.textEdit_module.clear()
        elif(modules in module_element):
            msg_box_repetition = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "错误输入提示", "模块名称重复！")
            msg_box_repetition.exec_()
            self.textEdit_module.clear()
        else:
            module_dict = dict()
            module_id = max(list(DBManager().query("modules", "module_id")))
            logger.debug("模块当前最大id为："+module_id)
            try:
                module_dict["module"] = modules
                module_dict["module_id"] = int(module_id)+1
                DBManager().insert_data("modules",module_dict)
                logger.debug("插入模块数据成功：modules ="+modules + ",module_id ="+ str((int(module_id)+1)))
                self.listWidget_module_handle()
                self.textEdit_module.clear()
            except:
                logger.exception("模块数据插入错误")

    #删除模块方法
    def delete_module(self):
        try:
            condition_List_module = list()
            condition_List_module_id = list()
            delete_modules = self.listWidget_module.selectedItems()
            for i in delete_modules:
                condition_List_module.clear()
                condition_List_module_id.clear()
                condition_List_module.append("module='" + i.text() + "'")
                module_id = DBManager().query("modules", "module_id", condition_List_module)[0]
                DBManager().delete("modules",condition_List_module)
                logger.debug("modules表，删除数据成功："+i.text())
                condition_List_module_id.append("module_id='" + module_id + "'")
                DBManager().delete("casemodel",condition_List_module_id)
                logger.debug("casemodel表，删除数据成功,删除id为："+ module_id)

                DBManager().delete("thirdlevel",condition_List_module_id)
                logger.debug("thirdlevel表，删除数据成功,删除id为："+ module_id)
            self.listWidget_module_handle()
        except:
            logger.exception("删除数据错误:")