import json

from os.path import exists, isfile


def project_name(path_project):
    if exists(path_project) and isfile(path_project):
        with open(path_project) as file:
            data = json.load(file)
            data = data['Modules'][0]
            name = data['Name']

    else:
        name = ''

    return name
