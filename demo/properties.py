"""

@Time: 2021/1/20 18:09
@Author:
@File: properties.py
"""
from pyfuseki.ontology_mapper import BaseProperty
from rdflib import Namespace
from pyfuseki import config
yb = Namespace(config.COMMON_PREFIX)

class ObjectProperty(BaseProperty):
    """
    本体中所有Object properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    subordinateTo = yb.subordinateTo   # 从属于


class DataProperty(BaseProperty):
    """
    本体中所有Data properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    createTime = yb.createTime
    enName = yb.enName