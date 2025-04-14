import pytest
from httpx import AsyncClient
from main import app




''' =============ADMIN FUNCTIONALITIES CHECKING...ADMIN TESTCASES============= '''

@pytest.mark.asyncio
async def test_admin_dashboard():
    """Test the welcome message on the admin dashboard."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/admin/")
        assert response.status_code == 200
        assert response.json() == {
            "message": "Welcome to the Banking API Admin Dashboard. Access /docs for detailed documentation."
        }

@pytest.mark.asyncio
async def test_get_all_customers():
    """Test retrieving all customers from the admin panel."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/admin/customers")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0  # Ensure there are customers

@pytest.mark.asyncio
async def test_get_all_accounts():
    """Test retrieving all accounts from the admin panel."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/admin/accounts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0  # Ensure there are accounts

@pytest.mark.asyncio
async def test_get_all_transfers():
    """Test retrieving all transfers from the admin panel."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/admin/transfers")
        assert response.status_code == 200
        assert isinstance(response.json(), list)



'''======================ADMIN TESTS ENDED==================='''



'''====================ACCOUNTS TESTS STARTED=================='''

@pytest.mark.asyncio
async def test_create_account():
    """Test creating a new bank account."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/accounts/create",
            json={"customer_id": 1, "customer_name": "Arisha Barron", "initial_deposit": 500.0}
        )
        assert response.status_code == 200
        assert response.json()["customer_id"] == 1
        assert response.json()["balance"] == 500.0


@pytest.mark.asyncio
async def test_create_account_for_nonexistent_customer():
    """Test creating an account for a non-existent customer (should return 404)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/accounts/create",
            json={"customer_id": 999, "customer_name": "Fake Customer", "initial_deposit": 500.0}
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "Customer not found. Please create a customer first."




@pytest.mark.asyncio
async def test_get_customer_accounts():
    """Test retrieving all accounts for a given customer."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/accounts/1/accounts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_customer_accounts_not_found():
    """Test retrieving accounts for a non-existent customer (should return 404)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/accounts/999/accounts")  # Non-existent customer
        assert response.status_code == 404
        assert response.json()["detail"] == "No accounts found for this customer."

@pytest.mark.asyncio
async def test_get_account_balance():
    """Test retrieving the balance of a given account."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/accounts/1/balance")
        assert response.status_code == 200
        assert "balance" in response.json()

@pytest.mark.asyncio
async def test_get_account_balance_not_found():
    """Test retrieving balance for a non-existent account (should return 404)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/accounts/999/balance")  # Non-existent account
        assert response.status_code == 404
        assert response.json()["detail"] == "Account not found."

@pytest.mark.asyncio
async def test_get_account_transfers():
    """Test retrieving all transfers related to an account."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/accounts/1/transfers")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_account_transfers_not_found():
    """Test retrieving transfers for a non-existent account (should return 404)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/accounts/999/transfers")  # Non-existent account
        assert response.status_code == 404
        assert response.json()["detail"] == "Account not found."




'''======================ACCOUNTS TESTS ENDED============='''





'''======================CUSTOMERS TESTS STARTED===================='''

@pytest.mark.asyncio
async def test_create_customer():
    """Test creating a new customer."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/customers/create",
            json={"id": 5, "name": "John Doe"}
        )
        assert response.status_code == 200
        assert response.json() == {"id": 5, "name": "John Doe"}

@pytest.mark.asyncio
async def test_create_duplicate_customer():
    """Test creating a customer with an existing ID (should return 400)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        await client.post("/customers/create", json={"id": 6, "name": "Alice"})
        response = await client.post("/customers/create", json={"id": 6, "name": "Bob"})
        assert response.status_code == 400
        assert response.json()["detail"] == "Customer with this ID already exists."



'''======================CUSTOMERS TESTS STARTED======================'''




'''======================TRANSFERS TESTS STARTED======================'''



@pytest.mark.asyncio
async def test_create_transfer():
    """Test creating a valid transfer between two accounts."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/transfers/",
            json={"source_account": 1, "destination_account": 2, "amount": 100.0}
        )
        assert response.status_code == 200
        assert response.json()["source_account"] == 1
        assert response.json()["destination_account"] == 2
        assert response.json()["amount"] == 100.0

@pytest.mark.asyncio
async def test_create_transfer_insufficient_funds():
    """Test transferring an amount greater than the source account balance (should return 400)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/transfers/",
            json={"source_account": 1, "destination_account": 2, "amount": 999999.0}  # Unrealistic amount
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Insufficient funds in the source account."

@pytest.mark.asyncio
async def test_create_transfer_invalid_accounts():
    """Test transferring between non-existent accounts (should return 404)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/transfers/",
            json={"source_account": 999, "destination_account": 1000, "amount": 50.0}
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "One or both accounts not found."

@pytest.mark.asyncio
async def test_create_transfer_same_account():
    """Test transferring to the same account (should return 400)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/transfers/",
            json={"source_account": 1, "destination_account": 1, "amount": 50.0}
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Source and destination accounts must be different."


'''===========TESTING MAIN============'''       
@pytest.mark.asyncio
async def test_admin_dashboard_access():
    """Test accessing the admin dashboard (should return 200)."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/admin/")
        assert response.status_code == 200
        assert response.json() == {
            "message": "Welcome to the Banking API Admin Dashboard. Access /docs for detailed documentation."
        }



'''=============TESTED MAIN======='''

'''======================TRANSFERS TESTS STARTED======================'''


'''TESTCASES : TASK WISE'''
'''

- There should be API routes that allow them to:
  - Create a new bank account for a customer, with an initial deposit amount. A
    single customer may have multiple bank accounts.
  - Transfer amounts between any two accounts, including those owned by
    different customers.
  - Retrieve balances for a given account.
  - Retrieve transfer history for a given account.


'''
@pytest.mark.asyncio
async def test_create_bank_account():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a new account
        response = await client.post(
            "/accounts/create",
            json={
                "customer_id": 1,
                "customer_name": "Arisha Barron",
                "initial_deposit": 500.0
            }
        )
        assert response.status_code == 200
        assert response.json()["customer_id"] == 1
        assert response.json()["balance"] == 500.0


@pytest.mark.asyncio
async def test_transfer_amount():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Perform a transfer
        response = await client.post(
            "/transfers/",
            json={
                "source_account": 1,
                "destination_account": 2,
                "amount": 200.0
            }
        )
        assert response.status_code == 200
        assert response.json()["amount"] == 200.0
        assert response.json()["source_account"] == 1
        assert response.json()["destination_account"] == 2


@pytest.mark.asyncio
async def test_get_account_balance():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Check balance for account 1
        response = await client.get("/accounts/1/balance")
        assert response.status_code == 200
        assert "balance" in response.json()


@pytest.mark.asyncio
async def test_get_transfer_history():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Fetch transfer history for account 1
        response = await client.get("/accounts/1/transfers")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
