"""

@Time: 2021/9/18 13:04
@Author:
@File: rf_prefix.py
"""
import rdflib
from pyfuseki import config
import uuid

class NameSpace(rdflib.Namespace):
    """
    继承 rdflib 的 Namespace 并扩充其他相关的功能
    """

    def __getitem__(self, key, default = None) -> rdflib.URIRef:
        return super(NameSpace, self).__getitem__(key, default)

    def __getattr__(self, name) -> rdflib.URIRef:
        return super(NameSpace, self).__getattr__(name)

    def uid(self) -> rdflib.URIRef:
        """
        以 uuid 生成一个唯一 id 来作为 value 包装成 URIRef
        :return:
        """
        return self[str(uuid.uuid1())]

    def to_uri(self) -> rdflib.URIRef:
        """
        将自身转换成 URIRef
        :return:
        """
        uri = str(self)
        if uri.endswith('/'):
            uri = uri[:uri.rfind('/')]
        return rdflib.URIRef(uri)


def rdf_prefix(cls: type, local_prefix: str =None):
    if local_prefix is None:
        local_prefix = config.COMMON_PREFIX
    annotations = cls.__annotations__
    for k in annotations:
        setattr(cls, k, local_prefix + k)
    return cls

if __name__ == '__main__':
    a = NameSpace('http://www.google.com/person/')
    b = a.to_uri()
    print(b)