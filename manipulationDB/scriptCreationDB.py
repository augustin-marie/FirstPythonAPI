# coding: utf-8
from requetesDB import RequetesDB

# ./dbname.db vas créé dbname.db dans le dossier parent ce qui est un peut contre intuitif
sql = RequetesDB("./interventions.db")

# On imagine que dans le futur on aurait une table client et une table technicien
# Mais pour le moment les champs idTechnicien et idClient ne renvoient vers rien
# resolu vaut 0 si l'intervention n'a pas encore été effectuée avec succés et 1 sinon
sqlCreatetable = f"CREATE TABLE IF NOT EXISTS interventions("\
    f"idIntevention INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"\
    f"idTechnicien INTEGER,"\
    f"idClient INTEGER,"\
    f"descriptionIntervention TEXT,"\
    f"lieuIntervention TEXT,"\
    f"resolu NUMERIC,"\
    f"compteRenduIntervention TEXT)"

sql.executerCommande(sqlCreatetable)
sql.commit()
sql.fermerConnection()