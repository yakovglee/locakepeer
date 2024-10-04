import uvicorn
from fastapi import FastAPI
from back.app.core.config import settings

from db import db

app = FastAPI()


@app.get("/")
def heloo():
    return {'data': db.session.get_all_records()}


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.FASTApi.host, port=settings.FASTApi.port, reload=True)