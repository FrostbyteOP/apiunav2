
from shapely import from_wkb, Point, to_geojson
from shapely.wkt import loads
import json

#this will serialize the data into a json for easier usage on the front
def data_serializer(list_data):
    out_lis = []
    for output in list_data:
        out_dic = {}
        keys = ["id", "title", "price", "starts_at", "members_id", "owner_id", "owner_name", "startlocation", "endlocation"]
        if len(output) != len(keys):
            return False
        
        for i in range(len(output)):
            to_ins = ''
            if keys[i] == "startlocation" or keys[i] == "endlocation":
                a = output[i]
                a = str(a)
                point = loads(a)
                to_ins = to_geojson(point)
                to_ins = json.loads(to_ins)
                #print(to_ins)
                to_ins = to_ins["coordinates"]
            else:
                to_ins = output[i]
            out_dic[keys[i]] = to_ins
        
        out_lis.append(out_dic)


    return out_lis