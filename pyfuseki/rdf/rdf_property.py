"""

@Time: 2021/9/24 20:01
@Author:
@File: rdf_property.py
"""
from pyfuseki import config
from pyfuseki.rdf.rdf_prefix import NameSpace

def rdf_property(prefix: str = None):
    if prefix is None:
        prefix = config.COMMON_PREFIX
    def _gen_uri_helper(cls: type):
        ns = NameSpace(prefix)
        annotations = cls.__annotations__
        for k in annotations:
            setattr(cls, k, ns[k])
        return cls
    return _gen_uri_helper

