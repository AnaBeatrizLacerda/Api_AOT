# Importa os modelos Pydantic e cria a instância principal da aplicação FastAPI
from models import *
import json
from fastapi import FastAPI, HTTPException
app = FastAPI()


# Variáveis globais
# Listas globais que vão guardar os dados carregados na inicialização da API
personagens: list[Personagem] = []
titas: list[Tita] = []
esquadroes: list[Esquadrao] = []


# Evento startup usando decorador
# Roda uma única vez quando a API sobe, carregando os JSONs para as listas globais
@app.on_event("startup")
def carregar_dados_iniciais():
    global personagens
    global titas
    global esquadroes
    personagens = carregar_personagens()
    titas = carregar_titas()
    esquadroes = carregar_esquadroes()


#Funções de carregamento (as três: personagens, titãs, esquadrões)
# Cada função abre seu respectivo JSON, converte cada item em objeto Pydantic e devolve a lista pronta
def carregar_personagens():
    with open("json/personagens.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        resultado = []

        for dados_personagem in dados:
            novo_personagem= Personagem(**dados_personagem)
            resultado.append(novo_personagem)
    return resultado

def carregar_titas():
    with open("json/titas.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        resultado = []

        for dados_tita in dados:
            novo_tita= Tita(**dados_tita)
            resultado.append(novo_tita)
    return resultado

def carregar_esquadroes():
    with open("json/esquadroes.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        resultado = []

        for dados_esquadrao in dados:
            novo_esquadrao= Esquadrao(**dados_esquadrao)
            resultado.append(novo_esquadrao)
    return resultado


# # Rotas GET de listagem (/personagens, /titas, /esquadroes)
# # Rotas que devolvem a lista completa de cada entidade, já carregada em memória
# @app.get("/personagens")
# def listar_personagens():
#     return personagens

# @app.get("/titas")
# def listar_titas():
#     return titas

# @app.get("/esquadroes")
# def listar_esquadroes():
#     return esquadroes


# # Rotas GET por id (/personagens/{id}, /titas/{id}, /esquadroes/{id})
# @app.get("/personagens/{id}")
# async def get_personagem(id: int):
#     for personagem in personagens:
#         if personagem.id == id:
#             return personagem
#     raise HTTPException(status_code=404, detail="Personagem não encontrado")

# @app.get("/titas/{id}")
# async def get_titas(id : int):
#     for tita in titas:
#         if tita.id == id:
#             return tita
#     raise HTTPException(status_code=404, detail="Titã  não encontrado")

# @app.get("/esquadroes/{id}")
# async def get_esquadrao(id : int):
#     for esquadrao in esquadroes:
#         if esquadrao.id == id:
#             return esquadrao
#     raise HTTPException(status_code=404, detail="Esquadrão não encontrado")


# # Rota relacional  
# # Busca o personagem pelo id, confirma se ele é titã-mudante, e então busca o titã associado a ele
# @app.get("/personagens/{id}/tita")
# async def get_tita_do_personagem(id: int):
#     personagem = await get_personagem(id)
#     if personagem.e_tita_mudante == False:
#         raise HTTPException(status_code=404, detail="Personagem não possui titã")
#     for tita in titas:
#         if tita.personagem_associado == id:
#             return tita
#     raise HTTPException(status_code=404, detail="Titã não encontrado")


# # Método Post
# # Recebe os dados no corpo da requisição, gera um novo id automaticamente e adiciona o item na lista global
# @app.post("/personagens")
# async def post_personagem(personagem : Personagem):
#     personagem_dic = personagem.model_dump()
#     personagem_dic["id"] = len(personagens) + 1
#     novo_personagem = Personagem(**personagem_dic)
#     personagens.append(novo_personagem)
#     return novo_personagem

# @app.post("/titas")
# async def post_tita(tita : Tita):
#     tita_dic = tita.model_dump()
#     tita_dic["id"] = len(titas) + 1
#     novo_tita = Tita(**tita_dic)
#     titas.append(novo_tita)
#     return novo_tita
    

# @app.post("/esquadroes")
# async def post_esquadrao(esquadrao : Esquadrao):
#     esquadrao_dic = esquadrao.model_dump()
#     esquadrao_dic["id"] = len(esquadroes) + 1
#     novo_esquadrao = Esquadrao(**esquadrao_dic)
#     esquadroes.append(novo_esquadrao)
#     return novo_esquadrao


# # Método Put
# @app.put("/personagens/{id}")
# async def put_personagem(id: int, dados_atualizados: Personagem):
#     for index, personagem in enumerate(personagens):
#         if personagem.id == id:
#             dados_dic = dados_atualizados.model_dump()
#             dados_dic["id"] = id
#             personagens[index] = Personagem(**dados_dic)
#             return personagens[index]
#     raise HTTPException(status_code=404, detail="Personagem não encontrado")


# @app.put("/titas/{id}")
# async def put_tita(id: int, dados_atualizados: Tita):
#     for index, tita in enumerate(titas):
#         if tita.id == id:
#             dados_dic = dados_atualizados.model_dump()
#             dados_dic["id"] = id
#             titas[index] = Tita(**dados_dic)
#             return titas[index]
#     raise HTTPException(status_code=404, detail="Titã não encontrado")

# @app.put("/esquadroes/{id}")
# async def put_esquadrao(id: int, dados_atualizados: Esquadrao):
#     for index, esquadrao in enumerate(esquadroes):
#         if esquadrao.id == id:
#             dados_dic = dados_atualizados.model_dump()
#             dados_dic["id"] = id
#             esquadroes[index] = Esquadrao(**dados_dic)
#             return esquadroes[index]
#     raise HTTPException(status_code=404, detail="Esquadrão não encontrado")

# # Método Delete
# @app.delete("/personagens/{id}")
# async def delete_personagem(id: int):
#     for index, personagem in enumerate(personagens):
#         if personagem.id == id:
#             personagens.pop(index)
#             return {"mensagem": "Personagem removido com sucesso"}
#     raise HTTPException(status_code=404, detail="Personagem não encontrado")

# @app.delete("/titas/{id}")
# async def delete_tita(id: int):
#     for index, tita  in enumerate(titas):
#         if tita.id == id:
#             titas.pop(index)
#             return {"mensagem": "Titãs removido com sucesso"}
#     raise HTTPException(status_code=404, detail="Titã não encontrado")

# @app.delete("/esquadroes/{id}")
# async def delete_esquadrao(id: int):
#     for index, esquadrao in enumerate(esquadroes):
#         if esquadrao.id == id:
#             esquadroes.pop(index)
#             return {"mensagem" : "Esquadrão removido com sucesso"}
#     raise HTTPException(status_code=404, detail="Esquadrão não encontrado")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Conectando com SQLModel
from typing import Annotated
from fastapi import Query
from sqlmodel import select
from fastapi import HTTPException

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

#Personagens 
@app.get('/personagem/')
async def get_personagem(
    session: SessionDepence,
    offset: int =0,
    limit: Annotated[int, Query(le=100)] = 100
) -> list[Personagem]:
    personagens = session.exec(select(Personagem).offset(offset).limit(limit)).all()
    return personagens
 
 
@app.get('/personagem/{personagem_id}')
async def get_personagem(personagem_id : int, session: SessionDepence) -> Personagem:
    personagem = session.get(Personagem, personagem_id)
    if not personagem:
        raise HTTPException(status_code=404, detail="Personagem não encontrada")
    return personagem
 
 
@app.post('/personagem/')
async def post_personagem(personagem: Personagem, session: SessionDepence) -> Personagem:
    session.add(personagem)
    session.commit()
    session.refresh(personagem)
    return personagem


@app.patch("/personagem/{personagem_id}", response_model=Personagem)
def update_personagem(personagem_id: int, hero: Personagem, session: SessionDepence):
    personagem_db = session.get(Personagem, personagem_id)
    if not personagem_db:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
        
    personagem_data = hero.model_dump(exclude_unset=True)
    personagem_db.sqlmodel_update(personagem_data)
    
    session.add(personagem_db)
    session.commit()
    session.refresh(personagem_db)
    return personagem_db

 
@app.delete('/personagem/{personagem_id}')
async def delete_personagem(personagem_id: int, session: SessionDepence):
    personagem = session.get(Personagem, personagem_id)
    if not personagem:
        raise HTTPException(status_code=404, detail="personagem não encontrada")
    session.delete(personagem)
    session.commit()
    return {"Delete" : True}
 
 
#Titãs
@app.get('/tita/')
async def get_tita(
    session: SessionDepence,
    offset: int =0,
    limit: Annotated[int, Query(le=100)] = 100
) -> list[Tita]:
    titas = session.exec(select(Tita).offset(offset).limit(limit)).all()
    return titas

@app.get('/tita/{tita_id}')
async def get_tita(tita_id : int, session: SessionDepence) -> Tita:
    tita = session.get(Tita, tita_id)
    if not tita:
        raise HTTPException(status_code=404, detail="Titã não encontrada")
    return tita
 
 
@app.post('/tita/')
async def post_tita(tita: Tita, session: SessionDepence) -> Tita:
    session.add(tita)
    session.commit()
    session.refresh(tita)
    return tita

@app.patch("/tita/{tita_id}", response_model=Tita)
def update_tita(tita_id: int, hero: Tita, session: SessionDepence):
    tita_db = session.get(Tita, tita_id)
    if not tita_db:
        raise HTTPException(status_code=404, detail="Titã não encontrado")
        
    tita_data = hero.model_dump(exclude_unset=True)
    tita_db.sqlmodel_update(tita_data)
    
    session.add(tita_db)
    session.commit()
    session.refresh(tita_db)
    return tita_db
 
 
@app.delete('/tita/{tita_id}')
async def delete_tita(tita_id: int, session: SessionDepence):
    tita = session.get(Tita, tita_id)
    if not tita:
        raise HTTPException(status_code=404, detail="Tita não encontrada")
    session.delete(tita)
    session.commit()
    return {"Delete" : True}

#Esquadrão
@app.get('/esquadrao/')
async def get_esquadrao(
    session:SessionDepence,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100 
) -> list[Esquadrao]:
    esquadroes = session.exec(select(Esquadrao).offset(offset).limit(limit)).all()
    return esquadroes

@app.get('/esquadrao/{esquadrao_id}')
async def get_esquadrao(esquadrao_id: int, session: SessionDepence) -> Esquadrao:
    esquadrao = session.get(Esquadrao, esquadrao_id)
    if not esquadrao:
        raise HTTPException(status_code = 404, detail= "Esquadrão não encontrado")
    return esquadrao

@app.post('/esquadrao/')
async def post_esquadrao(esquadrao: Esquadrao, session: SessionDepence) -> Esquadrao:
    session.add(esquadrao)
    session.commit()
    session.refresh(esquadrao)
    return esquadrao


@app.patch("/esquadrao/{esquadrao_id}", response_model=Esquadrao)
def update_esquadrao(esquadrao_id: int, hero: Esquadrao, session: SessionDepence):
    esquadrao_db = session.get(Esquadrao, esquadrao_id)
    if not esquadrao_db:
        raise HTTPException(status_code=404, detail="Esquadrão não encontrado")
        
    esquadrao_data = hero.model_dump(exclude_unset=True)
    esquadrao_db.sqlmodel_update(esquadrao_data)
    
    session.add(esquadrao_db)
    session.commit()
    session.refresh(esquadrao_db)
    return esquadrao_db




@app.delete('/esquadrao/{esquadrao_id}')
async def delete_esquedrao(esquadrao_id: int, session: SessionDepence):
    esquadrao = session.get(Esquadrao, esquadrao_id)
    if not esquadrao:
        raise HTTPException(status_code=404, detail="Esquadrão não encontrado")
    session.delete(esquadrao)
    session.commit()
    return {"Delete" : True}

