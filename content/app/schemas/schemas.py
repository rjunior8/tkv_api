from pydantic import BaseModel
from typing import List


class AddCustomersReq(BaseModel):
    name: str
    surname: str


class AddAccReq(BaseModel):
    customer_id: int
    initial_credit: float
    
    
class CustomersInfoReq(BaseModel):
    customer_id: int
    
    
class CustomersInfoRes(BaseModel):
    name: str
    surname: str
    balance: float
    transactions: List[float]


class Customers(BaseModel):
    id: int
    name: str
    surname: int

    class Config:
        orm_mode = True


class Accounts(BaseModel):
    id: int
    transaction: float
    owner: int

    class Config:
        orm_mode = True
