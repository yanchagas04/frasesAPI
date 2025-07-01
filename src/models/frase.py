from pydantic import BaseModel
from datetime import datetime

class Frase(BaseModel):
    id: int
    frase: str
    autor: str
    data: datetime