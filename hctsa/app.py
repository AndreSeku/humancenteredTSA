#!/usr/bin/env python3

'''
This is the hctsa-core module, using Flask as a minimal backend webserver.
'''

# TODO Flask Server
# rest API:
# - potentielle nachfolgermethoden basierend auf spezifischer methode, array mit potentiellen methoden
# - add_method, return true, false
# - pipeline löschen/neu 'starten', return true, false
# - pipeline letztes element löschen, return true, false
# - pipeline run, return results

from pipeline.pipeline import Pipeline
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pipeline/add")
def pipeline_add():
  ...
  return

@app.route("/pipeline/delete")
def pipeline_delete():
  ...
  return

@app.route("/pipeline/run")
def pipeline_run():
  ...
  return

@app.route("/pipeline/reset")
def pipeline_reset():
  ...
  return



