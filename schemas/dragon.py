from pydantic import BaseModel
from typing import Optional, List
class Dragon(BaseModel):
    id : Optional[int] = None
    name: str 
    color: str  
    kingdom: str 
    flame: bool  