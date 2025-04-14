# from fastapi import APIRouter, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext

# router = APIRouter()

# # Secret key to encode the JWT tokens (keep this secret)
# SECRET_KEY = "your_secret_key_here"  # Change this to a strong secret key
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes

# # Password hashing context
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Utility functions for password hashing
# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

# # JWT token creation
# def create_access_token(data: dict) -> str:
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode = data.copy()
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # JWT token verification
# def verify_access_token(token: str) -> dict:
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except JWTError:
#         raise ValueError("Invalid token or expired")

# # Sample hardcoded user (in a real app, fetch user from DB)
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "hashed_password": "$2b$12$KIXk3cm0c9MHeLQdYAd1lOmIZj/MY3Ljoij0w7HznWlY09tm0hOgu"  # hashed "password123"
#     }
# }


# # Token endpoint to generate JWT token
# @router.post("/token")
# def login_for_access_token(form_data: OAuth2PasswordRequestForm):
#     # OAuth2PasswordRequestForm is used to extract the form data
#     user = fake_users_db.get(form_data.username)
#     if not user or not verify_password(form_data.password, user["hashed_password"]):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_access_token(data={"sub": form_data.username})
#     return {"access_token": access_token, "token_type": "bearer"}