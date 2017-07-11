import ctypes, sys

from BatchLightUE4.Views.GUI import UIBuildMap

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class BatchBuildSetup:
    def __init__(self):
        self.nom = 'Build Light Batch'

app_name = BatchBuildSetup().nom
app = UIBuildMap(None)
app.title(app_name)
print("Admin Needed")

if is_admin():
    print("Admin Ok")
    app.mainloop()

else:
    # Re-run the program with admin rights
    print("Admin pas Ok")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", app.mainloop(), "",
                                        None, 1)

# if __name__ == "__main__":