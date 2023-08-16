from fastapi import APIRouter

from fastapi.responses import JSONResponse

from typing import Optional, List


from config.database import Session
from models.dragon import dragon as Dragon_model

from fastapi.encoders import jsonable_encoder

from services.dragon import dragonService
from schemas.dragon import Dragon

dragon_router =APIRouter()



@dragon_router.get('/Dragon', tags=['Dragon'], response_model=List[Dragon], status_code=200)
def get_dragon() -> List[Dragon]:
    db = Session()
    result = dragonService(db).get_dragon()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dragon_router.post('/Dragon', tags=['Dragon'], response_model=dict, status_code=201)
def create_dragon(dragon: Dragon) -> dict:
    db = Session()
    dragonService(db).create_dragon(dragon)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el dragon"})


@dragon_router.put('/Dragon/{id}', tags=['Dragon'], response_model=dict, status_code=200)
def update_dragon(id: int, dragon: Dragon)-> dict:
    db = Session()
    dragonService(db).update_dragon(id,dragon)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el dragon"})


@dragon_router.delete('/Dragon/{id}', tags=['Dragon'], response_model=dict, status_code=200)
def delete_dragon(id: int)-> dict:
    db = Session()
    dragonService(db).delete_dragon(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el caballero"})