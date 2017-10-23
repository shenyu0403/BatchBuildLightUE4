from configparser import ConfigParser
from os.path import abspath, dirname, join, exists


class Setup(object):
    config = ConfigParser()
    config_name = 'settings.ini'
    config_path = join(abspath(dirname(__package__)), config_name)

    def __init__(self):
        if exists(self.config_path):
            self.read()
        else:
            self.write()

    def write(self):
        self.config.add_section('Project Work')
        self.config.add_section('All Projects')
        self.config.add_section('Default')

        self.config['Default'] = {
            'Path': '',
            'Projects': '',
            'CSV': False,
        }

        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def read(self):
        data = self.config.read(self.config_path)

        return data

    def base(self):
        self.config.read(self.config_path)
        data = self.config.options('Default')

        return data
