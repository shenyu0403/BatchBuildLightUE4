from configparser import ConfigParser
from os.path import abspath, dirname, join, exists


class Setup(object):
    config = ConfigParser()
    config_name = 'settings.ini'
    config_path = join(abspath(dirname(__package__)), config_name)

    if exists(config_path):
        config.read(config_path)
    else:

        config.add_section('Last Project')
        config.add_section('All Projects')
        with open(config_path, 'w') as configfile:
            config.write(configfile)
