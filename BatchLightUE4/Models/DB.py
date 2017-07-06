import os
import json
# -----------------------------
# Generate all data needs to know enviroment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
levels_dict = {
    # Gymnasium
    1: ('GYM01', 'SanJuanTheater'),
    2: ('GYM02', 'MittelbrunnZentrum'),
    # Stadium
    3: ('STA00', 'Ui'),
    4: ('STA01', 'UmmDharbStadium'),
    5: ('STA02', 'ManzoVBArena'),
    6: ('STA03', 'BanKhaemSporthall'),
    7: ('STA04', 'HosojimiCenter'),
    8: ('STA05', 'CharlesFrabetStadium'),
    9: ('STA06', 'JalbarosCenterArena'),
    10: ('STA07', 'CuapixcoEsteColegio'),
    11: ('STA08', 'AbramCenterStadium'),
    12: ('STA09', 'PretovkaClubStadion'),
    # Training Courts
    13: ('TC01', 'RoyalStratfordGymnasium'),
    14: ('TC02', 'MartinSherpardHall'),
}

slave = {
    1: ('Aurel', 'DESKTOP-O6QPOKM'),
    2: ('Quentin', 'MUTTON03'),
    3: ('Marine', 'WHITESHEEP02'),
}
revisions = []

path_json = os.path.abspath(
    "BatchLightUE4/Models/setup.json")

if os.path.isfile(path_json):
    with open(path_json) as f:
        paths_dict = json.load(f)

else:
    paths_dict = {
        "UE4 Editor": "UE4Editor.exe",
        "UE4 Project": "Project.uproject",
    }
