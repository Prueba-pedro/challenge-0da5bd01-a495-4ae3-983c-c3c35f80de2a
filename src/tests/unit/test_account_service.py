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