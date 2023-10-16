from typing import Union

from fastapi import FastAPI
from schema import Pet
from uuid import UUID

app = FastAPI()


@app.post("/pet", status_code=201)
def post_pet(
    pet: Pet
) -> Pet:
    pass


@app.get("/pets", status_code=201)
def get_pets(
    skip: int = 0,
    limit: int = 20,
    order: str | None = None
) -> list[Pet]:
    pass


@app.get("/pet/{pet_id}")
def get_pet(pet_id: UUID) -> list[Pet]:
    pass


@app.put("/pet/{pet_id}", status_code=202)
def put_pet(
    pet_id: UUID,
    pet: Pet
) -> Pet:
    pass


@app.delete("/pet/{pet_id}")
def get_pet(
    pet_id: UUID,
) -> UUID:
    pass
