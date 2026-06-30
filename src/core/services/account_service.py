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