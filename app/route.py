import requests
import polyline
from dotenv import load_dotenv
load_dotenv()
import os

def here_maps_route(orilat, orilong, deslat, deslong, mode):
    if mode == "car":
        req_str = os.getenv("HERE_MAPS_ROUTE_ENDPOINT_CAR")
    elif mode == "bike":
        req_str = os.getenv("HERE_MAPS_ROUTE_ENDPOINT_BIKE")
    
    req = req_str.format(orilat, orilong, deslat, deslong, os.getenv("HERE_MAPS_KEY"))
    res = requests.get(req)

    parsed_res = res.json()["routes"][0]
    res_polyline = parsed_res["sections"][0]["polyline"]
    print(res_polyline)
    #decoded_coordinates = polyline.decode(res_polyline)
    ##print(decoded_coordinates)
    coordinates = []
    return({"coordinates" : res_polyline})
    '''except:
        
        print(res.json())
        return({"error":"cant get route"})'''




if __name__ == "__main__":
    des = {"lat" :18.499980,
    "lon" :73.940783}

    ori = {"lat" : 18.494563,
    "lon" : 73.932510}

    req = os.getenv("HERE_MAPS_ROUTE_ENDPOINT_CAR").format(ori["lat"], ori["lon"], des["lat"], des["lon"], os.getenv("HERE_MAPS_KEY"))


    res = requests.get(req)


    parsed_res = res.json()["routes"][0]
    res_polyline = parsed_res["sections"][0]["polyline"]

    polyline_str = res_polyline

    decoded_coordinates = polyline.decode(polyline_str)

    print(type(decoded_coordinates[0]))


