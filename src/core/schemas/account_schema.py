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