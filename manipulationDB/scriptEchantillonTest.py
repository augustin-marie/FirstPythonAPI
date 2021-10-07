# coding: utf-8
from intervention import Intervention
from requetesDB import RequetesDB

# échantillon test pour test l'afficheage de l'API

echantillonTest ={
    Intervention(8, 18, "Intervention test n°1", "671 rue Ultricies", 0, ''),
    Intervention(2, 26, "Intervention test n°2", "12 rue Magnis", 1, 'Intervention effectuée'),
    Intervention(10, 5, "Intervention test n°3", "12 Avenue Amet", 0, ''),
    Intervention(4, 4, "Intervention test n°4", "64 Country Road", 0, ''),
    Intervention(0, 47, "Intervention test n°5", "19 avenue de Sed", 1, 'Intervention effectuée'),
    Intervention(5, 4, "Intervention test n°6", "39 rue Lacinia", 0, ''),
    Intervention(10, 29, "Intervention test n°7", "15 route de Nullam", 1, 'Intervention effectuée'),
}

try :
    sql = RequetesDB("./interventions.db")

    for interventionTest in echantillonTest:
        sqlInsert = f"Insert into interventions(idTechnicien, idClient, descriptionIntervention,"\
            f"lieuIntervention, resolu, compteRenduIntervention) VALUES ('{interventionTest.idTechnicien}', "\
            f"'{interventionTest.idClient}','{interventionTest.descriptionIntervention}',"\
            f"'{interventionTest.lieuIntervention}','{interventionTest.resolu}','{interventionTest.compteRenduIntervention}')"
        sql.executeCommand(sqlInsert)
        sql.commit()

except Exception as exc:
    print("Une erreur c'est produite : " + str(exc))
    sql.closeConnection()