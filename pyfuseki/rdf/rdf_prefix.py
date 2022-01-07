"""

@Time: 2021/9/18 13:04
@Author:
@File: rf_prefix.py
"""
import rdflib
from pyfuseki import config
import uuid
from typing import Callable


name_to_uri = dict()

class NameSpace(rdflib.Namespace):
    """
    继承 rdflib 的 Namespace 并扩充其他相关的功能
    """

    def __getitem__(self, key) -> rdflib.URIRef:
        return super(NameSpace, self).__getitem__(key)

    def __getattr__(self, name) -> rdflib.URIRef:
        return super(NameSpace, self).__getattr__(name)

    def uid(self) -> rdflib.URIRef:
        """
        以 uuid 生成一个唯一 id 来作为 value 包装成 URIRef
        :return:
        """
        return rdflib.URIRef(self[str(uuid.uuid1())])

    def to_uri(self) -> rdflib.URIRef:
        """
        将自身转换成 URIRef
        :return:
        """
        uri = str(self)
        if uri.endswith('/'):
            uri = uri[:uri.rfind('/')]
        return rdflib.URIRef(uri)


def __default_prefix_connect_strategy(prefix: str, attr_name: str) -> str:
    return prefix + attr_name + '/'

def rdf_prefix(prefix: str = None, prefix_connect_strategy: Callable[[str, str], str] = __default_prefix_connect_strategy):
    """
    装饰到用来定义本体中的类的 class 上，能够为该 class 的字段生成相应的 rdf 命名空间
    :param local_prefix: 前缀
    """
    if prefix is None:
        prefix = config.COMMON_PREFIX
    def _gen_prefix_helper(cls: type):
        attrs = cls.__annotations__.keys()
        for k in attrs:
            setattr(cls, k, NameSpace(prefix_connect_strategy(prefix, k)))
        return cls
    return _gen_prefix_helper
