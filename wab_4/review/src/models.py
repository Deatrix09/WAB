from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from uuid import UUID



from .database import Base


class CoffeeShop(Base):
    __tablename__ = "coffee_shops"
    
    id = Column(UUID, primary_key = True, index= True)
    
    
class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(UUID, primary_key = True, index= True)
    coffee_shop = Column(UUID)
    user_id = Column(UUID)
    rating = Column(Integer)
    description = Column(String)
    created = Column(DateTime)