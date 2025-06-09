from flask import Flask, jsonify, request
from flask_cors import CORS
from BeerDatabase import BeerDatabase

app = Flask(__name__)
CORS(app)
beer_db = BeerDatabase('beer.db')
beer_db.connect()


@app.route('/beers', methods=['GET'])
def get_beers():
    try:
        beers = beer_db.get_beers()
        return jsonify(beers)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/beer', methods=['POST'])
def add_beer():
    try:
        data = request.get_json()
        beer_db.add_beer(data)
        return jsonify(message="Beer added successfully")
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/aktivebeer', methods=['GET'])
def get_aktivebeer():
    try:
        beer = beer_db.get_aktiv_beer()
        return jsonify(beer)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/malt', methods=['POST'])
def add_malts():
    try:
        data = request.get_json()
        beer_db.add_malts(data)
        return jsonify(message="Malts added successfully")
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/malts', methods=['GET'])
def get_malts():
    try:
        malts = beer_db.get_malts()
        return jsonify(malts)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/hop', methods=['POST'])
def add_hops():
    try:
        data = request.get_json()
        beer_db.add_hop(data)
        return jsonify(message="Hops added successfully")
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/hops', methods=['GET'])
def get_hops():
    try:
        hops = beer_db.get_hops()
        return jsonify(hops)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/yeast', methods=['POST'])
def add_yeast():
    try:
        data = request.get_json()
        beer_db.add_yeast(data)
        return jsonify(message="Yeast added successfully"), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/yeasts', methods=['GET'])
def get_yeast():
    try:
        yeast = beer_db.get_yeasts()
        return jsonify(yeast)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/finishedbeers', methods=['GET'])
def get_finishedbeers():
    try:
        finished_beers = beer_db.get_finished_beers()
        return jsonify({"finishedbeers": finished_beers})
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route('/finishedbeer', methods=['POST'])
def add_finishedbeer():
    try:
        data = request.get_json()
        beer_db.add_finished_beer(data)
        return jsonify(message="Finished Beer added successfully")
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.errorhandler(404)
def not_found(error=None):
    return jsonify(message="Endpoint not found"), 404


@app.errorhandler(500)
def internal_server_error(error=None):
    return jsonify(message="Internal server error"), 500


if __name__ == '__main__':
    app.run()