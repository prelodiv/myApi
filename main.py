from fastapi import  FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
from config.database import engine,Base


from middlewares.error_handler import ErrorHandler

from routers.dragon import dragon_router
from routers.knight import knight_router
from routers.user import user_router
app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(dragon_router)
app.include_router(knight_router)
app.include_router(user_router)
Base.metadata.create_all(bind = engine)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")




    

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')




