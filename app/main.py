from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/companies/", response_model=list[schemas.Company])
def read_companies(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies
