class Tabor:
    def __init__(self,kezdo_honap,kezdo_nap,zaro_honap,zaro_nap,diakok,tema):
        self.kezdo_honap = kezdo_honap
        self.kezdo_nap = kezdo_nap
        self.zaro_honap = zaro_honap
        self.zaro_nap = zaro_nap
        self.diakok = diakok
        self.tema = tema

    def __repr__(self):
        return f"{self.nyito_honap} - {self.nyito_nap} - {self.zaro_honap} - {self.zaro_nap} - {self.tema}"