"""

@Time: 2021/1/20 14:13
@File: async_fuseki.py
"""
import httpx
import asyncio
from rdflib import Graph

from pyfuseki.asyncFuseki.fuseki_resp import AsyncFusekiResp
from pyfuseki import exceptions
from pyfuseki.utils import RdfUtils


class AsyncFuseki:
    """A class which connect Fuseki asynchronously"""

    def __init__(self, fuseki_url: str, db_name: str):
        """
        Examples
        --------
        >>> fuseki = AsyncFuseki('http://localhost:3030', 'test_db')
        """
        self._fuseki_url = fuseki_url
        self._db_name = db_name
        self._req_url = f"{fuseki_url}/{db_name}"

    def getReqUrl(self):
        return self._req_url

    async def _post_data_to_fuseki(self, data: dict) -> AsyncFusekiResp:
        """
        Send a POST request to Fuseki and wrap the returned object as an AsyncFusekiResp object
        :param data: The data carried in the POST request
        :return: The response of Fuseki returned.
        :raise FusekiConnectError
        :raise httpx.HTTPStatusError
        """
        async with httpx.AsyncClient() as client:
            try:
                resp: httpx.Response = await client.post(self._req_url, data=data)
            except httpx.ConnectError:
                raise exceptions.FusekiConnectError('Fuseki 连接出错，请确认 Fuseki 是否已开启。')

            resp.raise_for_status()  # 当HTTP状态码不正常时引发异常
        return AsyncFusekiResp(resp)

    async def query_sparql(self, sparql: str) -> AsyncFusekiResp:
        """
        异步方式对Fuseki的查询接口运行SPARQL语句
        :param sparql: 运行的查询SPARQL语句
        :return: 查询的响应
        :raise FusekiConnectError Fuseki连接出错
        :raise httpx.HTTPStatusError Fuseki响应的非正常状态码引发的异常
        """
        data = {'query': sparql}
        return await self._post_data_to_fuseki(data)

    async def update_sparql(self, sparql: str) -> AsyncFusekiResp:
        """
        异步方式对Fuseki的更新接口运行SPARQL语句
        :param sparql: 运行的更新SPARQL语句
        :return: 查询的响应
        :raise FusekiConnectError Fuseki连接出错
        :raise httpx.HTTPStatusError Fuseki响应的非正常状态码引发的异常
        """
        data = {'update': sparql}
        return await self._post_data_to_fuseki(data)

    async def insert_graph(self, graph: Graph, print_sparql: bool = False) -> AsyncFusekiResp:
        """
        采用异步的方式向Fuseki插入一个RDF Graph中保存的数据，当插入数据时建议使用这个函数
        :param graph: 保存有RDF数据的graph
        :return: Fuseki的响应
        :raise FusekiConnectError Fuseki连接出错
        :raise httpx.HTTPStatusError Fuseki响应的非正常状态码引发的异常
        """
        insert_sparql_str = RdfUtils.convert_graph_to_insert_sparql(graph)
        if print_sparql:
            print(insert_sparql_str)
        return await self.update_sparql(insert_sparql_str)



if __name__ == '__main__':
    fuseki = AsyncFuseki('http://localhost:3030', 'test_db')
    s = """
    SELECT *
    WHERE {?s ?p ?o}
    LIMIT 25
    """

    resp = asyncio.run(fuseki.query_sparql(s))
    print(resp)
    items = resp.to_bindingItemModels()

    print(items)
