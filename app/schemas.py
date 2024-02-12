from typing import Optional, List
from pydantic import BaseModel
import datetime


# Companyモデルの基本クラス
class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None
    industry: str
    established_year: Optional[datetime.date] = None
    headquarters: Optional[str] = None
    website_url: Optional[str] = None
    number_of_employees: Optional[int] = None
    capital: Optional[float] = None
    logo: Optional[str] = None


# Companyを作成する際に使用するクラス（POSTリクエスト）
class CompanyCreate(CompanyBase):
    pass


# Companyを更新する際に使用するクラス（PUTリクエスト）
class CompanyUpdate(CompanyBase):
    pass


# データベースから読み込んだCompanyデータをクライアントに返す際に使用するクラス
class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True
