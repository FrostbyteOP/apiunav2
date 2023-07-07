import os
from mysql.connector import Error
import mysql.connector
import app.serializer as serializer
class Connect():

  def __init__(self, host, db, user, passw, ssl) -> None:
    
    self.connection = mysql.connector.connect(
      host=host,
      database=db,
      user=user,
      password=passw,
      ssl_ca=ssl
      )

  def write_ride(self, q):
      
      
    '''title = "testrec" # varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
    price = 200 # int,
    members_id = "NULL"
    vehicle_id = "NULL" #int,
    owner_id = "NULL" #int,
    owner_name = "jonathan"# int,'''
    mycursor = self.connection.cursor()
    #mycursor.execute("""INSERT INTO ride(title, price, owner_name, endlocation, startlocation) 
    # VALUES ('Mac2', 2000, 'joanthan2', ST_GeomFromText( 'point(23.7786222 -81.1956483)', 4326 ), ST_GeomFromText( 'point(23.7786222 -81.1956473)',  4326 ))""")
    #print(queries.a)
    mycursor.execute(q)
    self.connection.commit()
    return True

  def get_rides(self, startlat, startlong, endlat, endlong):
    mycursor = self.connection.cursor()
    mycursor.execute("""SELECT id, title, price, starts_at, members_id, owner_id, owner_name, ST_AsText(startlocation), ST_AsText(endlocation) FROM ride WHERE ST_Distance(startlocation, ST_GeomFromText( 'point({startlat} {startlong})', 4326 )) < 1000 && ST_Distance(endlocation, ST_GeomFromText( 'point({endlat} {endlong})', 4326 )) < 1000 LIMIT 50;""".format(
      startlat=startlat,
      startlong=startlong,
      endlat=endlat,
      endlong=endlong
      ))
    a = mycursor.fetchall()
    serialized_res = serializer.data_serializer(a)
    return serialized_res

  def get_ride_byid(self, rideid):
    mycursor = self.connection.cursor()
    mycursor.execute("""SELECT id, title, price, starts_at, members_id, owner_id, owner_name, ST_AsText(startlocation), ST_AsText(endlocation) FROM ride WHERE ride.id = {rideid};""".format(rideid=rideid))
    op = mycursor.fetchall()
    serialized_res = serializer.data_serializer(op)
    return serialized_res
  #get_ride()

  #get_rides(18.499817, 73.9408529, 18.5006153, 73.9389066)
  def delete_ride_byid(self, rideid):
    mycursor = self.connection.cursor()
    mycursor.execute("""DELETE FROM ride WHERE ride.id = {rideid} """.format(rideid=rideid))
    self.connection.commit()
    return True

  def close_connection(self):
    self.connection.close()

  def get_user(self):
    mycursor = self.connection.cursor()
    mycursor.execute("""SELECT CURRENT_USER; """)
    op = mycursor.fetchall()
    return [op]

# from dotenv import load_dotenv
# load_dotenv(0)
# a = Connect(os.getenv("HOST"), os.getenv("DATABASE"), os.getenv("USERNAME_db"), os.getenv("PASSWORD"), os.getenv("SSL_CERT"))
# print(a.get_ride_byid(3))
# a.close_connection()

# print(a.get_user())