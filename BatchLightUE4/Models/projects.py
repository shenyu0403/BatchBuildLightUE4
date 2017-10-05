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
            self.create_all_tables()

    def create_all_tables(self):
        self.bd.execute('''CREATE TABLE  projects(
                id          INTEGER PRIMARY KEY,
                paths_id    INT,
                levels_id   INT)''')

        self.bd.execute('''CREATE TABLE  paths(
                path_id     INTEGER PRIMARY KEY,
                editor      TEXT,
                project     TEXT)''')

        self.bd.execute('''CREATE TABLE levels(
                level_id   INTEGER PRIMARY KEY,
                project_id   INTEGER,
                name        TEXT,
                path        TEXT)''')
        self.bd.commit()
        # self.bd.close()

        msg_def = 'Create a news base data'
        print(msg_def)

    def select_project(self):
        self.bd.execute('''SELECT id, project_id, paths_id
                        FROM projects''')
        self.bd.cursor()

        msg_func = 'Select a Projects'
        print(msg_func)

    def select_path(self, id_project):
        """Select a Data path from a project used.
        :id_project : The project working"""
        request = self.bd.cursor()
        request.execute('''SELECT * 
                        FROM paths 
                        WHERE path_id = ?''',
                        (id_project, ))

        data = request.fetchall()

        return data

    def select_levels(self, id_project):
        """Select a Data path from a project used.
        :id_project : The project working"""
        request = self.bd.cursor()
        request.execute('''SELECT * 
                        FROM levels 
                        WHERE project_id = ?''',
                        (id_project, ))

        data = request.fetchall()

        return data

    def write_data_path(self, editor, project):
        id_project = 0
        self.bd.cursor()
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
        id_project = 0
        levels = {}
        path_data = self.select_path(id_project)
        path_data = path_data[0][2]
        path_project = os.path.dirname(path_data) + '/Content/'

        for root, dirs, files in os.walk(path_project):
            for file in files:
                if file.endswith('.umap'):
                    levels[file] = os.path.join(root, file)

                    cur = self.bd.cursor()
                    cur.execute('''
                    INSERT INTO levels(project_id, name, path) 
                    VALUES (?, ?, ?)''',
                                (id_project, file, root))

        # INSERT INTO COMPANY VALUES(7, 'James', 24, 'Houston', 10000.00)
        self.bd.commit()
        self.bd.close()

        msg_func = 'Write a news Data Levels'
        print(msg_func)

    def debug_data(self):
        cur = self.bd.cursor()
        cur.execute('''SELECT * FROM paths''')

        rows = cur.fetchall()

        for row in rows:
            print('Data : ', row)

        msg_func = 'Read Data from the base data'
        print(msg_func)
