from flask import Flask, jsonify, request
from flask_cors import CORS
from BeerDatabase import BeerDatabase

app = Flask(__name__)
CORS(app)
# Instanz der BeerDatabase-Klasse erstellen
beer_db = BeerDatabase('beer')
beer_db.connect()

# API-Endpunkt zum Abrufen aller Bierdaten
@app.route('/beers', methods=['GET'])
def get_beers():
    beers = beer_db.get_beers()
    return jsonify(beers)

# API-Endpunkt zum Hinzufügen eines neuen Bierdatensatzes
@app.route('/beer', methods=['POST'])
def add_beer():
    data = request.get_json()
    beer_db.add_beer(data)
    return jsonify(message="Beer added successfully")

@app.route('/malt', methods=['POST'])
def add_malts():
    data = request.get_json()
    beer_db.add_Malts(data)
    return jsonify(message="Malts added successfully")

@app.route('/malts', methods=['GET'])
def get_malts():
    malts = beer_db.get_malts()

    return jsonify(malts)

@app.route('/hop', methods=['POST'])
def add_hops():
    data = request.get_json()
    beer_db.add_Hop(data)
    return jsonify(message="Hops added successfully")

@app.route('/hops', methods=['GET'])
def get_hops():
    hops = beer_db.get_hops()
    return jsonify(hops)

@app.route('/yeast', methods=['POST'])
def add_yeast():
    data = request.get_json()
    try:
        beer_db.add_Yeast(data)
        return jsonify(message="Yeast added successfully"),200
    except Exception as e:
        return jsonify(error=str(e)),201
@app.errorhandler(404)
def not_found():
    return jsonify(message="Endpoint not found"), 404

@app.errorhandler(500)
def internal_server_error():
    return jsonify(message="Internal server error"), 500



@app.route('/yeasts', methods=['GET'])
def get_yeast():
    yeast = beer_db.get_yeasts()
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

@app.route('/temperatur', methods=['GET'])
def get_temperature():
    temperature = 20
    return jsonify(temperature)







if __name__ == '__main__':
    app.run(debug=True)
