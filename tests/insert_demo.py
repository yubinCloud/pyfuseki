import pyfuseki.register
from rdflib import Graph, Literal

from pyfuseki import FusekiUpdate
from pyfuseki.utils import RdfUtils

from rdflib import URIRef as uri, RDF, XSD
from pyfuseki.rdf import rdf_prefix, rdf_property, NameSpace as ns

COMMON_PREFIX = 'http://www.inet.com/kg/ontoligies/ifa#'
pyfuseki.register.register_common_prefix(COMMON_PREFIX)

@rdf_prefix
class FirmRdfPrefix():
    """
    公司信息三元组前缀的枚举
    用于向graph中bind前缀，该枚举的name为前缀，value为其对应的包装了IRI的URIRef或Namespace对象
    """
    BrandProject: ns
    Event: ns
    Firm: ns
    Person: ns


rp = FirmRdfPrefix()


@rdf_property
class DataProperty:
    """
    本体中所有Data properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    hasName: uri
    brandAgencyDataProperty: uri
    createTime: uri
    enName: uri

dp = DataProperty()

@rdf_property
class ObjectProperty:
    """
    本体中所有Object properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    brandAgencyObjectProperty: uri
    subordinateTo: uri   # 从属于
    hasFounder: uri  # 有创始人

op = ObjectProperty()

if __name__ == '__main__':
    fuseki = FusekiUpdate('http://localhost:8500', 'test_db')
    g = Graph()
    """测试整个过程"""
    # 假设获取的数据为data
    data = {
        'band_project': '腾讯',
        '工商id': '1110',
        '所属企业': '深圳市腾讯计算机系统有限公司',
        '成立日期': '1998-11-11',
        '英文名称': 'QQ',
        '创办人': '马化腾',
    }
    # 将rev_data转化成RDF三元组并加入graph中
    tencent = rp.BrandProject[data['工商id']]
    tencent_firm = rp.Firm['深圳市腾讯计算机系统有限公司']
    # g.add((tencent, RDF.type, rp.BrandProject.to_uri()))
    # g.add((tencent_firm, RDF.type, rp.Firm.to_uri()))
    RdfUtils.add_dict_to_graph(g, tencent, {
        op.subordinateTo: tencent_firm,
        dp.createTime: Literal('1998-11-11', datatype=XSD.date),
        dp.enName: Literal(data['英文名称'])
    })
    print(g)
    # 将graph插入
    fuseki.insert_graph(g, print_sparql=True, unsafe_auto_gen_type_rel=True)
