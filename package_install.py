import pip

package = [
    'psutil',
    'json',
    'python-perforce',
    'tkinter',
]

def install(package):
    pip.main(['install', package])

for value in package:
    install(value)