from fastapi import APIRouter, HTTPException
from typing import List, Dict
from models import Account, NewAccountRequest, Transfer, CUSTOMERS, ACCOUNTS, TRANSFERS

router = APIRouter()

# Routes
'''
This end point is used to create a new account for an on-boarded customer in our  Banking App

'''
@router.post("/create", response_model=Account)
def create_account(request: NewAccountRequest):
    # Validate that the customer exists
    existing_customer = next((c for c in CUSTOMERS if c.id == request.customer_id), None)

    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found. Please create a customer first.")

    # Generate new account ID
    account_id = len(ACCOUNTS) + 1

    # Create and store the new account
    new_account = Account(account_id=account_id, customer_id=request.customer_id, balance=request.initial_deposit)
    ACCOUNTS.append(new_account)
    
    return new_account


'''
This end point is used to list all the accounts of an on-boarded customer in our Banking App

'''


@router.get("/{customer_id}/accounts", response_model=List[Account])
def get_customer_accounts(customer_id: int):
    customer_accounts = [acc for acc in ACCOUNTS if acc.customer_id == customer_id]
    if not customer_accounts:
        raise HTTPException(status_code=404, detail="No accounts found for this customer.")
    return customer_accounts


'''
This end point is used to check the balance of an account in our Banking App

'''


@router.get("/{account_id}/balance", response_model=Dict[str, float])
def get_balance(account_id: int):
    account = next((acc for acc in ACCOUNTS if acc.account_id == account_id), None)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found.")
    return {"balance": account.balance}


'''
This end point is used to check transaction history of an account in our Banking App

'''

@router.get("/{account_id}/transfers", response_model=List[Transfer])
def get_account_transfers(account_id: int):
    if not any(acc.account_id == account_id for acc in ACCOUNTS):
        raise HTTPException(status_code=404, detail="Account not found.")

    transfers = [
        transfer for transfer in TRANSFERS
        if transfer.source_account == account_id or transfer.destination_account == account_id
    ]
    return transfers

# @router.get("/", response_model=List[Account])
# def get_all_accounts():
#     return ACCOUNTS
