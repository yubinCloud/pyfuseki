"""

@Time: 2021/1/20 16:22
@Author:
@File: BaseRdfPrifixEnum.py
"""
from enum import Enum
import rdflib
from typing import Union

class BaseRdfPrefixEnum(Enum):
    def val(self, value: str = None) -> Union[rdflib.BNode, rdflib.URIRef]:
        """
        以该namespace和传入的value生成一个URIRef或BNode或Literal
        :param value: 所生成的Identifier的值
        :return: 所生成的Identifier
        """
        if value is None:
            return rdflib.BNode()
        else:
            return self.value[value]