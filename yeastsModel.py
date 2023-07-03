def parse_yeasts_result(result) :
    yeasts=[]

    yeast_dict={}

    for row in result :
        id=row[0]

        if id not in yeast_dict :
            yeast_dict[id]={
                "id" : id,
                "name": row[1],
                "description" :row[2],
                "attenuation" :row[3],
            }
    for key in yeast_dict :
        yeasts.append(yeast_dict[key])
    return yeasts