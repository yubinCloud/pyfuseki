"""
实现本体与Python类的映射
@Time: 2021/1/20 16:08
@Author:
@File: __init__.py.py
"""
from .prefixes import rdf_prefix, show_all_prefixes
from .BaseRdfPrefixEnum import BaseRdfPrefixEnum
from .BaseProps import BaseProperty
from .global_namespace_manager import GlobalNamespaceManager