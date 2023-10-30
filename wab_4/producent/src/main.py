from fastapi import FastAPI
from .rabbitmq import publish

app = FastAPI()



@app.get("/")
def read_root(name: str = "World"):
    msg = f"Hello {name}"
    publish(msg)
    return msg

