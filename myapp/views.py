from django.shortcuts import render
import sqlite3, json, os

def index(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    con = sqlite3.connect(dir_path + "/../CovidVaccineDB.sqlite3")
    cur = con.cursor()
    cur.execute('SELECT distinct(region) FROM Centers;')
    region = cur.fetchall()
    cur.execute('SELECT distinct(type) FROM Centers;')
    type = cur.fetchall()
    cur.execute('SELECT * FROM Centers;')
    row_headers=[x[0] for x in cur.description]
    data = cur.fetchall()
    json_data=[]
    for result in data:
        json_data.append(dict(zip(row_headers,result)))
    data = json.dumps(json_data)
    return render(request, 'index.html', context={'region' : region,'type' : type,'data' : data})
