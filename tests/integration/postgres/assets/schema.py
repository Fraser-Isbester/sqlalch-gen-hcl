from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    CheckConstraint,
    ForeignKey,
)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    full_name = Column(String)
    age = Column(Integer)

    check_age_positive = CheckConstraint(age > 0)
    check_age_reasonable = CheckConstraint(age < 200)


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    account_created_at = Column(DateTime, nullable=False)
