# coding: utf-8

# idTechnicien=0 veut dire que l'intervention n'a pas été distribuée
class Intervention:
    def __init__(self, idTechnicien, idClient, descriptionIntervention, lieuIntervention, resolu, compteRenduIntervention):
        self.idTechnicien=idTechnicien
        self.idClient=idClient
        self.descriptionIntervention=descriptionIntervention
        self.lieuIntervention=lieuIntervention
        self.resolu=resolu
        self.compteRenduIntervention=compteRenduIntervention