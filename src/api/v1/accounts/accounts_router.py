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