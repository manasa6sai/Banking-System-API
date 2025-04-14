
# 🏦 FastAPI Banking API

**Author:** Manasa Sai Karanam  
**Framework:** FastAPI  
**Status:** ✅ Completed  
**API Docs:** Swagger UI Enabled  
**Date:** April 2025

---

## 📘 Overview

This is a production-ready **Banking API system** built with **FastAPI**, simulating a backend for internal operations at a financial institution. It provides endpoints for managing customers, accounts, and transfers, and includes administrative routes for full system visibility.

---

## 🚀 Features

### 👤 Customer Operations
- `POST /customers/create` - Create a new customer

### 💼 Account Operations
- `POST /accounts/create` - Create an account with initial deposit
- `GET /accounts/{customer_id}/accounts` - Retrieve all accounts for a customer
- `GET /accounts/{account_id}/balance` - Get current balance of an account
- `GET /accounts/{account_id}/transfers` - View all transfers related to an account

### 🔁 Transfer Operations
- `POST /transfers/` - Make a transfer between any two accounts

### 🛠️ Admin Routes
- `GET /admin/` - Welcome message for admin
- `GET /admin/customers` - List all customers
- `GET /admin/accounts` - List all accounts
- `GET /admin/transfers` - List all transfers

---

## ⚙️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Testing:** Pytest
- **Docs:** Swagger UI (`/docs`), Redoc (`/redoc`)

---

## 📁 Project Structure

```plaintext
banking-api/
├── main.py                  # FastAPI application
├── models.py                # Pydantic schemas & SQLAlchemy models
├── routes/                  # API route definitions
│   ├── customers.py
│   ├── accounts.py
│   ├── transfers.py
│   └── admin.py
├── services.py              # Business logic
├── database.py              # DB connection and initialization
├── tests/                   # Unit and integration tests
├── requirements.txt
└── README.md
```

---

## 🧪 Running the Application

### 1. Clone and setup
```bash
git clone https://github.com/your-username/banking-api.git
cd banking-api
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Start FastAPI app
```bash
uvicorn main:app --reload
```

### 3. Access API
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running Tests
```bash
pytest tests/
```

---

## 🧠 Future Scope

- Add JWT-based authentication
- Extend customer profile support
- Add pagination and filtering to admin endpoints
- Dockerize the entire setup for cloud deployment

---

## 📬 Contact

For queries, reach out at  
📧 **manasakaranam6199@gmail.com**

---
