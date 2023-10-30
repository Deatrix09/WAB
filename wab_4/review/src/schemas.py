from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PostReview(BaseModel):
    coffee_shop_id: UUID
    user_id: UUID
    start: int
    descriptin: str
    
    
class Review(BaseModel):
    review_id: UUID
    coffee_shop_id: UUID
    user_id: UUID
    start: int
    descriptin: str 
    created: datetime