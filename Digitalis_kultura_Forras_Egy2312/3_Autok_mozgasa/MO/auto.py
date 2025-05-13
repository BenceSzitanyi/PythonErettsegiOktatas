class Auto:
    def __init__(self,rendszam,ora,perc,sebesseg):
        self.rendszam = rendszam
        self.ora = ora
        self.perc = perc
        self.sebesseg = sebesseg

    def __repr__(self):
        return f"{self.rendszam} - {self.ora} - {self.perc} - {self.sebesseg} km/h"