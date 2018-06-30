from flask import Flask, render_template, url_for, request
from travelzeus.dbtravel import getCities, getLocDetails, getCityAttractions
import pdb
app = Flask(__name__)

@app.route('/landing1')
def landing1():
    loc = request.args.get('location')
    geo = getLocDetails( loc)
    if len(geo) < 1:
        return render_template("error.html")
    
    cityDetails = geo[0]
    attractions = getCityAttractions( cityDetails[0])
    if len( attractions) < 1:
        return render_template("error.html")
    
    return render_template('landing1.html', req=request, geo=geo[0], attractions=attractions)

@app.route('/landing2')
def landing2():
    return render_template('landing2.html', req=request)

@app.route('/landing3')
def landing3():
    return render_template('landing3.html', req=request)

@app.route('/landing4')
def landing4():
    return render_template('landing4.html', req=request)

@app.route('/')
def index():
    res = getCities()
    return render_template('index-new.html', cities=res)

if __name__ == "__main__":
    app.run()