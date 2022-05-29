from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic

from app.database.database import SessionLocal, engine
from app.models import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/api/v2/docs",
              redoc_url="/api/v2/redocs",
              title="TKV API",
              description="API to open a new 'current account' of already existing customers.",
              version="2.0",
              openapi_url="/api/v2/openapi.json",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

security = HTTPBasic()


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


from app.controllers import routes
