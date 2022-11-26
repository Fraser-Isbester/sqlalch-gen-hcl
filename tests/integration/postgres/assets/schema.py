from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    # Feat: Primary Key
    id = Column(Integer, primary_key=True)

    # Feat: Column Types
    name = Column(String(30))
    full_name = Column(String)
    age = Column(Integer)

    # Feat: Check Constraints
    check_age_positive = CheckConstraint(age > 0)
    check_age_reasonable = CheckConstraint(age < 200)


class Account(Base):
    __tablename__ = "account"

    # Feat: Primary Key
    id = Column(Integer, primary_key=True)

    # Feat: Column Types, Foreign Keys
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    account_created_at = Column(DateTime, nullable=False)
