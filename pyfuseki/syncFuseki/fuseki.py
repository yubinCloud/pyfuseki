"""

@Time: 2021/1/20 17:12
@Author:
@File: fuseki.py
"""
import SPARQLWrapper as sw
from SPARQLWrapper import SPARQLWrapper, JSON, POST, DIGEST
from rdflib import Graph

from pyfuseki.utils import RdfUtils


class BaseFuseki:
    """The base class used to connect and operate the Fuseki service."""

    def __init__(self, fuseki_url: str, dataset: str):
        """
        初始化 BaseFusekiConn
        :param fuseki_url: Jena Fuseki 服务的URL，如本地环境下为"http://localhost:3030"
        :param dataset: Jena Fuseki中数据集的名称
        """
        self.fuseki_url = fuseki_url
        self.dataset = dataset
        self.endpoint_url = None
        self.sparql_conn = None

    def run_sparql(self, sparql_str: str, return_format=JSON) -> sw.Wrapper.QueryResult:
        """
        运行 SPARQL 语句并获取结果，默认返回结果为JSON形式
        :param sparql_str: SPARQL语句
        :param return_format: Possible values are :data:`JSON`, :data:`XML`, :data:`TURTLE`, :data:`N3`, :data:`RDF`, :data:`RDFXML`, :data:`CSV`, :data:`TSV`, :data:`JSONLD` (constants in this module). All other cases are ignored.
        :return: 查询结果
        """
        self.sparql_conn.setQuery(sparql_str)
        self.sparql_conn.setReturnFormat(return_format)
        return self.sparql_conn.query()


class FusekiQuery(BaseFuseki):
    """The class used to connect Fuseki and query data from it."""

    def __init__(self, fuseki_url: str, dataset: str):
        """
        初始化 FusekiQueryConn
        :param fuseki_url: Jena Fuseki 服务的URL，如本地环境下为"http://localhost:3030"
        :param dataset: Jena Fuseki中数据集的名称
        """
        super().__init__(fuseki_url, dataset)
        self.endpoint_url = '/'.join((fuseki_url, dataset, 'query'))
        self.sparql_conn = SPARQLWrapper(self.endpoint_url)


class FusekiUpdate(BaseFuseki):
    """The class used to connect Fuseki and update data from it."""

    def __init__(self, fuseki_url: str, dataset: str):
        """
        初始化 FusekiUpdateConn
        :param fuseki_url: Jena Fuseki 服务的URL，如本地环境下为"http://localhost:3030"
        :param dataset: Jena Fuseki中数据集的名称
        """
        super().__init__(fuseki_url, dataset)
        self.endpoint_url = '/'.join((fuseki_url, dataset, 'update'))
        self.sparql_conn = SPARQLWrapper(self.endpoint_url)
        self.sparql_conn.setMethod(POST)
        self.sparql_conn.setHTTPAuth(DIGEST)

    def insert_graph(self, rdf_graph: Graph, print_sparql:bool=False, unsafe_auto_gen_type_rel:bool=False) -> sw.Wrapper.QueryResult:
        """
        向Fuseki插入一个RDF Graph中保存的数据
        :param rdf_graph: rdflib.Graph的一个对象，存储了本次insert的所有信息
        :param print_sparql: 是否打印生成的SPARQL语句
        :param unsafe_auto_gen_type_rel: 不安全地自动生成所有 URIRef 的 rdf:type 关系
            注意该选项正确运行的前提是假设了每个 URIRef 的类型是它 type URI 后面跟着一个 “/xxx”，xxx标识该 URI
            如假设了 'http://kg/Person/1110' 的 rdf:type 是 'http://kg/Person'
        :return: Fuseki运行的结果
        :raises: ValueError
        """
        insert_sparql_str = RdfUtils.convert_graph_to_insert_sparql(rdf_graph, unsafe_auto_gen_type_rel)
        if print_sparql:
            print(insert_sparql_str)
        return self.run_sparql(insert_sparql_str)
