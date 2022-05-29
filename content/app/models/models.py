from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Customers(Base):
    
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    
    account = relationship("Accounts")
    
    
class Accounts(Base):
    
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    transaction = Column(Float)
    owner = Column(Integer, ForeignKey("customers.id"), nullable=False)
