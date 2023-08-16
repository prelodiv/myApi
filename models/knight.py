from config.database import Base
from sqlalchemy import Column, Integer,String
class knight(Base):
    __tablename__ = "knights"

    id = Column(Integer, primary_key = True)
    name = Column(String )
    history = Column(String )
    kingdom = Column(String )
    age = Column(Integer)