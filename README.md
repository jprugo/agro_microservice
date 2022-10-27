# cassandra-fastapi

## Installation

Then installation through pip and virtual-env is recommended:

```bash
pip install -r requirements.txt
```

Once dependencies installed, make sure to have running cassandra in docker with the following instruction:

```bash
docker compose up -d
CASSANDRA=$(docker container ls | grep 'cassandra_1' | awk '{print $1}')
```

Then we have to create some objects in the cluster to continue with these steps:

```bash
docker cp setup.cql $CASSANDRA:/
docker exec -it $CASSANDRA cqlsh -f setup.cql
docker exec -it $CASSANDRA cqlsh -e 'expand on; SELECT * FROM agro_gwtsas.model limit 30'
```

Finally, lunch the FastAPI app:

```bash
uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
```

All good !

## You can check the OpenApi document using:

Check http://127.0.0.1:8000/docs in your web browser.
