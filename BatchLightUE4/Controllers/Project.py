import json
import os


def project_name(path_project):
    if os.path.exists(path_project):
        with open('data.json') as path_project:
            data = json.load(path_project)

        print(data)

    else:
        data = ''

    return data
