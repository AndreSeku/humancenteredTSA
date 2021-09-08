---
sidebar_position: 1
---

# Flask-Webserver

There is the possibility to run the **hctsa**-package as a Python-based backend, based on Flask. Hence, there is a REST API to use build up and run the pipeline. Therefore, it is possible to integrate the **hctsa**-package as a standalone backend-service into existing or new applications.

## Start

At first, you have to download the **hctsa**-package manually from GitHub.
To start the Flask-webserver, you can use the Makefile and use the following command at the specific folder into your shell:
```bash
make run
```
The webserver can be accesses through `http://localhost:5000` or `http://0.0.0.0:5000`.

## REST API

The existing endpoints are as follows:

- `http://0.0.0.0:5000/pipeline/rules`: 

GET; {} -> Get JSON with method rules - as described in the method_rules.yml
- `http://0.0.0.0:5000/pipeline/data`: 

GET/POST: {„filename“: „test“} -> loading the test data
- `http://0.0.0.0:5000/pipeline/add`: 

GET/POST: {„method“: METHOD} -> adds METHOD into the pipeline; actually not working with the sns_methods for seaborn visualizations!
- `http://0.0.0.0:5000/pipeline/delete`: 

GET/POST {„position“: INT} -> deletes the function at position INT, -1 would be the last function in the pipeline
- `http://0.0.0.0:5000/pipeline/run`: 

GET: {} -> Runs the pipeline. Gets a JSON of the resulting pd.Series or pd.DataFrame Object
- `http://0.0.0.0:5000/pipeline/reset`: 

GET: {} -> Resetting the pipeline and the data to an empty pipeline.