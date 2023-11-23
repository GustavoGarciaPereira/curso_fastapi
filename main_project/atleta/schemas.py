from pydantic import BaseModel, Field
from typing import Annotated

class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta", example="Gustavo", max_length=100)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="123.456.789-00", regex="^\d{3}\.\d{3}\.\d{3}-\d{2}$")]
    idade: Annotated[int, Field(description="Idade do atleta", example=25, gt=0, le=100)]
    peso: Annotated[float, Field(description="Peso do atleta em kg", example=70.5, gt=0)]
    altura: Annotated[float, Field(description="Altura do atleta em metros", example=1.75, gt=0)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    centro_treinamento_id: Annotated[int, Field(description="ID do centro de treinamento", example=1)]
    categoria_id: Annotated[int, Field(description="ID da categoria do atleta", example=2)]
