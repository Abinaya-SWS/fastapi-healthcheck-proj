from fastapi import FastAPI

from app.database.connection import Base, engine
from app.models.user import User
from app.routes.health import router as health_router
from app.routes.users import router as users_router


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(health_router)
app.include_router(users_router)from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import Base, engine
from app.models.user import User
from app.routes.health import router as health_router
from app.routes.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        Base.metadata.create_all(bind=engine)

        print("Database connection: OK")
        print("FastAPI server started")

    except Exception as error:
        print(f"Database connection: FAILED - {error}")
        raise

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health_router)
app.include_router(users_router)