from fastapi import FastAPI
# from typing import List
from src.models.model import Model, ReadModel

from cassandra.cluster import Cluster, dict_factory

cluster = Cluster(port=9042)
session = cluster.connect('agro_gwtsas')  # 'data' is the database name
session.row_factory = dict_factory

app = FastAPI()


@app.get("/health")
async def health():
    """
    Make sur your API is running
    """
    return {"detail": "All good!"}

# -> List[ReadModel]


@app.get("/models")
async def get_model():
    """
    Return all models
    """
    items = []
    rows = session.execute("SELECT * FROM model;")
    for row in rows:
        items.append(
            ReadModel(
                id=str(row['id']),
                t_ext=row['t_ext'],
                t_suelo=row['t_suelo'],
                h_ext=row['h_ext'],
                h_suelo=row['h_suelo'],
                luz=row['luz'],
                bateria=row['bateria'],
                v_ent=row['v_ent']
            )
        )
    data = {'items': items}

    return data


@app.post("/model")
async def post_model(item: Model):
    """
    Add a new model in the table
    """
    data_dict = item.__dict__
    print(data_dict)
    returned_value = session.execute(
        """
            INSERT INTO model (
                id,
                t_ext,
                t_suelo,
                h_ext,
                h_suelo,
                luz,
                bateria,
                v_ent,
                date
            ) VALUES (
                {id},
                {t_ext},
                {t_suelo},
                {h_ext},
                {h_suelo},
                {luz},
                {bateria},
                {v_ent},
                toTimestamp(now())
            );""".format(
            **data_dict)
    )
    return {'detail': "model has been added"}


@app.put("/model")
async def put_model(item: Model):
    """
    Update model in the table
    """
    returned_value = session.execute(
        """
        UPDATE model
        SET 
            t_ext={t_ext},
            t_suelo={t_suelo},
            h_ext={h_ext},
            h_suelo={h_suelo},
            luz={luz},
            bateria={bateria},
            v_ent={v_ent}
        WHERE id={id};
        """.format(**item.__dict__)
    )
    return {'detail': "model has been updated"}
