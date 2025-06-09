GET_BEERS = """
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
    Beer.cookingTime,
    Beer.cookingTemperatur,
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
"""

ADD_BEER = "INSERT INTO Beer (name, type, color, alcohol, originalwort, bitterness, description, rating, mashVolume,spargeVolume,cookingTime,cookingTemperatur) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? ,?,?,?)"

AKTIVATE_BEER = "UPDATE Beer SET aktiv = 1 WHERE id = ?"

GET_AKTIV_BEER = "SELECT * FROM Beer WHERE aktiv = 1"

ADD_MALTS = "INSERT INTO Malts (name, description, ebc) VALUES (?, ?, ?)"

ADD_HOP = "INSERT INTO Hops (name, description, type ,alpha) VALUES (?, ?, ?,?)"

ADD_YEAST = "INSERT INTO Yeasts (name,evg,description,temperature, type) VALUES (?, ?, ?, ?,?)"

GET_MALTS = "SELECT * FROM Malts"

GET_HOPS = "SELECT * FROM Hops"

GET_YEASTS = "SELECT * FROM Yeasts"

GET_FINISHED_BEERS = "SELECT * FROM FinishedBeers"

ADD_FINISHED_BEER = "INSERT INTO FinishedBeers (note, originalwort, residual_extract, beer_id) VALUES (?, ?, ?, ?)"

ADD_BEERMALTS = "INSERT INTO BeerMalts (beer_id, malts_id, quantity) VALUES (?, ?, ?)"
ADD_BEERHOPS = "INSERT INTO BeerHops (beer_id, hops_id, quantity, time) VALUES (?, ?, ?, ?)"
ADD_BEERYEAST = "INSERT INTO BeerYeast (beer_id, yeast_id, quantity) VALUES (?, ?, ?)"
ADD_FERMENTATIONSTEPS = "INSERT INTO FermentationSteps (beer_id, type, temperature, time) VALUES (?, ?, ?, ?)"