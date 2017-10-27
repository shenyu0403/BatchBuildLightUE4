import json

from os.path import exists, isfile


def project_name(path_project):
    name = ''
    if exists(path_project) and isfile(path_project):
        with open(path_project) as file:
            data = json.load(file)
            if data.get('Modules'):
                data = data['Modules'][0]
                name = data['Name']

    return name
