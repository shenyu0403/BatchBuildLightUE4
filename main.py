from BatchLightUE4.Views.GUI import UIBuildMap

class BatchBuildSetup:
    def __init__(self):
        self.nom = 'Build Light Batch'

app_name = BatchBuildSetup().nom

if __name__ == "__main__":
    app = UIBuildMap(None)
    app.title(app_name)
    app.mainloop()
