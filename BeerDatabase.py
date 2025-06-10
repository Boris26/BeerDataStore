import json
import sqlite3
import beerModel
import hopsModel
import maltsModel
import yeastsModel
import sql_queries
import finishedBeerModel  # Modell für FinishedBeers


class BeerDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.last_id = 0
        self.connection = None
        self.cursor = None

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def get_beers(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_queries.GET_BEERS)
            beers = cursor.fetchall()
            b = beerModel.parse_beer_result(beers)
            json_data = json.dumps(b, indent=4)
            return json_data

    def add_beer(self, data):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = sql_queries.ADD_BEER
            values = (
                data['name'], data['type'], data['color'], data['alcohol'], data['originalwort'], data['bitterness'],
                data['description'], data['rating'], data['mashVolume'], data['spargeVolume'], data['cookingTime'],
                data['cookingTemperatur']
            )
            cursor.execute(query, values)
            self.last_id = cursor.lastrowid
            conn.commit()
            self.add_malts_to_beer(data)
            self.add_hops_to_beer(data)
            self.add_yeast_to_beer(data)
            self.add_fermenation_steps(data)

    def add_malts_to_beer(self, data):
        malts = data.get('malts', [])
        if not malts:
            return
        with self.get_connection() as conn:
            cursor = conn.cursor()
            for malt in malts:
                query = sql_queries.ADD_BEERMALTS  # <-- ausgelagert
                values = (self.last_id, malt['id'], malt['quantity'])
                cursor.execute(query, values)
            conn.commit()

    def add_hops_to_beer(self, data):
        hops = data.get('wortBoiling', {}).get('hops', [])
        if not hops:
            return
        with self.get_connection() as conn:
            cursor = conn.cursor()
            for hop in hops:
                query = sql_queries.ADD_BEERHOPS  # <-- ausgelagert
                values = (self.last_id, hop['id'], hop['quantity'], hop['time'])
                cursor.execute(query, values)
            conn.commit()

    def add_yeast_to_beer(self, data):
        yeasts = data.get('fermentationMaturation', {}).get('yeast', [])
        if not yeasts:
            return
        with self.get_connection() as conn:
            cursor = conn.cursor()
            for yeast in yeasts:
                query = sql_queries.ADD_BEERYEAST  # <-- ausgelagert
                values = (self.last_id, yeast['id'], yeast['quantity'])
                cursor.execute(query, values)
            conn.commit()

    def add_fermentation_steps(self, data):
        fermentation_steps = data.get('fermentationSteps', [])
        if not fermentation_steps:
            return
        with self.get_connection() as conn:
            cursor = conn.cursor()
            for fermentation_step in fermentation_steps:
                query = sql_queries.ADD_FERMENTATIONSTEPS  # <-- ausgelagert
                values = (self.last_id, fermentation_step['type'], fermentation_step['temperature'], fermentation_step['time'])
                cursor.execute(query, values)
            conn.commit()

    def add_malts(self, data):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = sql_queries.ADD_MALTS
            values = (data['name'], data['description'], data['ebc'])
            cursor.execute(query, values)
            conn.commit()

    def add_hop(self, data):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = sql_queries.ADD_HOP
            values = (data['name'], data['description'], data['type'], data['alpha'])
            cursor.execute(query, values)
            conn.commit()

    def add_yeast(self, data):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = sql_queries.ADD_YEAST
            values = (data['name'], data['evg'], data['description'], data['temperature'], data['type'])
            try:
                cursor.execute(query, values)
                conn.commit()
            except Exception as e:
                raise Exception("Failed to insert yeast into the database: " + str(e))

    def get_malts(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_queries.GET_MALTS)
            malts = maltsModel.parse_malts_result(cursor.fetchall())
            json_data = json.dumps(malts, indent=4)
            return json_data

    def get_hops(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_queries.GET_HOPS)
            hops = hopsModel.parse_hops_result(cursor.fetchall())
            json_data = json.dumps(hops, indent=4)
            return json_data

    def get_yeasts(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_queries.GET_YEASTS)
            yeasts = yeastsModel.parse_yeasts_result(cursor.fetchall())
            json_data = json.dumps(yeasts, indent=4)
            return json_data

    def get_finished_beers(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_queries.GET_FINISHED_BEERS)
            finished_beers = finishedBeerModel.parse_finished_beers_result(cursor.fetchall())
            return finished_beers

    def add_finished_beer(self, data):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = sql_queries.ADD_FINISHED_BEER
            values = (
                data.get('note'),
                data.get('originalwort'),
                data.get('residual_extract'),
                data.get('beer_id')
            )
            cursor.execute(query, values)
            conn.commit()