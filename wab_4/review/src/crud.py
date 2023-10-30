from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import uuid

from . import models, schemas


def insert_review(db: Session, review: schemas.PostReview) -> models.Review:
    db_review = models.Review(id=uuid.uuid4,**review.dict())
    
    db.add(review)
    db.commit()
    db.refresh(db_review)
    return db_review