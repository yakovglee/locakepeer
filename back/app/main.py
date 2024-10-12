import uvicorn
from fastapi import FastAPI

from core.config import settings


from src import routers


app = FastAPI()

app.include_router(routers)


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=settings.FASTApi.host, port=settings.FASTApi.port, reload=True
    )
