from flask import Flask, jsonify, request
from BeerDatabase import BeerDatabase

app = Flask(__name__)

# Instanz der BeerDatabase-Klasse erstellen
beer_db = BeerDatabase('beer')
beer_db.connect()

# API-Endpunkt zum Abrufen aller Bierdaten
@app.route('/beers', methods=['GET'])
def get_beers():
    beers = beer_db.get_beers()
    return jsonify(beers)

# API-Endpunkt zum Hinzufügen eines neuen Bierdatensatzes
@app.route('/beers', methods=['POST'])
def add_beer():
    data = request.get_json()
    beer_db.add_beer(data)
    return jsonify(message="Beer added successfully")

@app.route('/malts', methods=['POST'])
def add_malts():
    data = request.get_json()
    beer_db.add_Malts(data['name'], data['description'], data['ebc'])
    return jsonify(message="Malts added successfully")

@app.route('/malts', methods=['GET'])
def get_malts():
    malts = beer_db.get_malts()
    return jsonify(malts)

@app.route('/hops', methods=['POST'])
def add_hops():
    data = request.get_json()
    beer_db.add_Hops(data['name'], data['description'], data['alpha'])
    return jsonify(message="Hops added successfully")

@app.route('/hops', methods=['GET'])
def get_hops():
    hops = beer_db.get_hops()
    return jsonify(hops)

@app.route('/yeast', methods=['POST'])
def add_yeast():
    data = request.get_json()
    beer_db.add_Yeast(data['name'], data['description'], data['alcohol'])
    return jsonify(message="Yeast added successfully")

@app.route('/yeast', methods=['GET'])
def get_yeast():
    yeast = beer_db.get_yeast()
    return jsonify(yeast)

@app.route('/fermentation', methods=['POST'])
def add_fermentation():
    data = request.get_json()
    beer_db.add_Fermentation(data['name'], data['description'], data['temperature'])
    return jsonify(message="Fermentation added successfully")

@app.route('/fermentation', methods=['GET'])
def get_fermentation():
    fermentation = beer_db.get_fermentation()
    return jsonify(fermentation)

@app.route('/fermentationmaturation', methods=['POST'])
def add_fermentationmaturation():
    data = request.get_json()
    beer_db.add_FermentationMaturation(data['name'], data['description'], data['temperature'])
    return jsonify(message="FermentationMaturation added successfully")

@app.route('/fermentationmaturation', methods=['GET'])
def get_fermentationmaturation():
    fermentationmaturation = beer_db.get_fermentationmaturation()
    return jsonify(fermentationmaturation)









if __name__ == '__main__':
    app.run(debug=True)
