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
                "cookingTime" :row[11],
                "cookingTemperatur" :row[12],
                "fermentation" :[],
                "malts" :[],
                "wortBoiling" :{
                    "totalTime" :row[20],
                    "hops" :[]
                },
                "fermentationMaturation" :{
                    "fermentationTemperature" :row[26],
                    "carbonation" :row[27],
                    "yeast" :[]
                }
            }

        fermentation={
            "type" :row[13],
            "temperature" :row[14],
            "time" :row[15]
        }
        if fermentation not in beer_dict[id]["fermentation"]:
            beer_dict[id]["fermentation"].append(fermentation)
        # Malts hinzufügen
        malt={
            "name" :row[16],
            "description" :row[17],
            "EBC" :row[18],
            "quantity" :row[19]
        }
        if malt not in beer_dict[id]["malts"]:
            beer_dict[id]["malts"].append(malt)

        # Hops hinzufügen
        hop={
            "name" :row[21],
            "description" :row[22],
            "alpha" :row[23],
            "quantity" :row[24],
            "time" :row[25],
        }
        if hop not in beer_dict[id]["wortBoiling"]["hops"]:
            beer_dict[id]["wortBoiling"]["hops"].append(hop)

        # Yeast hinzufügen
        yeast={
            "name" :row[28],
            "description" :row[29],
            "EVG" :row[30],
            "temperature" :row[31],
            "type" :row[32]
        }
        if yeast not in beer_dict[id]["fermentationMaturation"]["yeast"]:
            beer_dict[id]["fermentationMaturation"]["yeast"].append(yeast)

    beers=list(beer_dict.values())
    return beers
