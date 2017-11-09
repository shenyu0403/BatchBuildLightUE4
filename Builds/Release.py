"""Generate a Packages with the update version, launch this file and follow
all indication."""

# 1/ Check the number version
# 2/ Propose a news number version
# 3/ Edit the INI file and pack-it
# 4/ Upload on Github :) .

from BatchLightUE4.Controllers.Setup import Setup

init = Setup()
print('Actual Version : ', init.version())
nbr_version = input('Number Version : ')
init.version(update=nbr_version)

