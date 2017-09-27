from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from collections import namedtuple, OrderedDict
import os


# # All Data Base
# project_id = 1
# path = {
#     'Unreal Editor': 'path',
#     'Project File': 'path'
# }
#
# all_levels = {
#     'Levels 01': ('path', True, True),
# }
#
# project = namedtuple('Project ID', ('Path ID', 'Levels'))


class TableProgram(QtCore.QAbstractTableModel):
    base_sql = 'projects.db'

    def __init__(self):
        super(TableProgram, self).__init__()
        bd_exist = os.path.exists(self.base_sql)

        bd = QSqlDatabase.addDatabase('QSQLITE')
        bd.setDatabaseName(self.base_sql)
        bd.open()

        if not bd_exist:
            self.create_data()

        self.read_data()

    @staticmethod
    def create_data():
            QSqlQuery(''' CREATE TABLE  projects (
                            project_id  INTEGER PRIMARY KEY
                            paths_id    INTEGER
                            levels_id   INTEGER)
                            ''')

            QSqlQuery(''' CREATE TABLE paths (
                            path_id     INTERGER PRIMARY KEY
                            editor      TEXT
                            project     TEXT)
                            ''')

            QSqlQuery(''' CREATE TABLE levels (
                            levels_id   INTEGER PRIMARY KEY
                            name        TEXT
                            path        TEXT)
            ''')

            msg_def = 'Create a news base data'

            return msg_def

    def read_data(self):
        msg_func = 'Read Data from the base data'

        return msg_func

    @staticmethod
    def add_data():
        msg_func = 'Add Data inside the BD'

        return msg_func
