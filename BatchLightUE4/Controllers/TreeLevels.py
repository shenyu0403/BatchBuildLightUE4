import os, json

def builds_tree_lvls():
    print('!! Builds Levels Tree !!')
    path_json_setup = os.path.abspath("BatchLightUE4/Models/setup_path.json")
    path_json_lvl = os.path.abspath("BatchLightUE4/Models/lvls_tree.json")

    with open(path_json_setup) as f:
        paths_dict = json.load(f)

    lvls = {}
    path_project = os.path.dirname(paths_dict['UE4 Project']) + '/Content/'

    for root, dirs, files in os.walk(path_project):
        for file in files:
            if file.endswith('.umap'):
                print(os.path.join(root, file))
                lvls[file] = os.path.join(root, file)

        with open(path_json_lvl, 'w') as f:
            json.dump(lvls, f, indent=4)

    return lvls