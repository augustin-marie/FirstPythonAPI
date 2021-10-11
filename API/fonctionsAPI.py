# coding: utf-8
from flask import Flask, jsonify, request
from manipulationDB.requetesDB import RequetesDB
from manipulationDB.intervention import Intervention

app = Flask(__name__)

@app.route('/api/afficher')
def afficher():
    sql = RequetesDB("../interventions.db")
    sqlLecture = f"SELECT * FROM interventions"
    sql.executerCommande(sqlLecture)

    dicoInterventions={}
    for row in sql.cursor:
        dicoInterventions[row[0]] = str(Intervention(row[1], row[2], row[3], row[4], row[5], row[6]))

    return jsonify(dicoInterventions)

# @app.route('/api/ajouter/<int:idTechnicien>/<int:idClient>/<str:descriptionIntervention>/'\
#     '<str:lieuIntervention>/<int:resolu>/<str:compteRenduIntervention>', methods=['POST'])
# def ajouterInterventino():
#     team = request.get_json(force=True)
#     return ("OK")

if __name__=="__main__":
    app.run(debug=True)