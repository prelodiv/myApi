from config.database import Base
from sqlalchemy import Column, Integer,String,Boolean
class dragon(Base):
    __tablename__ = "dragons"

    id = Column(Integer, primary_key = True)
    name = Column(String )
    color = Column(String )
    kingdom = Column(String )
    flame =  Column(Boolean )