from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from models import Transfer, TransferRequest, TRANSFERS, ACCOUNTS

router = APIRouter()

# Routes

'''
This end point is used to make a bank transfer from one account to another in our Banking App

'''


@router.post("/", response_model=Transfer)
def make_transfer(request: TransferRequest):
    # Prevent same-account transfers
    if request.source_account == request.destination_account:
        raise HTTPException(status_code=400, detail="Source and destination accounts must be different.")

    # Validate source and destination accounts
    source_account = next((acc for acc in ACCOUNTS if acc.account_id == request.source_account), None)
    destination_account = next((acc for acc in ACCOUNTS if acc.account_id == request.destination_account), None)

    if not source_account or not destination_account:
        raise HTTPException(status_code=404, detail="One or both accounts not found.")

    if source_account.balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds in the source account.")

    # Process the transfer
    source_account.balance -= request.amount
    destination_account.balance += request.amount

    # Create transfer record
    transfer_id = len(TRANSFERS) + 1
    transfer_record = Transfer(
        transfer_id=transfer_id,
        source_account=request.source_account,
        destination_account=request.destination_account,
        amount=request.amount,
        transfer_time=datetime.now()
    )
    TRANSFERS.append(transfer_record)
    return transfer_record





# @router.get("/", response_model=List[Transfer])
# def get_all_transfers():
#     return TRANSFERS
