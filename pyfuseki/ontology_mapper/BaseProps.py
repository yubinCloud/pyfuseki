"""

@Time: 2021/1/20 16:43
@Author:
@File: BaseProps.py
"""
from enum import unique, Enum

@unique
class BaseProperty(Enum):
    """
    PropertyIRI 枚举类的基类，其子类包含 ObjectProperty 和 DataPropertyIRI
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    pass