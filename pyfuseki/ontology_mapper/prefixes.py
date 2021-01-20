"""

@Time: 2021/1/20 16:09
@Author:
@File: prefixes.py
"""
from typing import List
from enum import EnumMeta

__prefix_cls_list: List[EnumMeta] = []

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
    __prefix_cls_list.append(cls)
    return cls


def show_all_prefixes():
    for prefix_cls in __prefix_cls_list:
        print(prefix_cls)