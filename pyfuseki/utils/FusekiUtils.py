"""

@Time: 2021/1/20 17:25
@Author:
@File: FusekiUtils.py
"""
from typing import List, Tuple, Optional, Dict
import SPARQLWrapper as sw


def parse_query_result(query_result: sw.Wrapper.QueryResult) -> Tuple[Optional[Dict], List[Dict]]:
    """
    解析查询的结果
    :param query_result: fuseki调用query方法后返回的结果
    :return: 查询的变量, 查询的结果
    """
    # 首先检查请求结果的格式是否为JSON形式
    if query_result.requestedFormat != 'json':
        raise ValueError('FusekiUtils.query_result method need a "JSON" format Fuseki response to parse.')

    json_resp = query_result.convert()  # 对查询的响应转换成字典的形式
    try:
        query_vars = json_resp['head']['vars']
        query_results = json_resp['results']['bindings']
        return query_vars, query_results
    except KeyError:
        return None, json_resp['boolean']


def extract_property_from_uri(uri: str) -> str:
    """
    从property uri中提取出property name
    :param uri: 如 <http://www.kg.com/kg/ontoligies/ifa#createTime>
    :return: 如 'createTime'
    """
    separator_idx = uri.rfind('#')
    if separator_idx == -1:
        raise ValueError
    return uri[separator_idx + 1:]


def extract_entity_type_and_name_from_uri(uri: str) -> Tuple[str, str]:
    """
    从entity uri中提取出其type和name
    :param uri: 如 http://www.kg.com/kg/ontoligies/ifa#Firm/百度
    :return: ('Firm', '百度')
    """
    name_separator = uri.rfind('/')
    type_separator = uri.rfind('#')
    return uri[type_separator + 1: name_separator], uri[name_separator + 1:]