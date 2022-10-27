from pydantic import BaseModel

class Model(BaseModel):
    id: int = ...
    t_ext: float
    t_suelo: float
    h_ext: float
    h_suelo: float
    luz: float
    bateria: bool
    v_ent: float


class ReadModel(Model):
    date: str