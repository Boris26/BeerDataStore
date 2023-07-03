def parse_hops_result(result) :
    hops=[]

    hop_dict={}

    for row in result :
        id=row[0]

        if id not in hop_dict :
            hop_dict[id]={
                "id" : id,
                "name": row[1],
                "description" :row[2],
                "alpha" :row[3],
            }
    for key in hop_dict :
        hops.append(hop_dict[key])
    return hops