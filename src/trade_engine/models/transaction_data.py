from pydantic import BaseModel, Field, validator
from typing import Optional


class TransactionData(BaseModel):
    symbol: str = Field(min_length=1, max_length=10)
    quantity: int = Field(gt=0)
    strike_price: float = Field(gt=0.0)
    expiration_date: str = Field(min_length=8, max_length=10)
    option_type: str = Field(min_length=3, max_length=5)
    action: str = Field(min_length=3, max_length=5)
    user_id: int = Field(gt=0)
    option_data_id: str = Field(min_length=20)
