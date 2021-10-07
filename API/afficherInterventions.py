# coding: utf-8
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/afficher')
def afficher():
    dicoInterventions={}
    return jsonify(dicoInterventions)

@app.route('/api/ajouter/<int:idTechnicien>/<int:idClient>/<str:descriptionIntervention>/'\
    '<str:lieuIntervention>/<int:resolu>/<str:compteRenduIntervention>', methods=['POST'])
def ajouterInterventino():
    team = request.get_json(force=True)
    return ("OK")

if __name__=="__main__":
    app.run(debug=True)