from fastapi import FastAPI, Request
import app.route as route
import app.queries as queries
import app.db_connect as db_connect
from dotenv import load_dotenv
load_dotenv()
import os

app = FastAPI()
connection = db_connect.Connect(os.getenv("HOST"), os.getenv("DATABASE"), os.getenv("USERNAME_db"), os.getenv("PASSWORD_db"), os.getenv("SSL_CERT"))

@app.get("/hello")
def hello():
    return {"main":"hello"}

@app.get("/get_route_{orilat}_{orilong}_{deslat}_{deslong}")
async def get_route(orilat, orilong, deslat, deslong):
    return route.here_maps_route(orilat, orilong, deslat, deslong, "bike")


@app.post("/push_ride")
async def getRideInformation(info : Request):
    req_info = await info.json()
    #print(req_info)
    query = queries.create_member(req_info['title'],
                                  req_info['price'],
                                  req_info['owner_name'],
                                  req_info['owner_id'],
                                  req_info['user_id'],
                                  req_info['startloc_lat'],
                                  req_info['startloc_long'],
                                  req_info['endloc_lat'],
                                  req_info['endloc_long'],
                                  req_info['starts_at'])
    
    if connection.write_ride(query):
        return {
        "status" : "SUCCESS",
        "data" : req_info
    }
    else:
        return {"res" : "error"}

@app.get("/get_rides/{startlat}_{startlong}_{endlat}_{endlong}")
async def get_rides_close(startlat, startlong, endlat, endlong):
    res = connection.get_rides(startlat=startlat, startlong=startlong, endlat=endlat, endlong=endlong)
    print(res)
    return {"res": res}

@app.get("/get_ride/{ride_id}")
async def get_ride_by_id(ride_id):
    res = connection.get_ride_byid(rideid=ride_id)
    #print(res)
    return {"res": res}

@app.get("/delete_ride/{ride_id}")
async def delete_ride(ride_id):
    res = connection.delete_ride_byid(rideid=ride_id)
    if res:
        return {"res" : "deleted Successfully"}
    else:
        return {"res" : "delete unsuccesfull :("}