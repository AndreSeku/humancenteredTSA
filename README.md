-- ! under construction ! --

# humancenteredTSA
human centered TimeSeries Analysis

# Flask Webservice
Start the Flask Webserver with `make start` within the main folder. 
The server is running under localhost on port 5000: `http://localhost:5000`

### REST API

http://0.0.0.0:5000/pipeline/rules
- GET; {} -> Get JSON with method rules - as described in the method_rules.yml

http://0.0.0.0:5000/pipeline/data
- GET/POST: {„filename“: „test“} -> loading the test data

http://0.0.0.0:5000/pipeline/add
- GET/POST: {„method“: METHOD} -> adds METHOD into the pipeline; actually not working with the sns_methods for seaborn visualizations!

http://0.0.0.0:5000/pipeline/delete
 - GET/POST {„position“: INT} -> deletes the function at position INT, -1 would be the last function in the pipeline

http://0.0.0.0:5000/pipeline/run
- GET: {} -> Runs the pipeline. Gets a JSON of the resulting pd.Series or pd.DataFrame Object

http://0.0.0.0:5000/pipeline/reset
- GET: {} -> Resetting the pipeline and the data to an empty pipeline.


## Project Structure
- hctsa: core folders and files
- app.py, a flask server with a REST API for using the pipeline
- - pipeline for creating and running the pipeline
- - descriptive timeseries analysis
- - preparation of timeseries data
- - visualizations and explainability
- - exception handling

## Dependencies
- pandas
- math
- matplotlib
- seaborn
- flask
- flask_cors
