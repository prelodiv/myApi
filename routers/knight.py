from fastapi import APIRouter

from fastapi.responses import  JSONResponse

from typing import Optional, List


from config.database import Session

from models.knight import knight as knight_model
from fastapi.encoders import jsonable_encoder
from services.knight import knightService
from schemas.knight import Knight


knight_router =APIRouter()




@knight_router.get('/knight', tags=['knight'], response_model=List[Knight], status_code=200)
def get_knight() -> List[Knight]:
    db = Session()
    result = knightService(db).get_knight()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



   
    

@knight_router.post('/knight', tags=['knight'], response_model=dict, status_code=201)
def create_knight(knight: Knight) -> dict:
    db = Session()
    knightService(db).create_knight(knight)
   
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el caballero"})



@knight_router.put('/knight/{id}', tags=['knight'], response_model=dict, status_code=200)
def update_knight(id: int, knight: Knight)-> dict:
    db = Session()
    knightService(db).update_knight(id,knight)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el caballero"})



@knight_router.delete('/Knight/{id}', tags=['knight'], response_model=dict, status_code=200)
def delete_knight(id: int)-> dict:
    db = Session()
    knightService(db).delete_knight(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el caballero"})