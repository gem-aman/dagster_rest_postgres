from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
from .rest_api_pipeline import source

@dlt_assets(
    dlt_source=source,
    dlt_pipeline=pipeline(
        pipeline_name="rest_pg",
        dataset_name="rest_pg",
        destination="postgres",
    ),
    name="rest_pg",
    group_name="rest_pg",
)
def dagster_rest_pg_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)
