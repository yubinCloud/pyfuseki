"""

@Time: 2021/9/9 22:15
@Author:
@File: insert_test.py
"""
import pyfuseki.register
from rdflib import Graph, Literal
from rdflib.namespace import XSD

from pyfuseki import FusekiUpdate
from pyfuseki.utils import RdfUtils

from rdflib import Namespace
import rdflib
from pyfuseki.ontology_mapper import BaseRdfPrefixEnum

COMMON_PREFIX = 'http://www.inet.com/kg/ontoligies/ifa#'
pyfuseki.register.register_common_prefix(COMMON_PREFIX)

class FirmRdfPrefix(BaseRdfPrefixEnum):
    """
    公司信息三元组前缀的枚举
    用于向graph中bind前缀，该枚举的name为前缀，value为其对应的包装了IRI的URIRef或Namespace对象
    """

    # ----------  Classes ---------- #
    BrandProject = Namespace(COMMON_PREFIX + 'BrandProject/')
    Event = Namespace(COMMON_PREFIX + 'Event/')
    Firm = Namespace(COMMON_PREFIX + 'Firm/')
    Person = Namespace(COMMON_PREFIX + 'Person/')

    # ---------- Datatypes ---------- #
    owl = rdflib.namespace.OWL
    xsd = rdflib.namespace.XSD
    rdf = rdflib.namespace.RDF
    rdfs = rdflib.namespace.RDFS

rp = FirmRdfPrefix

ifa = Namespace(COMMON_PREFIX)

from pyfuseki.ontology_mapper import BaseProperty


class DataProperty(BaseProperty):
    """
    本体中所有Data properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    hasName = ifa.hasName
    brandAgencyDataProperty = ifa.brandAgencyDataProperty
    createTime = ifa.createTime
    enName = ifa.enName

dp = DataProperty

class ObjectProperty(BaseProperty):
    """
    本体中所有Object properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    brandAgencyObjectProperty = ifa.brandAgencyObjectProperty
    subordinateTo = ifa.subordinateTo   # 从属于
    hasFounder = ifa['hasFounder']  # 有创始人

op = ObjectProperty

if __name__ == '__main__':


    fuseki = FusekiUpdate('http://localhost:3030', 'test_db')
    g = Graph()
    """测试整个过程"""
    # 假设获取的数据为rev_data
    rev_data = {
        'band_project': '腾讯',
        '所属企业': '深圳市腾讯计算机系统有限公司',
        '成立日期': '1998-11-11',
        '英文名称': 'QQ',
        '创办人': '马化腾',
    }
    # 将rev_data转化成RDF三元组并加入graph中
    tencent = rp.BrandProject.val('腾讯')
    RdfUtils.add_dict_to_graph(g, tencent, {
        op.subordinateTo.value: rp.Firm.val('深圳市腾讯计算机系统有限公司'),
        dp.createTime.value: Literal('1998-11-11', datatype=XSD.date),
        dp.enName.value: Literal(rev_data['英文名称'], datatype=XSD.string)
    })
    print(g)
    # 将graph插入
    fuseki.insert_graph(g)
