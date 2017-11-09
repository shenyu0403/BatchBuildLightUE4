"""Generate a Packages with the update version, launch this file and follow
all indication."""

# 1/ Check the number version -> Valid
# 2/ Propose a news number version -> Valid
# 3/ Edit the INI file and pack-it -> Valid
# 4/ Upload on Github :) .

import subprocess

from os.path import dirname
from BatchLightUE4.Controllers.Setup import Setup

# All Variable
init = Setup()
package = dirname(__file__) + '/packages.bat'

print('Actual Version : ', init.version())
nbr_version = input('Number Version : ')
init.version(update=nbr_version)

subprocess.call(package)
