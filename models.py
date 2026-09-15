from sqlmodel import Field, SQLModel, Relationship, create_engine, Session
from typing import Optional, List, Annotated
from fastapi import Depends


class Personagem(SQLModel, table=True):
    id : int | None = Field(default = None, primary_key = True)
    __tablename__ = "personagem"
    __table_args__ = {"extend_existing": True} 
    nome: str = Field(index = True)
    esquadrao: str = Field(index = True)
    e_tita_mudante : bool= Field(index = True)
    instrutor : str = Field(index = True)
    tita: Optional["Tita"] = Relationship(back_populates="personagem")

class Tita(SQLModel, table=True):
    id : int | None = Field(default = None, primary_key = True)
    __tablename__ = "tita"
    __table_args__ = {"extend_existing": True} 
    tipo: str = Field(index = True)
    altura_metros: float = Field(index = True)
    personagem_associado: Optional[int] = Field(default=None, foreign_key="personagem.id")
    personagem: Optional[Personagem] = Relationship(back_populates="tita")


class Esquadrao(SQLModel, table=True):
    id : int | None = Field(default = None, primary_key = True)
    __tablename__ = "esquadrao"
    __table_args__ = {"extend_existing": True} 
    nome: str = Field(index = True)
    lider: str = Field(index = True)


sqlite_file_name = "ets.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDepence = Annotated[Session, Depends(get_session)]
