from typing import List
from datetime import datetime
from pydantic import BaseModel

# Models
class Customer(BaseModel):
    id: int
    name: str

class Account(BaseModel):
    account_id: int
    customer_id: int
    balance: float

class Transfer(BaseModel):
    transfer_id: int
    source_account: int
    destination_account: int
    amount: float
    transfer_time: datetime

class NewAccountRequest(BaseModel):
    customer_id: int
    customer_name: str
    initial_deposit: float

class TransferRequest(BaseModel):
    source_account: int
    destination_account: int
    amount: float

# Pre-populated data
CUSTOMERS: List[Customer] = [
    Customer(id=1, name="Arisha Barron"),
    Customer(id=2, name="Branden Gibson"),
    Customer(id=3, name="Rhonda Church"),
    Customer(id=4, name="Georgina Hazel")
]

ACCOUNTS: List[Account] = [
    Account(account_id=1, customer_id=1, balance=1000.0),
    Account(account_id=2, customer_id=2, balance=1500.0),
    Account(account_id=3, customer_id=3, balance=2000.0),
    Account(account_id=4, customer_id=4, balance=2500.0)
]

TRANSFERS: List[Transfer] = []
