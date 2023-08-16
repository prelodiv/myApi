from pydantic import BaseModel
from typing import Optional, List


class Knight(BaseModel):
     id : Optional[int] = None
     name : str
     history : str
     kingdom :str
     age :int 