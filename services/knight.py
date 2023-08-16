from models.knight import knight as knight_model
from schemas.knight import Knight
class knightService():

    def __init__(self,db) -> None:
        self.db = db 

    def get_knight(self):
        result = self.db.query(knight_model).all()
        return result
    
    def create_knight(self,knight: Knight):
        new_knight = knight_model(**knight.dict())
        self.db.add(new_knight)
        self.db.commit()
        return  
    def update_knight(self, id: int, knight:Knight):
        result =   self.db.query(knight_model).filter(knight_model.id ==id).first()
        result.name = knight.name   
        result.history = knight.history
        result.kingdom = knight.kingdom
        result.age = knight.age
  
        self.db.commit()
        return
    def delete_knight(self,id:int):
           self.db.query(knight_model).filter(knight_model.id ==id).delete()
           self.db.commit()
           return