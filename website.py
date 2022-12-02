
from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from flask import render_template

es = Elasticsearch()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
  

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        Q = request.form['query']

        body = {
            "query": {
                "multi_match": {
                    "query": Q,
                    "fields": ["content", "title"]
                }
            }
        }
        res = es.search(index="wikisearch1", doc_type="title", body=body)
    else:
        print("error occured while making request")

    

    return render_template('result.html',result=res)

app.run(port=5000, debug=True)
