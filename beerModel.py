def parse_beer_result(result) :
    beers=[]

    beer_dict={}

    for row in result :
        id=row[0]

        if id not in beer_dict :
            beer_dict[id]={
                "id" : id,
                "name": row[1],
                "type" :row[2],
                "color" :row[3],
                "alcohol" :row[4],
                "originalwort" :row[5],
                "bitterness" :row[6],
                "description" :row[7],
                "rating" :row[8],
                "mashVolume" :row[9],
                "spargeVolume" :row[10],
                "fermentation" :[],
                "malts" :[],
                "wortBoiling" :{
                    "totalTime" :row[18],
                    "hops" :[]
                },
                "fermentationMaturation" :{
                    "fermentationTemperature" :row[24],
                    "carbonation" :row[25],
                    "yeast" :[]
                }
            }

        fermentation={
            "type" :row[11],
            "temperature" :row[12],
            "time" :row[13]
        }
        if fermentation not in beer_dict[id]["fermentation"]:
            beer_dict[id]["fermentation"].append(fermentation)
        # Malts hinzufügen
        malt={
            "name" :row[14],
            "description" :row[15],
            "EBC" :row[16],
            "quantity" :row[17]
        }
        if malt not in beer_dict[id]["malts"]:
            beer_dict[id]["malts"].append(malt)

        # Hops hinzufügen
        hop={
            "name" :row[19],
            "description" :row[20],
            "alpha" :row[21],
            "quantity" :row[22],
            "time" :row[23],
        }
        if hop not in beer_dict[id]["wortBoiling"]["hops"]:
            beer_dict[id]["wortBoiling"]["hops"].append(hop)

        # Yeast hinzufügen
        yeast={
            "name" :row[26],
            "description" :row[27],
            "EVG" :row[28],
            "temperature" :row[29],
            "type" :row[30]
        }
        if yeast not in beer_dict[id]["fermentationMaturation"]["yeast"]:
            beer_dict[id]["fermentationMaturation"]["yeast"].append(yeast)

    beers=list(beer_dict.values())
    return beers
