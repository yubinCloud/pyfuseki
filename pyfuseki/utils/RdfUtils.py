"""

@Time: 2021/1/20 16:59
@Author:
@File: RdfUtils.py
"""
from typing import List, Tuple, Dict, Union, Iterable
from rdflib import Graph, RDF
from rdflib.term import URIRef, Literal, BNode, Identifier
from pyfuseki import config

from pyfuseki.term import RDFList, Subject, Predicate, Object
from pyfuseki.ontology_mapper import BaseRdfPrefixEnum, GlobalNamespaceManager


def bind_prefixes_to_graph(graph: Graph, prefixes: Iterable[BaseRdfPrefixEnum]) -> None:
    """
    将一个列表中的每个RDFPrefix枚举绑定到graph中
    :param graph: rdflib库中Graph类的一个实例对象
    :param prefixes: 由RDFPrefix枚举组成的列表
    :return: None
    """
    if Graph is None or prefixes is None:
        return

    for prefix in prefixes:
        graph.namespace_manager.bind(prefix.name, prefix.value)


def add_list_to_graph(graph: Graph, spo_list: RDFList) -> None:
    """
    将一个SPO三元组的列表一次性地加入 graph 中
    :param graph: 需要加入RDF的graph
    :param spo_list: SPO三元组的列表
    :return: None

    Examples
    --------
    >>> g = Graph()
    >>> spo_list = [
    ...     (URIRef('http://www.ifa.com#Firm/tencent'), URIRef('http://www.ifa.com#hasName'), Literal('腾讯', datatype=XSD.string)),
    ...     (URIRef('http://www.ifa.com#Firm/tencent'), URIRef('http://www.ifa.com#hasApp'), URIRef('http://www.ifa.com#App/wechat'))
    ... ]
    >>> add_list_to_graph(g, spo_list)
    """
    quads = [(s, p, o, graph) for s, p, o in spo_list]
    graph.addN(quads)


def add_dict_to_graph(graph: Graph, s: Subject,
                      po_dict: Dict[Predicate, Object]) -> None:
    """
    将一个P-O的字典一次性地加入 graph 中
    :param graph: 需要加入RDF的graph
    :param s: subject的URIRef
    :param po_dict: predicate-object 组成的字典类型
    :return: None

    Examples
    --------
    >>> from rdflib import XSD, Graph, Literal, URIRef
    >>>
    >>> g = Graph()
    >>> po_dict = {
    ...     URIRef('http://www.ifa.com#hasName'): Literal('腾讯', datatype=XSD.string),
    ...     URIRef('http://www.ifa.com#hasApp'): URIRef('http://www.ifa.com#App/wechat')
    ... }
    >>> s = URIRef('http://www.ifa.com#Firm/tencent')
    >>> add_dict_to_graph(g, s, po_dict)
    """
    quads = [(s, p, o, graph) for p, o in po_dict.items()]
    graph.addN(quads)


def make_all_type_rel(rdf_graph: Graph, COMMON_PREFIX: str = None):
    """
    生成subject和object的所有类型关系的SPO三元组
    :return: 迭代生成所有三元关系的字符串

    Examples
    --------
    >>> for rel in make_all_type_rel(graph)
    >>>     print(rel)
    """
    if COMMON_PREFIX is None:
        COMMON_PREFIX = config.COMMON_PREFIX

    global_nm = GlobalNamespaceManager.get()
    rdf_type_rel = RDF.term('type')

    def extract_type_rel_from_identifier(identifier: Union[BNode, URIRef]):
        """
        在一个identifier中提取出 rdf:type 的三元组关系，并将其转化成字符串表示
        :return: 转化后的字符串
        """
        typename = str(global_nm.compute_qname(identifier)[1])
        if typename[-1] == '/':
            typename = typename[:-1]
        return f'{identifier.n3()} {rdf_type_rel.n3()} {URIRef(typename).n3()}.'

    for s, o in rdf_graph.subject_objects():
        try:
            yield extract_type_rel_from_identifier(s)
        except ValueError:
            pass

        try:
            yield extract_type_rel_from_identifier(o)
        except ValueError:
            pass




def convert_graph_to_insert_sparql(rdf_graph: Graph, auto_gen_type_rel: bool=False) -> str:
    """
    将一个graph转化成一个INSERT SPARQL语句
    :param rdf_graph: 待转化的graph
    :param auto_gen_type_rel：自动产生 rdf:type 关系
    :return: 转化后的SPARQL语句
    """
    # 检查参数是否异常
    if rdf_graph is None:
        raise ValueError
    # 构建 rdf:type 关系
    if auto_gen_type_rel:
        type_rel_graph = create_type_rel_graph(rdf_graph)
        rdf_graph += type_rel_graph
    # 构造graph中已经存在的关系
    spo_str = '\n'.join(
        [f'{s.n3()} {p.n3()} {o.n3()}.' for (s, p, o) in rdf_graph]
    )

    return f"""
                INSERT DATA
                {{
                    {spo_str}
                }}
            """


def create_type_rel_graph(g: Graph) -> Graph:
    type_rel_graph = Graph()
    entity_set = set()  # 用于防止URI重复

    def add_uri_to_rel_graph(uri: URIRef):
        """
        对一个 URIRef 生成 rdf:type 关系并存入 type_rel_graph 中
        :param uri:
        :return:
        """
        uri_s = str(uri)
        if uri_s in entity_set:
            return
        entity_set.add(uri_s)
        type_rel_graph.add((uri, RDF.type, URIRef(uri_s[:uri_s.rfind('/')])))

    for s, p, o in g:
        if o == RDF.type:
            continue
        if type(s) is URIRef:
            add_uri_to_rel_graph(s)
        if type(o) is URIRef:
            add_uri_to_rel_graph(o)
    return type_rel_graph