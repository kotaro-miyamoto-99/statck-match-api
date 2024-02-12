from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    Date,
    Float,
    Enum,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum


class IndustryChoices(PyEnum):
    FIN = "FIN"  # 金融
    HC = "HC"  # ヘルスケア
    MANU = "MANU"  # 製造業
    RETAIL = "RETAIL"  # 小売
    EDU = "EDU"  # 教育
    CONS = "CONS"  # 建設
    TRANS = "TRANS"  # 交通
    ENER = "ENER"  # エネルギー
    AGRI = "AGRI"  # 農業
    ENT = "ENT"  # エンターテイメント
    FOOD = "FOOD"  # 飲食業
    REAL = "REAL"  # 不動産
    TELE = "TELE"  # 通信
    PHAR = "PHAR"  # 製薬
    AUTO = "AUTO"  # 自動車
    AERO = "AERO"  # 航空宇宙
    CHEM = "CHEM"  # 化学
    INSU = "INSU"  # 保険
    IT = "IT"  # ITサービス
    HR = "HR"  # 人材
    MEDICAL = "MEDICAL"  # 医療


Base = declarative_base()


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    description = Column(Text, nullable=True)
    industry = Column(Enum(IndustryChoices), nullable=False)
    established_year = Column(Date, nullable=True)
    headquarters = Column(String(255), nullable=True)
    website_url = Column(String, nullable=True)
    number_of_employees = Column(Integer, nullable=True)
    capital = Column(Float, nullable=True)
    logo = Column(String, nullable=True)


class TempCompany(Base):
    __tablename__ = "temp_companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    description = Column(Text, nullable=True)
    industry = Column(Enum(IndustryChoices), nullable=False)
    established_year = Column(Date, nullable=True)
    headquarters = Column(String(255), nullable=True)
    website_url = Column(String, nullable=True)
    number_of_employees = Column(Integer, nullable=True)
    capital = Column(Float, nullable=True)
    # SQLAlchemyではImageFieldに相当するフィールドがないため、ファイルパスを保存するStringフィールドを使用
    logo = Column(String, nullable=True)
    is_approved = Column(Boolean, default=False)


class Technology(Base):
    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    icon = Column(String, nullable=True)


class CompanyTechnology(Base):
    __tablename__ = "company_technologies"
    company_id = Column(Integer, ForeignKey("companies.id"), primary_key=True)
    technology_id = Column(
        Integer, ForeignKey("technologies.id"), primary_key=True
    )

    # Relationship to access the Company and Technology from CompanyTechnology instances
    company = relationship("Company", back_populates="technologies")
    technology = relationship("Technology", back_populates="companies")


Company.technologies = relationship(
    "CompanyTechnology", back_populates="company"
)
Technology.companies = relationship(
    "CompanyTechnology", back_populates="technology"
)
