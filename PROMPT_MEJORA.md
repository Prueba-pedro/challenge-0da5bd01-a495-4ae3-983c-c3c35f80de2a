# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
import jwt
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# === ARCHIVO: src/main.py ===
app = FastAPI()

from.core.config import settings
from.core.security import SecurityConfig
from.core.models import Account
from.core.schemas import AccountSchema, AccountCreate, AccountUpdate
from.core.services import AccountService
from.api.v1.accounts import accounts_router

app.include_router(accounts_router)

# === ARCHIVO: src/core/config/settings.py ===
class Settings:
    SECRET_KEY = 'your-secret-key'
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()

# === ARCHIVO: src/core/security/security.py ===
class SecurityConfig:
    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

security_config = SecurityConfig()

# === ARCHIVO: src/core/models/account.py ===
Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    balance = Column(Float)
    account_type = Column(String)
    holder = Column(String)

# === ARCHIVO: src/core/schemas/account_schema.py ===
class AccountSchema(BaseModel):
    id: int
    account_number: str
    balance: float
    account_type: str
    holder: str

class AccountCreate(BaseModel):
    account_number: str
    balance: float
    account_type: str
    holder: str

class AccountUpdate(BaseModel):
    balance: float
    account_type: str
    holder: str

# === ARCHIVO: src/core/services/account_service.py ===
class AccountService:
    def __init__(self, db: Session):
        self.db = db

    def get_account_by_number(self, account_number: str):
        return self.db.query(Account).filter(Account.account_number == account_number).first()

    def create_account(self, account: AccountCreate):
        db_account = Account(**account.dict())
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return db_account

    def update_account(self, account_number: str, account: AccountUpdate):
        db_account = self.get_account_by_number(account_number)
        if db_account is None:
            raise HTTPException(status_code=404, detail='Account not found')
        for key, value in account.dict().items():
            setattr(db_account, key, value)
        self.db.commit()
        self.db.refresh(db_account)
        return db_account

    def delete_account(self, account_number: str):
        db_account = self.get_account_by_number(account_number)
        if db_account is None:
            raise HTTPException(status_code=404, detail='Account not found')
        self.db.delete(db_account)
        self.db.commit()

# === ARCHIVO: src/api/v1/accounts/accounts_router.py ===
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from..core.models import Account
from..core.schemas import AccountSchema, AccountCreate, AccountUpdate
from..core.services import AccountService
from..core.security import security_config
from..core.config import settings
from..core.security import SecurityConfig

router = APIRouter()

@router.post('/accounts/', response_model=AccountSchema)
def create_account(account: AccountCreate, db: Session = Depends(security_config.get_db)):
    return AccountService(db).create_account(account)

@router.get('/accounts/{account_number}', response_model=AccountSchema)
def get_account(account_number: str, db: Session = Depends(security_config.get_db)):
    account = AccountService(db).get_account_by_number(account_number)
    if account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return account

@router.put('/accounts/{account_number}', response_model=AccountSchema)
def update_account(account_number: str, account: AccountUpdate, db: Session = Depends(security_config.get_db)):
    return AccountService(db).update_account(account_number, account)

@router.delete('/accounts/{account_number}')
def delete_account(account_number: str, db: Session = Depends(security_config.get_db)):
    AccountService(db).delete_account(account_number)
    return {'detail': 'Account deleted'}

# === ARCHIVO: src/tests/unit/test_account_service.py ===
from sqlalchemy.orm import Session
from..core.models import Account
from..core.services import AccountService
from..core.schemas import AccountCreate, AccountUpdate

def test_create_account(db: Session):
    account_service = AccountService(db)
    account = AccountCreate(account_number='123456789', balance=100.0, account_type='checking', holder='John Doe')
    created_account = account_service.create_account(account)
    assert created_account.account_number == account.account_number

def test_update_account(db: Session):
    account_service = AccountService(db)
    account = AccountCreate(account_number='123456789', balance=100.0, account_type='checking', holder='John Doe')
    created_account = account_service.create_account(account)
    update_data = AccountUpdate(balance=200.0, account_type='savings', holder='Jane Doe')
    updated_account = account_service.update_account(created_account.account_number, update_data)
    assert updated_account.balance == update_data.balance

def test_delete_account(db: Session):
    account_service = AccountService(db)
    account = AccountCreate(account_number='123456789', balance=100.0, account_type='checking', holder='John Doe')
    created_account = account_service.create_account(account)
    account_service.delete_account(created_account.account_number)
    deleted_account = account_service.get_account_by_number('123456789')
    assert deleted_account is None

# === ARCHIVO: src/tests/integration/test_accounts_router.py ===
from fastapi.testclient import TestClient
from..main import app
from..core.models import Account
from sqlalchemy.orm import Session
from..core.services import AccountService
from..core.schemas import AccountCreate, AccountUpdate

def test_create_account(test_db: Session):
    client = TestClient(app)
    account_data = AccountCreate(account_number='123456789', balance=100.0, account_type='checking', holder='John Doe')
    response = client.post('/api/v1/accounts/', json=account_data.dict())
    assert response.status_code == 200
    assert response.json()['account_number'] == account_data.account_number

def test_get_account(test_db: Session):
    client = TestClient(app)
    account_service = AccountService(test_db)
    account_data = AccountCreate(account_number='123456789', balance=100.0, account_type='checking', holder='John Doe')
    created_account = account_service.create_account(account_data)
    response = client.get(f'/api/v1/accounts/{created_account.account_number}')
    assert response.status_code == 200
    assert response.json()['account_number'] == created_account.account_number

def test_update_account(test_db: Session):
    client = TestClient(app)
    account_service = AccountService(test_db)
    account_data = AccountCreate(account_number='123456789', balance=100.0, account_type='checking', holder='John Doe')
    created_account = account_service.create_account(account_data)
    update_data = AccountUpdate(balance=200.0, account_type='savings', holder='Jane Doe')
    response = client.put(f'/api/v1/accounts/{created_account.account_number}', json=update_data.dict())
    assert response.status_code == 200
    assert response.json()['balance'] == update_data.balance

def test_delete_account(test_db: Session):
    client = TestClient(app)
    account_service = AccountService(test_db)
    account_data = AccountCreate(account_number='123456789', balance=100.0, account_type='checking', holder='John Doe')
    created_account = account_service.create_account(account_data)
    response = client.delete(f'/api/v1/accounts/{created_account.account_number}')
    assert response.status_code == 200
    assert response.json()['detail'] == 'Account deleted'

```
