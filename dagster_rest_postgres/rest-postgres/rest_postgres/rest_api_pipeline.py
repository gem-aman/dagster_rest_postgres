from dlt.sources.rest_api import rest_api_source

source = rest_api_source({
    "client": {
        "base_url": "http://localhost:5000/",
    },
  "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "append",
            "endpoint": {
                "params": {
                    "per_page": 100,
                },
            },
        },
    "resources": [
        # "posts" will be used as the endpoint path, the resource name,
        # and the table name in the destination. The HTTP client will send
        # a request to "https://api.example.com/posts".
        "employees"
    ],
})


# pipeline = dlt.pipeline(
#     pipeline_name="rest_api_example",
#     destination="postgres",
#     dataset_name="rest_api_data",
# )

# load_info = pipeline.run(source)
# print(load_info)

# @dlt.resource(
#     columns={"event_tstamp": {"data_type": "timestamp", "precision": 3, "timezone": False}},
#     primary_key="event_id",
# )
# def events():
#     yield [{"event_id": 1, "event_tstamp": "2024-07-30T10:00:00.123"},
#            {"event_id": 2, "event_tstamp": "2024-07-30T10:00:00.123"},
#            {"event_id": 3, "event_tstamp": "2024-01-30T10:00:00.123"},
#            {"event_id": 4, "event_tstamp": "2024-08-30T10:00:00.123"}
#            ]

# pipeline = dlt.pipeline(destination="postgres", dataset_name="dlt_load",)
# print(pipeline.run(events(), table_name="events"))