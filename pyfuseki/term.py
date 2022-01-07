"""

@Time: 2021/2/18 17:01
@Author:
@File: type.py
"""
from typing import List, Tuple, Union
from rdflib.term import Identifier, URIRef, BNode


Subject = Union[URIRef, BNode]
Predicate = URIRef
Object = Identifier

Statement = Tuple[Subject, Predicate, Object]

RDFList = List[Statement]
