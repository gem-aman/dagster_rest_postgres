from setuptools import find_packages, setup

setup(
    name="rest_postgres",
    packages=find_packages(exclude=["rest_postgres_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
