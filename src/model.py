from typing import List
from pydantic import BaseModel
from constants import TransactionType
from typing import List, Optional

class Transaction(BaseModel):
    category: TransactionType
    value: float

class DataItem(BaseModel):
    date: str
    transactions: List[Transaction]
    total_cost: Optional[float]
    report: Optional[List[float]]