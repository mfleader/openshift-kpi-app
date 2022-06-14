# OpenShift KPI Application

## Configure Python Web Api

1. Install a Python virtual environment given the dependencies in `pyproject.toml`. Use your preferred python virtual environment management tool. Mine is [poetry](https://python-poetry.org/docs/).

Prerequisite:
- Python version >= 3.9
- current working directory is project root

```shell
poetry install
```


2. Fill out the confgiuration parameters. A skeleton is at `openshift-kpi-app/backend/app/app-config-skeleton.toml`. It looks like this

```toml
cors_origins = []

[database]
dialect=
user=
password=
server_url=
name=
port=
```


3. Rename your configuration because the application is looking for a specific name.

```shell
export app_root="openshift-kpi-app/backend/app/"
mv "$app_root/app-config-skeleton.toml" "$app_root/ocp-kpi-web.toml"
```



## Insert Simulated Data

Prerequisites:

- a configured OpenShift KPI web api
- activated project Python environment
- a [SQL database supported by SQLAlchemy](https://www.sqlalchemy.org/features.html#Supported-Databases) in ready state
- your terminal current working directory is `openshift-kpi-app/backend/app`

```shell
    export PYTHONPATH=$(pwd)
    python scripts/insert_simdata.py
```