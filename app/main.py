from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
# CORSを許可するオリジンのリスト
origins = [
    "http://localhost:3000",  # Next.jsアプリが動作しているオリジン
    "https://stack-match.vercel.app",  # 本番環境のオリジン
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 全てのオリジンを許可する場合は ["*"] を使用
    allow_credentials=True,
    allow_methods=[
        "*"
    ],  # 特定のHTTPメソッドのみを許可する場合は ["GET", "POST"] などを指定
    allow_headers=["*"],  # 特定のヘッダのみを許可する場合は指定
)


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
