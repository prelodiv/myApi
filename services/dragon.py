from models.dragon import dragon as Dragon_model
from schemas.dragon import Dragon
class dragonService():

    def __init__(self,db) -> None:
        self.db = db 

    def get_dragon(self):
        result = self.db.query(Dragon_model).all()
        return result
    
    def create_dragon(self,dragon: Dragon):
        new_dragon = Dragon_model(**dragon.dict())
        self.db.add(new_dragon)
        self.db.commit()
        return
    def update_dragon(self, id: int, dragon:Dragon):
        result =   self.db.query(Dragon_model).filter(Dragon_model.id ==id).first()
        result.name = dragon.name   
        result.color = dragon.color
        result.kingdom = dragon.kingdom
        result.flame = dragon.flame
        self.db.commit()
        return
    def delete_dragon(self, id: int):
            self.db.query(Dragon_model).filter(Dragon_model.id ==id).delete()
       
            self.db.commit()
            return