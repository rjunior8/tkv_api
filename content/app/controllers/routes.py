from fastapi import Depends
from fastapi.openapi.docs import get_swagger_ui_html
from sqlalchemy.orm import Session

import time
from typing import List

from app import app, get_db
from app.models import models
from app.schemas import schemas


@app.get("/")
@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/api/v2/openapi.json",
        title="TKV API",
        swagger_favicon_url="https://www.tekever.com/wp-content/uploads/2021/06/cropped-favicon-32x32.png")
    
    
@app.post("/add-customer")
async def add_customer(data: schemas.AddCustomersReq, db: Session = Depends(get_db)):
    
    new_customer = models.Customers()
    new_customer.name = data.name
    new_customer.surname = data.surname
    
    db.add(new_customer)
    db.commit()
    
    res = {
        "msg": "Customer created successfully!",
    }
    
    return JSONResponse(content=res, status_code=200)


@app.post("/add-acc")
async def add_acc(data: schemas.AddAccReq, db: Session = Depends(get_db)):
    
    customer = db.query(models.Customers).filter(models.Customers.id == data.customer_id).first()
    
    if customer:
        new_acc = models.Accounts()
        new_acc.transaction = float(data.initial_credit)    
        new_acc.owner = customer.id
        
        db.add(new_acc)
        db.commit()
        
        res = {
            "msg": "Account created successfully!",
        }
        
        return JSONResponse(content=res, status_code=200)
    
    return JSONResponse(content={"msg": "Customer NOT exists!"}, status_code=200)


@app.post("/customer-info", response_model=schemas.CustomersInfoRes)
async def customer_info(data: schemas.CustomersInfoReq, db: Session = Depends(get_db)):
    
    customer = db.query(models.Customers).filter(models.Customers.id == data.customer_id).first()
    
    if customer:
    
        transactions = db.query(
            models.Accounts.transaction).filter(models.Accounts.owner == user.id).all()
        
        transactions = [i[0] for i in transactions if i[0] != 0]
        balance = sum(transactions)
        
        return schemas.CustomersInfoRes(name=customer.name,
                                        surname=customer.surname,
                                        balance=balance,
                                        transactions=transactions)
        
    return JSONResponse(content={"msg": "Customer NOT exists!"}, status_code=200)
