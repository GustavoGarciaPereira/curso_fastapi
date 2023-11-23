from main_project.contrib.models import BaseModel
from datetime import datetime
from sqlalchemy import String, Integer, Float, ForeignKey, Datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import UUID, uuid4


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    # Chave primária como UUID
    pk_id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)

    # Outros campos
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(Datetime, nullable=False)
    centro_treinamento_id: Mapped[int] = mapped_column(Integer, ForeignKey('centros_treinamento.pk_id'), nullable=False)
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey('categorias.pk_id'), nullable=False)

    # Relações (opcional)
    centro_treinamento = relationship("CentroTreinamentoModel", back_populates="atletas")
    categoria = relationship("CategoriaModel", back_populates="atletas")
