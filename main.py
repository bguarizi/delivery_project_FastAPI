#Comando para rodar o fastAPI: uvicorn main:app --reload
#Biblioteca alembic é responsável pelas migrations dentro do banco de dados
#***Comando para iniciar o alembic: alembic init alembic
#***Depois que o alembic é executado, no arquivo alembic.ini é preciso alterar o endereço para acesso ao banco de dados
#***Depois tem que alterar o arquivo env.py da pasta alembic para importar o base para criação do banco de dados (linhas a serem adicionadas marcadas com #new)
#Comando para gerar migrações no banco de dados com alembic: alembic revision --autogenerate -m "Initial Migration"
#***Comando para executar a migração: alembic upgrade head
from fastapi import FastAPI
#from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import hashlib
import base64
import bcrypt
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

#bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") -> O uso do bcrypt com passlib não funcionou com as versões mais recentes

#Versão atualizada da criptografia, usando a biblioteca bcrypt -> É necessário adicionalmente instalar e importar: pip install bcrypt (ou usar meu arquivo de requirements.txt)
def _prehash(password: str) -> bytes:
    digest = hashlib.sha256(password.encode()).digest()
    return base64.b64encode(digest)  # retorna bytes, sempre < 72

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(_prehash(password), salt).decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(_prehash(plain), hashed.encode())

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

