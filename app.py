import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Strona z programems"}


@app.get("/get_random_number")
def get_random_number():
    # Generuj losową liczbę
    random_number = random.randint(1, 100)
    return {"random_number": random_number}
