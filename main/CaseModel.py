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
from main.SublevelHelp import Ui_Form_Help

from util.OutputWithTemplate import OutputWithTemplate
import sys

sys.path.append("../")


class Ui_Form_Main(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(679, 589)
        # module
        self.label_module = QtWidgets.QLabel(Form)
        self.label_module.setGeometry(QtCore.QRect(10, 29, 61, 20))
        self.label_module.setObjectName("label_module")
        self.comboBox_module = QtWidgets.QComboBox(Form)
        self.comboBox_module.setGeometry(QtCore.QRect(90, 20, 91, 31))
        self.comboBox_module.setObjectName("comboBox_module")
        self.comboBox_module_handle()
        self.comboBox_module_current_data = self.comboBox_module.currentText()
        # toplevel
        self.label_toplevel = QtWidgets.QLabel(Form)
        self.label_toplevel.setGeometry(QtCore.QRect(10, 89, 61, 20))
        self.label_toplevel.setObjectName("label_toplevel")
        self.comboBox_toplevel = QtWidgets.QComboBox(Form)
        self.comboBox_toplevel.setGeometry(QtCore.QRect(90, 80, 91, 31))
        self.comboBox_toplevel.setObjectName("comboBox_toplevel")
        self.comboBox_toplevel_handle()
        self.comboBox_toplevel_current_data = self.comboBox_toplevel.currentText()
        # sublevel
        self.label_sublevel = QtWidgets.QLabel(Form)
        self.label_sublevel.setGeometry(QtCore.QRect(13, 210, 61, 20))
        self.label_sublevel.setObjectName("label_sublevel")
        self.listWidget_sublevel = QtWidgets.QListWidget(Form)
        self.listWidget_sublevel.setGeometry(QtCore.QRect(90, 138, 201, 191))
        self.listWidget_sublevel.setObjectName("listWidget_sublevel")
        # 默认选中第一个
        self.listWidget_sublevel_handle(self.comboBox_toplevel_current_data)
        # thirdlevel
        self.label_thirdlevel = QtWidgets.QLabel(Form)
        self.label_thirdlevel.setGeometry(QtCore.QRect(300, 218, 41, 20))
        self.label_thirdlevel.setObjectName("label_thirdlevel")
        self.listWidget_thirdlevel = QtWidgets.QListWidget(Form)
        self.listWidget_thirdlevel.setGeometry(QtCore.QRect(350, 139, 201, 191))
        # 设定listWidget为可多选
        self.listWidget_thirdlevel.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_thirdlevel.setObjectName("listWidget_thirdlevel")
        self.listWidget_thirdlevel_handle()
        # casemodel
        self.label_caseModel = QtWidgets.QLabel(Form)
        self.label_caseModel.setGeometry(QtCore.QRect(13, 450, 61, 20))
        self.label_caseModel.setObjectName("label_caseModel")
        self.listWidget_caseModel = QtWidgets.QListWidget(Form)
        self.listWidget_caseModel.setGeometry(QtCore.QRect(90, 368, 261, 192))
        self.listWidget_caseModel.setObjectName("listWidget_caseModel")
        self.listWidget_casemodel_handle()
        # button
        self.pushButton_deleteSelection = QtWidgets.QPushButton(Form)
        self.pushButton_deleteSelection.setGeometry(QtCore.QRect(380, 530, 81, 31))
        self.pushButton_deleteSelection.setObjectName("pushButton_deleteSelection")
        self.pushButton_toExcel = QtWidgets.QPushButton(Form)
        self.pushButton_toExcel.setGeometry(QtCore.QRect(560, 488, 101, 31))
        self.pushButton_toExcel.setObjectName("pushButton_toExcel")
        self.pushButton_resetAll = QtWidgets.QPushButton(Form)
        self.pushButton_resetAll.setGeometry(QtCore.QRect(560, 528, 101, 31))
        self.pushButton_resetAll.setObjectName("pushButton_resetAll")
        self.pushButton_addToCaseModel = QtWidgets.QPushButton(Form)
        self.pushButton_addToCaseModel.setGeometry(QtCore.QRect(560, 300, 81, 31))
        self.pushButton_addToCaseModel.setObjectName("pushButton_addToCaseModel")
        self.pushButton_sublevel_help = QtWidgets.QPushButton(Form)
        self.pushButton_sublevel_help.setGeometry(QtCore.QRect(560, 448, 101, 31))
        self.pushButton_sublevel_help.setObjectName("pushButton_sublevel_help")
        self.retranslateUi(Form)
        # 下拉框变更事件
        self.comboBox_module.currentTextChanged.connect(self.comboBox_module_change_handle)
        # 下拉框变更事件
        self.comboBox_toplevel.currentTextChanged.connect(self.listWidget_sublevel_handle)
        # 次层元素选择与选项联动事件
        self.listWidget_sublevel.itemSelectionChanged.connect(self.listWidget_thirdlevel_handle)
        # 重新设定按钮事件
        self.pushButton_resetAll.clicked.connect(self.clear_all)
        self.pushButton_addToCaseModel.clicked.connect(self.add_to_casemodel)
        self.pushButton_deleteSelection.clicked.connect(self.delete_selection)
        self.pushButton_toExcel.clicked.connect(self.to_excel)
        self.pushButton_sublevel_help.clicked.connect(self.sublevel_help)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "测试建模工具"))
        self.pushButton_deleteSelection.setText(_translate("Form", "删除选定"))
        self.label_caseModel.setText(_translate("Form", "已设定项"))
        self.label_thirdlevel.setText(_translate("Form", "选项"))
        self.label_sublevel.setText(_translate("Form", "次层元素"))
        self.pushButton_toExcel.setText(_translate("Form", "导出excel"))
        self.label_toplevel.setText(_translate("Form", "顶层元素"))
        self.pushButton_resetAll.setText(_translate("Form", "重新设定"))
        self.pushButton_addToCaseModel.setText(_translate("Form", "添加"))
        self.pushButton_sublevel_help.setText(_translate("Form", "次层元素说明"))
        self.label_module.setText(_translate("Form", "模块"))

    # 顶层元素下拉框加载数据方法
    def comboBox_module_handle(self):
        comboBox_data = DBManager().query("modules", "module")
        for i in range(len(comboBox_data)):
            self.comboBox_module.addItem(comboBox_data[i])

    # 顶层元素下拉框加载数据方法
    def comboBox_module_change_handle(self):
        self.listWidget_thirdlevel_handle()
        self.listWidget_casemodel_handle()

    # 顶层元素下拉框加载数据方法
    def comboBox_toplevel_handle(self):
        comboBox_data = DBManager().query("toplevel", "toplevel_element")
        for i in range(len(comboBox_data)):
            self.comboBox_toplevel.addItem(comboBox_data[i])

    # 次层元素加载数据方法
    def listWidget_sublevel_handle(self, comboBox_current_data):
        try:
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
        except:
            logger.exception("发现错误：")

    # 三层元素加载数据方法
    def listWidget_thirdlevel_handle(self):
        try:
            # 获取列表中选中的值
            self.listWidget_thirdlevel.clear()
            condition_List = list()
            module = self.comboBox_module.currentText()
            condition_List.clear()
            condition_List.append("module='" + module + "'")
            module_id = DBManager().query("modules", "module_id", condition_List)[0]
            thirdlevel_widget = self.listWidget_sublevel.currentItem()
            row_data = thirdlevel_widget.text()
            condition_List.clear()
            condition_List.append("sublevel_element='" + row_data + "'")
            sublevel_id = DBManager().query("sublevel", "sublevel_id", condition_List)
            condition_List.clear()
            condition_List.append("sublevel_id='" + sublevel_id[0] + "'")
            condition_List.append("module_id='" + str(module_id) + "'")
            sublevel_element = DBManager().query("thirdlevel", "thirdlevel_element", condition_List)
            for i in sublevel_element:
                self.listWidget_thirdlevel.addItem(i)
        except:
            logger.exception("发现错误：")

    # 生成的建模数据加载方法
    def listWidget_casemodel_handle(self):
        try:
            self.listWidget_caseModel.clear()
            condition_List = list()
            module = self.comboBox_module.currentText()
            condition_List.clear()
            condition_List.append("module='" + module + "'")
            module_id = DBManager().query("modules", "module_id", condition_List)[0]
            condition_List.clear()
            condition_List.append("module_id='" + str(module_id) + "'")
            logger.debug("=====================================================================")
            logger.debug(condition_List)
            toplevel_element_list = DBManager().query("casemodel", "toplevel_element", condition_List)
            logger.debug(toplevel_element_list)
            sublevel_element_list = DBManager().query("casemodel", "sublevel_element", condition_List)
            thirdlevel_element_list = DBManager().query("casemodel", "thirdlevel_element", condition_List)
            casemodel_list = list()
            for j in range(len(toplevel_element_list)):
                casemodel_list.append(
                    toplevel_element_list[j] + "-" + sublevel_element_list[j] + ":" + thirdlevel_element_list[j])
            logger.debug(casemodel_list)
            for k in casemodel_list:
                self.listWidget_caseModel.addItem(k)
        except:
            logger.exception("发现错误：")

    # 根据操作生成模型数据方法
    def add_to_casemodel(self):
        try:
            module = self.comboBox_module.currentText()
            condition_List = list()
            condition_List.clear()
            condition_List.append("module='" + module + "'")
            module_id = DBManager().query("modules", "module_id", condition_List)[0]
            toplevel_element = self.comboBox_toplevel.currentText()
            items_sublevel = self.listWidget_sublevel.selectedItems()
            items_thirdlevel = self.listWidget_thirdlevel.selectedItems()
            for i_sublevel in items_sublevel:
                sublevel_element = i_sublevel.text()
                condition_List.clear()
                condition_List.append("sublevel_element='" + i_sublevel.text() + "'")
                sublevel_id = DBManager().query("sublevel", "sublevel_id", condition_List)[0]

            # 使用字典记录即将添加的值，并调用公用方法添加数据
            for i_thirdlevel in items_thirdlevel:
                data_dict = dict()
                condition_List.clear()
                condition_List.append("sublevel_id='" + sublevel_id + "'")
                logger.debug(sublevel_id)
                condition_List.append("module_id='" + str(module_id) + "'")
                condition_List.append("thirdlevel_element='" + i_thirdlevel.text() + "'")
                logger.debug(condition_List)
                thirdlevel_id = DBManager().query("thirdlevel", "thirdlevel_id", condition_List)[0]
                condition_List.clear()
                condition_List.append("module_id='" + str(module_id) + "'")
                condition_List.append("thirdlevel_element='" + i_thirdlevel.text() + "'")
                casemodel_thirdlevel_id = DBManager().query("casemodel", "thirdlevel_id", condition_List)
                if thirdlevel_id not in casemodel_thirdlevel_id:
                    data_dict["thirdlevel_id"] = thirdlevel_id
                    thirdlevel_element = i_thirdlevel.text()
                    data_dict["thirdlevel_element"] = thirdlevel_element
                    data_dict["sublevel_id"] = sublevel_id
                    data_dict["sublevel_element"] = sublevel_element
                    condition_List.clear()
                    condition_List.append("toplevel_element='" + toplevel_element + "'")
                    toplevel_id = DBManager().query("toplevel", "toplevel_id", condition_List)[0]
                    data_dict["toplevel_id"] = toplevel_id
                    data_dict["toplevel_element"] = toplevel_element
                    data_dict["module_id"] = module_id
                    logger.debug(data_dict)
                    DBManager().insert_data("casemodel", data_dict)
            self.listWidget_casemodel_handle()
        except:
            logger.exception("发现错误：")

    # 清除所有数据方法
    def clear_all(self):
        try:
            listWidget_count = self.listWidget_caseModel.count()
            module = self.comboBox_module.currentText()
            condition_list = list()
            condition_list.clear()
            condition_list.append("module='"+module+"'")
            module_id=DBManager().query("modules","module_id",condition_list)[0]
            condition_list.clear()
            condition_list.append("module_id='" + module_id + "'")
            while (listWidget_count != 0):
                DBManager().delete("casemodel", condition_list)
                listWidget_count = listWidget_count - 1
            self.listWidget_caseModel.clear()
        except:
            logger.exception("发现错误：")

    # 删除所选项方法
    def delete_selection(self):
        try:
            condition_list=list()
            module=self.comboBox_module.currentText()
            condition_list.clear()
            condition_list.append("module='"+module+"'")
            module_id=DBManager().query("modules","module_id",condition_list)[0]
            condition_list.clear()
            delete_data = self.listWidget_caseModel.currentItem().text()
            thirdlevel_data = "thirdlevel_element='" + delete_data.split(":")[1] + "'"
            condition_list.append(thirdlevel_data)
            condition_list.append("module_id='"+str(module_id)+"'")
            logger.debug(condition_list)
            DBManager().delete("casemodel", condition_list)
            self.listWidget_casemodel_handle()
        except:
            logger.exception("发现错误：")

    # 生成excel方法
    def to_excel(self):
        try:
            # toplevel_id在sublevel表中个数索引从1开始
            toplevel_count_list = list()
            condition_list = list()
            module = self.comboBox_module.currentText()
            condition_list.clear()
            condition_list.append("module='" + module + "'")
            module_id = DBManager().query("modules", "module_id", condition_list)[0]
            logger.debug(module_id)
            logger.debug(condition_list)
            for i in range(4):
                i = i + 1
                condition_list.clear()
                condition_list.append("toplevel_id='" + str(i) + "'")
                toplevel_count_list.append(len(DBManager().query("sublevel", "sublevel_elemnt", condition_list)))
            TEMPLATE_FILE = "../templates/测试建模模板.xlsx"
            SHEET_COUNT = 4
            real_index_list = list()
            condition_list.clear()
            condition_list.append("module_id='" + str(module_id) + "'")
            toplevel_id = DBManager().query("casemodel", "toplevel_id", condition_list)
            # sublevel_id数据索引从1开始
            sublevel_id = DBManager().query("casemodel", "sublevel_id", condition_list)
            for j in sublevel_id:
                real_index = int(j)
                toplevel_count_index = 0
                # 由于sublevel_id数据索引和sublevel表中toplevel_id个数索引均从1开始
                # 故两者之差大于0时认为当前sublevel_element为下一个顶级元素的次级元素，需要做差取真实表格索引
                while ((real_index - toplevel_count_list[toplevel_count_index]) > 0):
                    real_index = real_index - toplevel_count_list[toplevel_count_index]
                    toplevel_count_index = toplevel_count_index + 1
                real_index_list.append(real_index)
            thirdlevel_element = DBManager().query("casemodel", "thirdlevel_element", condition_list)
            data_list = list()
            data_list.append(toplevel_id)
            data_list.append(real_index_list)
            data_list.append(thirdlevel_element)
            logger.debug(data_list)
            OutputWithTemplate().output_with_excel(TEMPLATE_FILE, SHEET_COUNT, data_list)
        except:
            logger.exception("发现错误:")

    # 打开次层元素帮助方法
    def sublevel_help(self):
        try:
            self.help_widget = QtWidgets.QWidget()
            self.window_help = Ui_Form_Help()
            self.window_help.setupUi(self.help_widget)
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
            condition = " and ".join(condition_list)
            self.query.setFilter(condition)
        self.query.select()
        result_list = list()
        row_count = self.query.rowCount()
        for i in range(row_count):
            result_list.append(self.query.record(i).value(value))
        return result_list

    # 插入数据，数据索引从0开始
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

    # # 删除所有数据
    # def clear_all(self, table, condition_list=None):
    #     self.clearer = QtSql.QSqlTableModel()
    #     self.clearer.setTable(table)
    #     if condition_list is not None:
    #         condition = " and ".join(condition_list)
    #         self.clearer.setFilter(condition)
    #     # 查询出数据后才能成功执行后续的命令
    #     self.clearer.select()
    #     try:
    #         self.clearer.removeRows(0, 1)
    #         self.clearer.submitAll()
    #     except:
    #         logger.exception("发现错误")

    # 删除数据
    def delete(self, table, condition_list=None):
        self.delete = QtSql.QSqlTableModel()
        self.delete.setTable(table)
        if condition_list is not None:
            condition = " and ".join(condition_list)
            self.delete.setFilter(condition)
        self.delete.select()
        self.delete.removeRows(0, 1)
        self.delete.submitAll()

