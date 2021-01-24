# PyFuseki
<p align="center"><strong>pyfuseki</strong> <em>- An easy way to mix together OWL and Jena Fuseki.</em>   
</p>
<p>
<img src="https://img.shields.io/github/license/yubinCloud/pyfuseki">
</p>
A library that uses Python to connect and manipulate Jena Fuseki, which provides sync and async methods.

By using pyfuseki, you can easily store data from your program into Jena Fuseki, following the ontology model, and then query and parse Jena.

---

**Documentation**: <a href="https://yubincloud.github.io/pyfuseki/" target="_blank">https://yubincloud.github.io/pyfuseki/</a>

**Source Code**: <a href="https://github.com/yubinCloud/pyfuseki" target="_blank">https://github.com/yubinCloud/pyfuseki</a>

---
## Requirements

Python 3.6+

PyFuseki stands on the shoulders of giants:

+ [Pydantic](https://pydantic-docs.helpmanual.io/) for the data parts.
+ [httpx](https://www.python-httpx.org/) for the network parts.
+ [rdflib](https://rdflib.readthedocs.io/en/stable/) for the RDF parts.

## Installation

```console
$ pip install pyfuseki

---> 100%
```

## Example

+ First, we define the classes of the ontology predesigned:

```Python
from pyfuseki.ontology_mapper import rdf_prefix, BaseRdfPrefixEnum
from rdflib import Namespace
from pyfuseki import config
   
@rdf_prefix
class RdfPrefix(BaseRdfPrefixEnum):
    BrandProject = Namespace(config.COMMON_PREFIX + 'BrandProject')
    Firm = Namespace(config.COMMON_PREFIX + 'Firm')
```

+ Next, we define the data properties and object properties of the ontology predesigned:

```Python
from pyfuseki.ontology_mapper import BaseProperty
from rdflib import Namespace
from pyfuseki import config

yb = Namespace(config.COMMON_PREFIX)

class ObjectProperty(BaseProperty):
    """
    本体中所有Object properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    brandAgencyObjectProperty = yb.brandAgencyObjectProperty
    subordinateTo = yb.subordinateTo   # 从属于


class DataProperty(BaseProperty):
    """
    本体中所有Data properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    brandAgencyDataProperty = yb.brandAgencyDataProperty
    createTime = yb.createTime
    enName = yb.enName
```

+ Finally, we can insert data which we collected into Jena Fuseki:

```Python
async def insert_test():
    pyfuseki.register.register_common_prefix("http://www.yubin.com/kg/")
    fuseki = AsyncFuseki('http://localhost:3030', 'pyfuseki_db')
    g = Graph()
   
    """测试整个过程"""
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
```

