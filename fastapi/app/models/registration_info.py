from sqlmodel import Field, Session, SQLModel
from typing import Optional

class RegistrationInfo(SQLModel, table=True):
    key: Optional[str] = Field(default="", primary_key=True)
    is_valid: bool = Field(default=True)
    owner_name: str = Field(default="")
    subscription_offer_reference: str = Field(default="virtual")
    subscription_title: str = Field(default="Enregistré")
    subscription_is_running: bool = Field(default=True)
    subscription_begin_date: str = Field(default=None)
    subscription_end_date: str = Field(default=None)
    subscription_features: str = Field(default="[]")