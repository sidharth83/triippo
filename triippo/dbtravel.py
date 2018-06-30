import os, sys
import MySQLdb
from pprint import pprint
import re

def getCursor():
    db=MySQLdb.connect(user="travelzeus", passwd="sidharth", db="travelzeus")
    cur=db.cursor()
    return db, cur

def getCities():
    db, cur = getCursor()
    cur.execute("select city.name, country.name from city,country where city.country_id = country.id")
    result = cur.fetchall()
    db.close()
    return result

def getLocDetails(location):
    db, cur = getCursor()
    cur.execute("select id, latitude, longitude from city where name = '" + location + "'")
    result = cur.fetchall()
    db.close()
    return result

def getCityAttractions( cityId):
    db, cur = getCursor()
    sql = "select name, overview, latitude, longitude, icon, url from attractions where city_id=" + str( cityId)
    cur.execute(sql)
    result = cur.fetchall()
    db.close()
    return result