def parse_malts_result(result) :
    malts=[]

    malt_dict={}

    for row in result :
        id=row[0]

        if id not in malt_dict :
            malt_dict[id]={
                "id" : id,
                "name": row[1],
                "description" :row[2],
                "ebc" :row[3],
            }
    for key in malt_dict :
        malts.append(malt_dict[key])
    return malts