base_sql = 'projects.db'

# All Data Base
project_id = 1
path = {
    'Unreal Editor': 'path',
    'Project File': 'path'
}

all_levels = {
    'Levels 01': ('path', True, True),
}

project = nametuple('Project ID', ('Path ID', 'Levels'))


from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from collections import namedtuple, OrderedDict
import os

class ModeleTableProject(QtCore.QAbstractTableModel):
    def __init__(self):
        super(ModeleTableProject, self).__init__()
        BD_Exist = os.path.exists(base_sql)

        bd = QSqlDatabase.addDatabase('QSQLITE')
        bd.setDatabaseName(base_sql)
        bd.open()

        if not BD_Exist:
            self.createDB()

        self.readDB()

    def createDB(self):
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

    def readDB(self):
        query = QSqlQuery(''' SELECT levels_id, name
                            FROM levels
                            ORDER BY levels_id ''')
        self.idByLevels = OrderedDict()
        while query.next():
            self.idByLevels[query.value(1)] = query.value(0)

        query = QSqlQuery(''' SELECT project_id, paths_id, levels_id
                            FROM projects ''')

        self.project = []
        while query.next():
            livre = Livre(*(query.value(i) for i in range(8)))
            self.project.append(livre)

    def genre(self):
        return self.idByLevels.keys()