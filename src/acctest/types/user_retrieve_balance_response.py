# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UserRetrieveBalanceResponse", "BalanceInfo"]


class BalanceInfo(BaseModel):
    currency: Optional[str] = None

    granted_balance: Optional[str] = None

    topped_up_balance: Optional[str] = None

    total_balance: Optional[str] = None


class UserRetrieveBalanceResponse(BaseModel):
    balance_infos: List[BalanceInfo]

    is_available: bool
