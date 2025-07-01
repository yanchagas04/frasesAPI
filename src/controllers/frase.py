from lib.prisma.client import Prisma
from src.models.frase import Frase, FraseResponse
from src.models.error import ErrorResponse
from lib.prisma.errors import MissingRequiredValueError
from fastapi import status

prisma = Prisma()

async def frase_por_id(id: int) -> FraseResponse | ErrorResponse:
    try:
        frase : Frase = await prisma.frase.find_unique(where={'id': id})
        if frase:
            return FraseResponse(
                status = status.HTTP_200_OK,
                frase = frase
            )
        else:
            return ErrorResponse(
                status = status.HTTP_404_NOT_FOUND,
                message = 'Frase não encontrada'
            )
    except MissingRequiredValueError:
        return ErrorResponse(
            status = status.HTTP_400_BAD_REQUEST,
            message = 'O id da frase é obrigatório'
        )
    except Exception as e:
        return ErrorResponse(
            status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            message = str(e)
        )