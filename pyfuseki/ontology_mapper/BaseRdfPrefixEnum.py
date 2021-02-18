"""

@Time: 2021/1/20 16:22
@Author:
@File: BaseRdfPrefixEnum.py
"""
from enum import Enum
import rdflib
from typing import Union, Any
import uuid

class BaseRdfPrefixEnum(Enum):
    """
    All RDFPrefixEnum class should inherit from it.
    """
    def val(self, value: Any = None) -> Union[rdflib.BNode, rdflib.URIRef]:
        """
        以该namespace和传入的value生成一个URIRef或BNode或Literal
        :param value: 所生成的Identifier的值
        :return: 所生成的Identifier
        """
        if value is None:
            return rdflib.BNode()
        else:
            return self.value[str(value)]

    def uid(self) -> rdflib.URIRef:
        """
        以 uuid 生成一个唯一 id 来作为 value 包装成 URIRef
        :return:
        """
        return self.value[str(uuid.uuid1())]