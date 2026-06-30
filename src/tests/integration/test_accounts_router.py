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