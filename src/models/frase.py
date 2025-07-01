from pydantic import BaseModel
from datetime import datetime

class Frase(BaseModel):
    id: int
    texto: str
    autor: str
    data: datetime

class FraseCreateEdit(BaseModel):
    frase: str
    autor: str

class FraseResponse(BaseModel):
    status: str
    frase: Frase | None