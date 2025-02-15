from flask import Flask, render_template, jsonify
import datetime
import json
import random

app = Flask(__name__)

def jours_restants():
    """Calcule le nombre de jours restants jusqu'au 29 mars 2025."""
    date_cible = datetime.date(2025, 3, 29)
    aujourd_hui = datetime.date.today()
    jours = (date_cible - aujourd_hui).days
    return jours

def charger_blague():
    """Charge une blague aléatoire depuis blagues.json."""
    try:
        with open("blagues.json", "r", encoding="utf-8") as fichier:
            blagues = json.load(fichier)
            return random.choice(blagues)
    except Exception as e:
        print(f"Erreur lors du chargement des blagues : {e}")
        return {"titre": "Blague en attente 😆", "texte": "Pas de blague disponible pour le moment."}

@app.route("/")
def index():
    jours = jours_restants()
    blague = charger_blague()
    return render_template("index.html", jours=jours, blague=blague)

@app.route("/blague")
def nouvelle_blague():
    """Renvoie une nouvelle blague au format JSON."""
    blague = charger_blague()
    return jsonify(blague)

if __name__ == "__main__":
    app.run(debug=True)