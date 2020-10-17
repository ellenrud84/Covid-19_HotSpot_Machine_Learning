import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify, render_template
import pandas as pd
import json
app = Flask(__name__)

engine = create_engine("postgres://xebpvwdekstjxy:24a096ddb472f7eb9219c48ea89643aaf7a800ef199ba143a88add1036ac8e53@ec2-3-210-178-167.compute-1.amazonaws.com:5432/d5vu678447dkqu", echo=False)

conn = engine.connect()

Demographics = pd.read_sql("select * from county_demographics",conn)

Harris_Demo = pd.read_sql("select * from county_demographics where fips_code=48201",conn)

Harris_CD  = pd.read_sql("select county_name, a.fips_code, date, cases, deaths from county_daily_data a join county_demographics b on a.fips_code =b.fips_code where a.fips_code =48201",conn)

Harris_View1 = 'select * from public."Harris_Mobility_CD"'

Harris_Mobility_CD = pd.read_sql(Harris_View1,conn)



queries = [Demographics,Harris_Demo,Harris_CD, Harris_Mobility_CD]
result =[]
parsed = []

for x in range(len(queries)):
    result.append(queries[x].to_json(orient='index'))
    parsed.append(json.loads(result[x]))


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Demographics")
def Demo():
    return jsonify(parsed[0])

@app.route("/48201_Demo")
def Harris_demo():
    return jsonify(parsed[1])

@app.route("/48201")
def Harris1():
    return jsonify(parsed[2])

@app.route("/48201_Full")
def Harris_Full():
    return jsonify(parsed[3])

if __name__ == "__main__":
    app.run(debug=True)
