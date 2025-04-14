from fastapi import APIRouter, HTTPException
from typing import List
from models import CUSTOMERS, Customer

router = APIRouter()

# Routes
'''
This end point is used to on-board a new customer into out Banking App

'''
@router.post("/create", response_model=Customer)
def create_customer(customer: Customer):
    # Check if the customer ID already exists
    if any(c.id == customer.id for c in CUSTOMERS):
        raise HTTPException(status_code=400, detail="Customer with this ID already exists.")
    # Add new customer
    CUSTOMERS.append(customer)
    return customer

# @router.get("/", response_model=List[Customer])
# def get_all_customers():
#     return CUSTOMERS
