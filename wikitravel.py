import os, sys
import urllib3
import json
import MySQLdb
from urllib.request import Request, urlopen
from pprint import pprint

import pdb

db=MySQLdb.connect(user="travelzeus", passwd="sidharth", db="travelzeus")

def main( city):
    try:
        wikiurl="https://wikitravel.org/wiki/en/api.php?action=query&format=json&titles=" + city + "&prop=revisions&rvprop=content"
        req = Request(wikiurl, headers={'User-Agent': 'Mozilla/5.0'})
        pdb.set_trace()
        result = urlopen(req)
        j = json.loads(result.read())
        k = j['query']['pages']
        q = k[str(max(k, key=int))]
        pg = q ['revisions'][0]['*']
        pprint(pg)
    except:
        print("Could not get data for city:: " + city)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Arguments should be city names to decode")
        sys.exit(1)
    i=1
    while(i < len(sys.argv)):
        main( sys.argv[i])
        i = i+1