"""

@Time: 2021/9/18 13:04
@Author:
@File: rf_prefix.py
"""
import rdflib
from pyfuseki import config
import uuid


name_to_uri = dict()

class NameSpace(rdflib.Namespace):
    """
    继承 rdflib 的 Namespace 并扩充其他相关的功能
    """

    def __getitem__(self, key) -> rdflib.URIRef:
        return super(NameSpace, self).__getitem__(key)

    def __getattr__(self, name) -> rdflib.URIRef:
        return super(NameSpace, self).__getattr__(name)

    def uid(self, name) -> rdflib.URIRef:
        """
        以 uuid 生成一个唯一 id 来作为 value 包装成 URIRef
        :return:
        """
        if name not in name_to_uri:
            name_to_uri[name] = str(uuid.uuid1())
        uri = name_to_uri[name]
        return rdflib.URIRef(self[uri])

    def to_uri(self) -> rdflib.URIRef:
        """
        将自身转换成 URIRef
        :return:
        """
        uri = str(self)
        if uri.endswith('/'):
            uri = uri[:uri.rfind('/')]
        return rdflib.URIRef(uri)


def rdf_prefix(cls: type, local_prefix: str = None):
    if local_prefix is None:
        local_prefix = config.COMMON_PREFIX
    attrs = cls.__annotations__.keys()
    for k in attrs:
        setattr(cls, k, NameSpace(local_prefix + k + '/'))
    return cls

if __name__ == '__main__':
    a = NameSpace('http://www.google.com/person/')
    b = a.to_uri()

    @rdf_prefix
    class Node:
        name: str
        email: str

    n = Node()
    print(n.name['yubin'])