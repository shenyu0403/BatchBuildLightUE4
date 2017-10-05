from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import os
import sqlite3


class TableProgram(object):
    """Objects to work with the SQLite"""

    def __init__(self):
        super(TableProgram, self).__init__()
        self.base_sql = 'projects.db'
        self.bd_exist = os.path.exists(self.base_sql)

        self.bd = sqlite3.connect(self.base_sql)
        self.bd.cursor()

        if not self.bd_exist:
            self.create_data()

    def create_data(self):
        self.bd.execute('''CREATE TABLE  projects(
                id          INTEGER PRIMARY KEY,
                project_id  INT,
                paths_id    INT)''')

        self.bd.execute('''CREATE TABLE  paths(
                path_id     INTEGER PRIMARY KEY,
                editor      TEXT,
                project     TEXT)''')
        self.bd.execute('''CREATE TABLE levels(
                levels_id   INTEGER PRIMARY KEY,
                name        TEXT,
                path        TEXT)''')
        self.bd.commit()
        self.bd.close()

        msg_def = 'Create a news base data'
        print(msg_def)

    def write_data_path(self, editor, project):
        count_paths = self.bd.execute('''SELECT count(path_id) FROM paths''')
        count_paths = count_paths.fetchone()[0]

        if count_paths == 0:
            self.bd.execute('''INSERT INTO paths
                            VALUES(?, ?, ?)''',
                            (count_paths, editor, project))

        else:
            self.bd.execute('''UPDATE paths 
                            SET editor = ?, project = ? 
                            WHERE path_id = ?''',
                            (editor, project, count_paths))

        self.bd.commit()

        msg_func = 'Write a news Data Path'
        print(msg_func)

    def write_data_levels(self):
        msg_func = 'Write a news Data Levels'
        print(msg_func)

    @staticmethod
    def read_data():
        msg_func = 'Read Data from the base data'
        print(msg_func)
