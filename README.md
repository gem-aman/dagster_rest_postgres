## Steps
* Note: Running the basic rest app and the postgres as container.
* git clone & cd dagster_rest_postgres
* python -m venv venv
* venv\Scripts\activate.bat
* pip install dagster dagster-embedded-elt
* pip install -r dagster_rest_postgres/rest-postgres/rest_postgres/requirements.txt
* cd dagster_rest_postgres\rest-postgres && pip install -e ".[dev]"
* dagster dev

## Reference
* https://docs.dagster.io/integrations/embedded-elt/dlt
* https://github.com/dlt-hub/dlthub-education/blob/main/workshops/workshop_august_2024/part2/deployment/deploy_dagster/README.md