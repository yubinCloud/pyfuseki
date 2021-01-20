"""

@Time: 2021/1/20 14:17
@Author:
@File: BindingItem.py
"""
from pydantic import BaseModel


class BindingItem(BaseModel):
    """Model for each result item in the binding in the Fuseki query result"""
    type: str
    value: str


class SPOBindingItems(BaseModel):
    """An SPO triple"""
    s: BindingItem
    p: BindingItem
    o: BindingItem
