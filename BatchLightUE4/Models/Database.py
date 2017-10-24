import os
import sqlite3

from os.path import dirname


class TableProgram(object):
    """Objects to work with the SQLite"""

    def __init__(self):
        super(TableProgram, self).__init__()
        self.base_sql = 'projects.db'
        self.bd_exist = os.path.exists(self.base_sql)

        self.bd = sqlite3.connect(self.base_sql)

        if not self.bd_exist:
            self.create_all_tables()

    def create_all_tables(self):
        self.bd.cursor()
        self.bd.execute('''CREATE TABLE  projects(
                id          INTEGER PRIMARY KEY,
                name        TEXT,
                CSV         TEXT)''')

        self.bd.execute('''CREATE TABLE  paths(
                path_id     INTEGER PRIMARY KEY,
                editor      TEXT,
                project     TEXT,
                scene       TEXT,
                csv         TEXT)''')

        self.bd.execute('''CREATE TABLE levels(
                level_id    INTEGER PRIMARY KEY,
                name        TEXT,
                path        TEXT,
                state       INTEGER)''')

        self.bd.execute('''CREATE TABLE csv(
                level_id    INTEGER PRIMARY KEY,
                name        TEXT,
                path        TEXT,
                state       INTEGER)''')
        self.bd.commit()
        # self.bd.close()

    def select_project(self):
        self.bd.cursor()
        self.bd.execute('''SELECT id, project_id, paths_id
                        FROM projects''')

    def select_path(self, id_project):
        """Select a Data path from a project used.
        :id_project : The project working"""
        request = self.bd.cursor()
        request.execute('''SELECT * FROM paths 
                        WHERE path_id = ?''',
                        (id_project, ))

        data = request.fetchall()

        return data

    def select_levels(self, state=None, name=None):
        """Select a Data path from a project used.
        :id_project : The project working"""
        request = self.bd.cursor()
        if state is not None:
            request.execute('''SELECT * FROM levels WHERE state = ?''',
                            (state, ))

        elif name is not None:
            request.execute('''SELECT * FROM levels WHERE name = ?''',
                            (name, ))
        else:
            request.execute('''SELECT * FROM levels''')

        data = request.fetchall()

        return data

    def write_data_path(self, editor, project, scene):
        id_project = 1
        self.bd.cursor()
        count_paths = self.bd.execute('''SELECT count(path_id) FROM paths''')
        count_paths = count_paths.fetchone()[0]

        if count_paths == 0:
            self.bd.execute('''INSERT INTO paths VALUES(?, ?, ?, ?, ?)''',
                            (id_project, editor, project, scene, 'None'))

        else:
            self.bd.execute('''UPDATE paths 
                            SET editor = ?, project = ?, scene = ? 
                            WHERE path_id = ?''',
                            (editor, project, scene, id_project))

        self.bd.commit()

    def write_data_levels(self, treeview=None, index=None):
        id_project = 1
        path_data = self.select_path(id_project)
        path_project = dirname(path_data[0][2])
        path_subfolder = path_data[0][3]
        path_project = path_project + '/Content/' + path_subfolder

        # Check if the levels are write
        # Isn't into the table add a news entry
        # Else update this entry
        self.bd.cursor()

        for root, dirs, files in os.walk(path_project):
            for file in files:
                path = root.replace('\\', '/') + '/' + file
                request = self.bd.execute('''SELECT * FROM levels 
                WHERE name = ?''', (file, ))
                if request.fetchone() is None:
                    self.bd.execute('''INSERT INTO levels
                                            (name, path, state)
                                            VALUES(?, ?, ?)''',
                                    (file, path, 0))
                elif index is not None:
                    name = treeview.levels_list.data(index)
                    state = treeview.levels_list.itemFromIndex(index).checkState()
                    self.bd.execute('''UPDATE levels SET state = ? WHERE 
                    name = ?''', (state, name, ))

        self.bd.commit()

    def table_csv(self):
        self.bd.cursor()
        # Read
        # Write
        # Remove
        self.bd.commit()
        data = 'Table CSV'

        return data

    def debug_data(self):
        cur = self.bd.cursor()
        cur.execute('''SELECT * FROM paths''')

        rows = cur.fetchall()

        for row in rows:
            print('Data : ', row)

        msg_func = 'Read Data from the base data'
        print(msg_func)

