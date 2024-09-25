* git clone & cd dagster_rest_postgres
* python -m venv venv
* venv\Scripts\activate.bat
* pip install dagster dagster-embedded-elt
* dagster project scaffold --name rest-postgres
* cd rest_postgres
* dlt init rest_api postgres
* pip install -r requirements.txt
* the *pipeline.py is only going to work with sources and need to remove other stuff : https://github.com/dlt-hub/dlthub-education/blob/main/workshops/workshop_august_2024/part2/deployment/deploy_dagster/README.md#add-dlt-pipeline-to-github_source
* cd ../ && pip install -e ".[dev]"
* follow the doc :  https://github.com/dlt-hub/dlthub-education/blob/main/workshops/workshop_august_2024/part2/deployment/deploy_dagster/README.md

https://docs.dagster.io/integrations/embedded-elt/dlt
