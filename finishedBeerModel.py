
def parse_finished_beers_result(rows):
    """
    Wandelt die SQL-Ergebnisse von FinishedBeers in eine Liste von Dictionaries um.
    Erwartet, dass das SQL bereits beer_name enthält.
    """
    result = []
    for row in rows:
        # Passe die Indizes ggf. an die Spaltenreihenfolge im SQL an!
        finished_beer = {
            "id": row[0],
            "note": row[1],
            "originalwort": row[2],
            "residual_extract": row[3],
            "beer_name": row[4]
        }
        result.append(finished_beer)
    return result
