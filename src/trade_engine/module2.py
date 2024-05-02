from pydantic import BaseModel, Field, validator


class OptionData(BaseModel):
    symbol: str = Field(min_length=1, max_length=10)
    quantity: int = Field(gt=0)
    strike_price: float = Field(gt=0.0)
    expiration_date: str = Field(min_length=8, max_length=10)
    option_type: str = Field(min_length=3, max_length=5)
    action: str = Field(min_length=3, max_length=5)

    @validator('option_type')
    def validate_option_type(cls, v):
        valid_types = ['call', 'put']
        if v.lower() not in valid_types:
            raise ValueError(
                f"option_type must be one of: {', '.join(valid_types)}")
        return v.lower()

    @validator('action')
    def validate_action(cls, v):
        valid_actions = ['buy', 'sell']
        if v.lower() not in valid_actions:
            raise ValueError(
                f"action must be one of: {', '.join(valid_actions)}")
        return v.lower()
