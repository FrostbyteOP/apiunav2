def create_member(title, price, owner_name, owner_id,user_id, startloc_lat, startloc_long, endloc_lat, endloc_long, starts_at):
    #create a member query
    s = """INSERT INTO ride (title, price, owner_name, endlocation, startlocation, starts_at, members_id, owner_id) 
   VALUES ('{title}', {price}, '{owner_name}', ST_GeomFromText( 'point({endloc_lat} {endloc_long})', 4326 ), ST_GeomFromText( 'point({startloc_lat} {startloc_long})',  4326 ), '{starts_at}', {user_id}, {owner_id})""".format(
        user_id=user_id,
        title=title,
        price=price,
        owner_name=owner_name,
        owner_id=owner_id,
        startloc_lat=startloc_lat,
        startloc_long=startloc_long,
        endloc_lat=endloc_lat,
        endloc_long=endloc_long,
        starts_at=starts_at
        )
    return s



'''a = create_member(
    "newride",
    200,
    "rahul",
    100212,
    200123,
    18.4997712,
    73.9407345,
    18.5003320,
    73.9395507,
    "17:50"
)

#print(a)'''