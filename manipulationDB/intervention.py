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
    
    def __str__(self):
        return f"numéro technicien : {self.idTechnicien} / "\
            f"numéro client : {self.idClient} / "\
            f"description intervention : {self.descriptionIntervention} / "\
            f"lieu de l'intervention : {self.lieuIntervention} / "\
            f"status de résolution : {self.resolu} / "\
            f"compte rendu : {self.compteRenduIntervention}"