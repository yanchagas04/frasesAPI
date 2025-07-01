from fastapi import APIRouter

frase_router = APIRouter(
    prefix="/frase",
    tags=["Frase"],
)

@frase_router.get("/")
async def frase_aleatoria():
    pass #frase aleatoria

@frase_router.get("/{id}")
async def frase_por_id(id: int):
    pass #frase por id

@frase_router.get("/autor/{autor}")
async def frases_por_autor(autor: str):
    pass #frases por autor

@frase_router.get("/data/{data}")
async def frases_por_data(data: str):
    pass #frases por data