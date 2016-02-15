# -*- coding: utf-8 -*-
from PyQt5 import QtSql
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
