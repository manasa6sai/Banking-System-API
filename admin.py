from fastapi import APIRouter
from typing import List
from models import CUSTOMERS, ACCOUNTS, TRANSFERS, Customer, Account, Transfer

router = APIRouter()

# Welcome message for admin
@router.get("/")
def welcome():
    return {"message": "Welcome to the Banking API Admin Dashboard. Access /docs for detailed documentation."}

# Get all customers
@router.get("/customers", response_model=List[Customer])
def get_all_customers():
    return CUSTOMERS

# Get all accounts
@router.get("/accounts", response_model=List[Account])
def get_all_accounts():
    return ACCOUNTS

# Get all transfers
@router.get("/transfers", response_model=List[Transfer])
def get_all_transfers():
    return TRANSFERS
