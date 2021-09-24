"""

@Time: 2021/9/24 20:01
@Author:
@File: rdf_property.py
"""
from pyfuseki import config
from pyfuseki.rdf.rdf_prefix import NameSpace

def rdf_property(cls: type, local_prefix: str = None):
    if local_prefix is None:
        local_prefix = config.COMMON_PREFIX
    ns = NameSpace(local_prefix)
    annotations = cls.__annotations__
    for k in annotations:
        setattr(cls, k, ns[k])
    return cls

if __name__ == '__main__':
    @rdf_property
    class Node:
        name: str
        email: str
    n = Node()
    print(n.name)
