from fastapi import FastAPI
from .rabbitmq import publish
from .schemas import *
from . import schemas, crud,database


app = FastAPI()



@app.post("/review")
def create_review(request: schemas.PostReview) -> schemas.Review:
    review =  crud.insert_review(request)
    return schemas.Review(**review.dict())

