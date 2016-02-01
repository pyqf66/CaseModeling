# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaseModel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from util.logger import logger
from PyQt5 import QtCore
from PyQt5 import QtSql
from PyQt5 import QtWidgets

from util.OutputWithTemplate import OutputWithTemplate
import sys
sys.path.append("../")


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(666, 527)
        # toplevel
        self.label_toplevel = QtWidgets.QLabel(Form)
        self.label_toplevel.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label_toplevel.setObjectName("label_toplevel")
        self.comboBox_toplevel = QtWidgets.QComboBox(Form)
        self.comboBox_toplevel.setGeometry(QtCore.QRect(110, 40, 80, 22))
        self.comboBox_toplevel.setObjectName("comboBox_toplevel")
        self.comboBox_handle()
        self.comboBox_toplevel_current_data = self.comboBox_toplevel.currentText()
        # sublevel
        self.label_sublevel = QtWidgets.QLabel(Form)
        self.label_sublevel.setGeometry(QtCore.QRect(40, 150, 54, 12))
        self.label_sublevel.setObjectName("label_sublevel")
        self.listWidget_sublevel = QtWidgets.QListWidget(Form)
        self.listWidget_sublevel.setGeometry(QtCore.QRect(110, 70, 201, 191))
        self.listWidget_sublevel.setObjectName("listWidget_sublevel")
        # 默认选中第一个
        self.listWidget_sublevel_handle(self.comboBox_toplevel_current_data)
        # thirdlevel
        self.label_thirdlevel = QtWidgets.QLabel(Form)
        self.label_thirdlevel.setGeometry(QtCore.QRect(320, 150, 31, 16))
        self.label_thirdlevel.setObjectName("label_thirdlevel")
        self.listWidget_thirdlevel = QtWidgets.QListWidget(Form)
        self.listWidget_thirdlevel.setGeometry(QtCore.QRect(350, 71, 201, 191))
        # 设定listWidget为可多选
        self.listWidget_thirdlevel.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_thirdlevel.setObjectName("listWidget_thirdlevel")
        self.listWidget_thirdlevel_handle()
        # casemodel
        self.label_caseModel = QtWidgets.QLabel(Form)
        self.label_caseModel.setGeometry(QtCore.QRect(40, 390, 54, 12))
        self.label_caseModel.setObjectName("label_caseModel")
        self.listWidget_caseModel = QtWidgets.QListWidget(Form)
        self.listWidget_caseModel.setGeometry(QtCore.QRect(110, 300, 261, 192))
        self.listWidget_caseModel.setObjectName("listWidget_caseModel")
        self.listWidget_casemodel_handle()
        # button
        self.pushButton_deleteSelection = QtWidgets.QPushButton(Form)
        self.pushButton_deleteSelection.setGeometry(QtCore.QRect(380, 470, 75, 23))
        self.pushButton_deleteSelection.setObjectName("pushButton_deleteSelection")
        self.pushButton_toExcel = QtWidgets.QPushButton(Form)
        self.pushButton_toExcel.setGeometry(QtCore.QRect(560, 430, 75, 23))
        self.pushButton_toExcel.setObjectName("pushButton_toExcel")
        self.pushButton_resetAll = QtWidgets.QPushButton(Form)
        self.pushButton_resetAll.setGeometry(QtCore.QRect(560, 470, 75, 23))
        self.pushButton_resetAll.setObjectName("pushButton_resetAll")
        self.pushButton_addToCaseModel = QtWidgets.QPushButton(Form)
        self.pushButton_addToCaseModel.setGeometry(QtCore.QRect(560, 240, 75, 23))
        self.pushButton_addToCaseModel.setObjectName("pushButton_addToCaseModel")
        self.retranslateUi(Form)
        # 下拉框变更事件
        self.comboBox_toplevel.currentTextChanged.connect(self.listWidget_sublevel_handle)
        # 次层元素选择与选项联动事件
        self.listWidget_sublevel.itemSelectionChanged.connect(self.listWidget_thirdlevel_handle)
        # 重新设定按钮事件
        self.pushButton_resetAll.clicked.connect(self.clear_all)
        self.pushButton_addToCaseModel.clicked.connect(self.add_to_casemodel)
        self.pushButton_deleteSelection.clicked.connect(self.delete_selection)
        self.pushButton_toExcel.clicked.connect(self.to_excel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_deleteSelection.setText(_translate("Form", "删除选定"))
        self.label_caseModel.setText(_translate("Form", "已设定项"))
        self.label_thirdlevel.setText(_translate("Form", "选项"))
        self.label_sublevel.setText(_translate("Form", "次层元素"))
        self.pushButton_toExcel.setText(_translate("Form", "导出excel"))
        self.label_toplevel.setText(_translate("Form", "顶层元素"))
        self.pushButton_resetAll.setText(_translate("Form", "重新设定"))
        self.pushButton_addToCaseModel.setText(_translate("Form", "添加"))

    # 下拉框加载数据
    def comboBox_handle(self):
        comboBox_data = DBManager().query("toplevel", "toplevel_element")
        for i in range(len(comboBox_data)):
            self.comboBox_toplevel.addItem(comboBox_data[i])

    def listWidget_sublevel_handle(self, comboBox_current_data):
        self.listWidget_sublevel.clear()
        condition_List = list()
        condition_List.append("toplevel_element='" + comboBox_current_data + "'")
        toplevel_id = DBManager().query("toplevel", "toplevel_id", condition_List)
        condition_List.clear()
        condition_List.append("toplevel_id=" + toplevel_id[0])
        sublevel_element = DBManager().query("sublevel", "sublevel_element", condition_List)
        for i in sublevel_element:
            self.listWidget_sublevel.addItem(i)
        self.listWidget_sublevel.setCurrentRow(0)

    def listWidget_thirdlevel_handle(self):
        # 获取列表中选中的值
        self.listWidget_thirdlevel.clear()
        thirdlevel_widget = self.listWidget_sublevel.currentItem()
        row_data = thirdlevel_widget.text()
        condition_List = list()
        condition_List.append("sublevel_element='" + row_data + "'")
        sublevel_id = DBManager().query("sublevel", "sublevel_id", condition_List)
        condition_List.clear()
        condition_List.append("sublevel_id=" + sublevel_id[0])
        sublevel_element = DBManager().query("thirdlevel", "thirdlevel_element", condition_List)
        for i in sublevel_element:
            self.listWidget_thirdlevel.addItem(i)

    def listWidget_casemodel_handle(self):
        toplevel_element_list = DBManager().query("casemodel", "toplevel_element")
        sublevel_element_list = DBManager().query("casemodel", "sublevel_element")
        thirdlevel_element_list = DBManager().query("casemodel", "thirdlevel_element")
        casemodel_list = list()
        for j in range(len(toplevel_element_list)):
            casemodel_list.append(
                toplevel_element_list[j] + "-" + sublevel_element_list[j] + ":" + thirdlevel_element_list[j])
        for k in casemodel_list:
            self.listWidget_caseModel.addItem(k)

    def add_to_casemodel(self):
        self.listWidget_caseModel.clear()
        items = self.listWidget_thirdlevel.selectedItems()
        condition_List = list()
        for i in items:
            data_dict = dict()
            condition_List.append("thirdlevel_element='" + i.text() + "'")
            data_dict["thirdlevel_element"] = i.text()
            data_dict["thirdlevel_id"] = DBManager().query("thirdlevel", "thirdlevel_id", condition_List)[0]
            sublevel_id = DBManager().query("thirdlevel", "sublevel_id", condition_List)[0]
            data_dict["sublevel_id"] = sublevel_id
            condition_List.clear()
            condition_List.append("sublevel_id='" + sublevel_id + "'")
            data_dict["sublevel_element"] = DBManager().query("sublevel", "sublevel_element", condition_List)[0]
            toplevel_id = DBManager().query("sublevel", "toplevel_id", condition_List)[0]
            data_dict["toplevel_id"] = toplevel_id
            condition_List.clear()
            condition_List.append("toplevel_id='" + toplevel_id + "'")
            data_dict["toplevel_element"] = DBManager().query("toplevel", "toplevel_element", condition_List)[0]
            DBManager().insert_data("casemodel", data_dict)
        self.listWidget_casemodel_handle()

    def clear_all(self):
        listWidget_count = self.listWidget_caseModel.count()
        while (listWidget_count != 0):
            DBManager().clear_all("casemodel", 0)
            listWidget_count = listWidget_count - 1
        self.listWidget_caseModel.clear()

    def delete_selection(self):
        try:
            delete_data = self.listWidget_caseModel.currentItem().text()
            thirdlevel_data = "thirdlevel_element='" + delete_data.split(":")[1] + "'"
            DBManager().delete("casemodel", thirdlevel_data)
            self.listWidget_caseModel.clear()
            self.listWidget_casemodel_handle()
        except:
            logger.exception("发现错误：")

    def to_excel(self):
        try:
            TEMPLATE_FILE="../templates/测试建模模板.xlsx"
            SHEET_COUNT=4
            toplevel_id=DBManager().query("casemodel","toplevel_id")
            sublevel_id=DBManager().query("casemodel","sublevel_id")
            thirdlevel_element=DBManager().query("casemodel","thirdlevel_element")
            data_list=list()
            data_list.append(toplevel_id)
            data_list.append(sublevel_id)
            data_list.append(thirdlevel_element)
            logger.debug(data_list)
            OutputWithTemplate().output_with_excel(TEMPLATE_FILE,SHEET_COUNT,data_list)
        except:
            logger.exception("发现错误:")


class DBManager(object):
    def __init__(self):
        # 选择数据库类型，这里为sqlite3数据库
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        # 创建数据库test0.db,如果存在则打开，否则创建该数据库
        self.db.setDatabaseName("casemodel")
        # 打开数据库
        self.db.open()

    # 查询数据
    def query(self, table, value, condition_list=None):
        # 查询，其中condition是个list
        self.query = QtSql.QSqlTableModel()
        self.query.setTable(table)
        if condition_list is not None:
            for i in condition_list:
                self.query.setFilter(i)
        self.query.select()
        result_list = list()
        row_count = self.query.rowCount()
        for i in range(row_count):
            result_list.append(self.query.record(i).value(value))
        return result_list

    # 插入数据
    def insert_data(self, table, data_dict):
        self.insert = QtSql.QSqlTableModel()
        self.insert.setTable(table)
        self.insert.select()
        row_count = self.insert.rowCount()
        model = self.insert.record()
        for i in data_dict:
            model.setValue(i, data_dict[i])
        self.insert.insertRecord(row_count, model)
        self.insert.submitAll()

    # 删除所有数据
    def clear_all(self, table, start_row):
        self.clearer = QtSql.QSqlTableModel()
        self.clearer.setTable(table)
        # 查询出数据后才能成功执行后续的命令
        self.clearer.select()
        try:
            self.clearer.removeRows(0, 1)
            self.clearer.submitAll()
        except:
            logger.exception("发现错误")

    # 删除数据
    def delete(self, table, data):
        self.delete = QtSql.QSqlTableModel()
        self.delete.setTable(table)
        self.delete.setFilter(data)
        self.delete.select()
        self.delete.removeRows(0, 1)
        self.delete.submitAll()
