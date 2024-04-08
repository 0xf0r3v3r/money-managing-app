from pydantic import BaseModel


class CurrencyRead(BaseModel):
    id: int
    name: str
    symbol: str


class CurrencyCreate(BaseModel):
    name: str
    symbol: str


class CurrencyUpdate(BaseModel):
    name: str = None
    symbol: str = None


class AccountRead(BaseModel):
    id: int
    name: str
    note: str
    summ: float
    is_savings_account: bool
    image_url: str
    fk_currency_id: int
    fk_user_id: int


class AccountCreate(BaseModel):
    name: str
    note: str
    summ: float
    is_savings_account: bool
    image_url: str
    fk_currency_id: int


class AccountUpdate(BaseModel):
    name: str
    note: str
    summ: float
    image_url: str
    fk_currency_id: int
