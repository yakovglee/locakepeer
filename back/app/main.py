import uvicorn
from fastapi import FastAPI

from db.schemas import InfoSpot
from db import db

app = FastAPI()


@app.get("/")
def heloo():
    return {'data': db.session.get_all_records()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)