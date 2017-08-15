# BatchBuildLightUE4
[Python] [PyQt5] [UE4] [GameArt] [GameDev]

## Summary
Python tools [GUI] to automatize your *build light* process on UE4 project. This tools are in dev, it's functional but only for my project, a huge refactoring are needed to work for all project.

# Dependence
This tool use Python 3.6 and work with any package :
 - PyQt5
 - python-perforce
 - psutil
 - ifaddr

# How to use
For the first used, don't forget to  fill all path field (on the bottom window).
If your path are alright, select your level and click on build.

 You can select the checkbox "All" to force your Swarm Agent to use more machine.

 !! Don't forget to disable your hibernate option from Windows !!

![Screen Capture](Ressources/ScreenBatchBuildLight.jpg)

## Batch File
### Launch
This .bat launch the program.

### Update
Use this .bat to download the latest git version.

### Packages
Install all python dependence.