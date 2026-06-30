app = FastAPI()

from.core.config import settings
from.core.security import SecurityConfig
from.core.models import Account
from.core.schemas import AccountSchema, AccountCreate, AccountUpdate
from.core.services import AccountService
from.api.v1.accounts import accounts_router

app.include_router(accounts_router)