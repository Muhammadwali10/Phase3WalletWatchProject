from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)  # 'income' or 'expense'
    amount = Column(Float, nullable=False)
    description = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)
