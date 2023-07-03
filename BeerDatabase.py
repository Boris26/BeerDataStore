import json
import sqlite3
import json
import beerModel
import hopsModel
import maltsModel
import yeastsModel


class BeerDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.lastId = 0

    def get_connection(self) :
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
        with self.get_connection() as conn :
            cursor=conn.cursor()
            cursor.execute("""
         SELECT DISTINCT
    Beer.id,
    Beer.name,
    Beer.type,
    Beer.color,
    Beer.alcohol,
    Beer.originalwort,
    Beer.bitterness,
    Beer.description,
    Beer.rating,
    Beer.mashVolume,
    Beer.spargeVolume,
    FermentationSteps.type AS fermentationType,
    FermentationSteps.temperature AS fermentationTemperature,
    FermentationSteps.time AS fermentationTime,
    Malts.name AS maltName,
    Malts.description AS maltDescription,
    Malts.EBC AS maltEBC,
    BeerMalts.quantity AS maltQuantity,
    WortBoiling.totalTime AS wortBoilingTotalTime,
    Hops.name AS hopName,
    Hops.description AS hopDescription,
    Hops.alpha AS hopAlpha,
    BeerHops.quantity AS hopQuantity,
    BeerHops.time AS hopTime,
    FermentationMaturation.fermentationTemperature AS fermentationMaturationTemperature,
    FermentationMaturation.carbonation AS fermentationMaturationCarbonation,
    Yeasts.name AS yeastName,
    Yeasts.description AS yeastDescription,
    Yeasts.EVG AS yeastEVG,
    Yeasts.temperature AS yeastTemperature,
    Yeasts.type AS yeastType
FROM
    Beer
LEFT JOIN
    FermentationSteps ON Beer.id = FermentationSteps.beer_id
LEFT JOIN
    BeerMalts ON Beer.id = BeerMalts.beer_id
LEFT JOIN
    Malts ON BeerMalts.malts_id = Malts.id
LEFT JOIN
    WortBoiling ON Beer.id = WortBoiling.beer_id
LEFT JOIN
    BeerHops ON Beer.id = BeerHops.beer_id
LEFT JOIN
    Hops ON BeerHops.hops_id = Hops.id
LEFT JOIN
    FermentationMaturation ON Beer.id = FermentationMaturation.beer_id
LEFT JOIN
    BeerYeast ON Beer.id = BeerYeast.beer_id
LEFT JOIN
    Yeasts ON BeerYeast.yeast_id = Yeasts.id;
            """)
            beers=cursor.fetchall()
            b = beerModel.parse_beer_result(beers)
            jso = json.dumps(b, indent = 4)
            return jso
    def add_beer(self, data):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            print(data)
            query = "INSERT INTO Beer (name, type, color, alcohol, originalwort, bitterness, description, rating, mashVolume,spargeVolume) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? ,?)"
            values = (data['name'], data['type'], data['color'], data['alcohol'], data['originalwort'], data['bitterness'], data['description'], data['rating'], data['mashVolume'], data['spargeVolume'])
            cursor.execute(query, values)
            self.lastId = cursor.lastrowid
            conn.commit()
            self.addMaltsToBeer(data)
            self.addHopsToBeer(data)
            self.addYeastToBeer(data)
            self.addFermenationSteps(data)

    def addMaltsToBeer(self, data):
        malts = data['malts']
        for malt in malts:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = "INSERT INTO BeerMalts (beer_id, malts_id, quantity) VALUES (?, ?, ?)"
                values = (self.lastId, malt['id'], malt['quantity'])
                cursor.execute(query, values)
                conn.commit()
    def addHopsToBeer(self, data):
        hops = data['wortBoiling']['hops']
        for hop in hops:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = "INSERT INTO BeerHops (beer_id, hops_id, quantity, time) VALUES (?, ?, ?, ?)"
                values = (self.lastId, hop['id'], hop['quantity'], hop['time'])
                cursor.execute(query, values)
                conn.commit()

    def addYeastToBeer(self, data):
        yeasts = data['fermentationMaturation']['yeast']
        for yeast in yeasts:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = "INSERT INTO BeerYeast (beer_id, yeast_id, quantity) VALUES (?, ?,?)"
                values = (self.lastId, yeast['id'], yeast['quantity'])
                cursor.execute(query, values)
                conn.commit()

    def addFermenationSteps(self, data):
        fermentationSteps = data['fermentationSteps']
        for fermentationStep in fermentationSteps:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = "INSERT INTO FermentationSteps (beer_id, type, temperature, time) VALUES (?, ?, ?, ?)"
                values = (self.lastId, fermentationStep['type'], fermentationStep['temperature'], fermentationStep['time'])
                cursor.execute(query, values)
                conn.commit()



    def add_Malts(self,name,description,ebc):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Malts (name, description, ebc) VALUES (?, ?, ?)"
            values = (name, description, ebc)
            cursor.execute(query, values)
            conn.commit()

    def add_Hops(self,name,description,alpha):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Hops (name, description, alpha) VALUES (?, ?, ?)"
            values = (name, description, alpha)
            cursor.execute(query, values)
            conn.commit()

    def add_Yeasts(self,name,description,attenuation):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Yeasts (name, description, attenuation) VALUES (?, ?, ?)"
            values = (name, description, attenuation)
            cursor.execute(query, values)
            conn.commit()

    def get_malts(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Malts")
            malts = maltsModel.parse_malts_result(cursor.fetchall())
            jsonMalts = json.dumps(malts, indent=4)
            return jsonMalts

    def get_hops(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hops")
            hops = hopsModel.parse_hops_result(cursor.fetchall())
            jsonHops = json.dumps(hops, indent=4)
            return jsonHops

    def get_yeasts(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Yeasts")
            yeasts = yeastsModel.parse_yeasts_result(cursor.fetchall())
            jsonYeasts = json.dumps(yeasts, indent=4)
            return jsonYeasts


