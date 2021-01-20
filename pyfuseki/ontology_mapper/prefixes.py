"""

@Time: 2021/1/20 16:09
@Author:
@File: prefixes.py
"""
from typing import List
from enum import EnumMeta
from .BaseRdfPrefixEnum import BaseRdfPrefixEnum

__prefix_enum_store: List[EnumMeta] = []

def rdf_prefix(cls: EnumMeta):
    """
    class decorator, used to register RDF prefix classes.

    Examples
    --------
    >>> from pyfuseki.ontology_mapper import BaseRdfPrefixEnum
    >>> from rdflib import Namespace
    >>> from pyfuseki import config
    >>>
    >>> @rdf_prefix
    ... class MyPrefix(BaseRdfPrefixEnum):
    ...     Firm = Namespace(config.COMMON_PREFIX + "Firm")
    ...     Project = Namespace(config.COMMON_PREFIX + "Project")
    ...
    >>>
    """
    __prefix_enum_store.append(cls)
    return cls


def show_all_prefixes():
    for prefix_cls in __prefix_enum_store:
        print(prefix_cls)


def get_prefix_enum_store() -> List[EnumMeta]:
    for t in __prefix_enum_store:
        if BaseRdfPrefixEnum not in t.__bases__:
            raise ValueError('加入prefix_enum_store中的枚举类型必须为继承自BaseRDFPrefixEnum的类型')
    return __prefix_enum_store