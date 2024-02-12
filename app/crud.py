# crud.py
from sqlalchemy.orm import Session
from . import models


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()
