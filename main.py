from fastapi import FastAPI
from customers import router as customers_router
from accounts import router as accounts_router
from transfers import router as transfers_router
from admin import router as admin_router
#from auth import router as auth_router


app = FastAPI()

# Include routers
app.include_router(customers_router, prefix="/customers", tags=["Customers"])
app.include_router(accounts_router, prefix="/accounts", tags=["Accounts"])
app.include_router(transfers_router, prefix="/transfers", tags=["Transfers"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])

#app.include_router(auth_router, prefix="/auth", tags=["Authentication"])