import json
import os


def project_name(path_project):
    if os.path.exists(path_project):
        with open(path_project) as file:
            data = json.load(file)
            data = data['Modules'][0]
            name = data['Name']

    else:
        name = ''

    return name
