"""

@Time: 2021/1/20 17:59
@Author:
@File: main.py
"""
from pyfuseki import AsyncFuseki
import pyfuseki
from pyfuseki.utils import RdfUtils
from rdflib import Graph, Literal, XSD
from demo.RdfPrefix import RdfPrefix as rp
from demo.properties import ObjectProperty as op, DataProperty as dp
import asyncio


async def insert_test():
    pyfuseki.register.register_common_prefix("http://www.yubin.com/kg/")
    fuseki = AsyncFuseki('http://localhost:3030', 'pyfuseki_db')
    g = Graph()

    # RdfUtils.bind_prefixes_to_graph(self.g, [rp.BrandProject, rp.Firm])  # 绑定前缀
    # 假设获取的数据为rev_data
    rev_data = {
        'band_project': '腾讯',
        '所属企业': '深圳市腾讯计算机系统有限公司',
        '成立日期': '1998-11-11',
        '英文名称': 'QQ'
    }
    # 将rev_data转化成RDF三元组并加入graph中
    tencent = rp.BrandProject.val('腾讯')
    RdfUtils.add_dict_to_graph(g, tencent, {
        op.subordinateTo.value: rp.Firm.val('深圳市腾讯计算机系统有限公司'),
        dp.createTime.value: Literal(rev_data['成立日期'], datatype=XSD.date),
        dp.enName.value: Literal(rev_data['英文名称'], datatype=XSD.string)
    })
    print(g)
    # 将graph插入
    await fuseki.insert_graph(g)

if __name__ == '__main__':
    asyncio.run(insert_test())