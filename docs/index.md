# PyFuseki
<p align="center"><strong>pyfuseki</strong> <em>- An easy way to mix together OWL and Jena Fuseki.</em>   
</p>
<p>
<img src="https://img.shields.io/github/license/yubinCloud/pyfuseki">
</p>

一个用来连接并操作 Apache Jena Fuseki 的 Python 库，同时提供了同步和异步的两种操作方式。通过使用它，你可以很简单地将你的数据插入 Fuseki 中。

---

**Documentation**: <a href="https://yubincloud.github.io/pyfuseki/" target="_blank">https://yubincloud.github.io/pyfuseki/</a>

**Source Code**: <a href="https://github.com/yubinCloud/pyfuseki" target="_blank">https://github.com/yubinCloud/pyfuseki</a>

---
## Requirements

Python 3.6+

PyFuseki 基于以下三个库来实现任务:

+ [Pydantic](https://pydantic-docs.helpmanual.io/) 负责数据部分.
+ [httpx](https://www.python-httpx.org/) 负责网络部分.
+ [rdflib](https://rdflib.readthedocs.io/en/stable/) 负责对 RDF 的操作.

## Installation

```console
$ pip install pyfuseki
```

## Example

这里有个简单的例子来演示如何将你的数据插入到 Fuseki 中，先不用究于细节，之后我们会对每一部分进行讲解。

+ 首先，我们先按照本体来定义出里面的类，以方便实例化数据：

```Python
from pyfuseki.rdf import rdf_prefix, NameSpace as ns

@rdf_prefix('http://expample.com/')
class RdfPrefix():
    Person: ns
    Dog: ns

rp = RdfPrefix()
```

+ 接下来，我们按照本体中来定义出里面的关系（属性），以方便表示该关系：

```Python
from pyfuseki.rdf import rdf_property
from rdflib import URIRef as uri

@rdf_property('http://example.org/')
class ObjectProperty:
    own: uri 

@rdf_property('http://example.org/')
class DataProperty:
    hasName: uri
```

+ 最后，我们实例化出一些数据，并将其相关陈述（三元组）插入到图中：

```Python
from pyfuseki import FusekiUpdate
from rdflib import Graph, Literal, RDF

g = Graph()

# 实例化数据
person = rp.Person['12345']  # 假设 '12345' 是这个人的唯一身份证号
dog = rp.Dog['56789']  # 假设这只狗也有唯一的 ID 为 ‘56789’

# 将陈述加入到图中
g.add((person, RDF.type, rp.Person.to_uri()))  # 声明 person 的类型是 Person
g.add((dog, RDF.type, rp.Dog.to_uri()))
g.add((person, dp.hasName, Literal('Ryan')))  # 加入了一条三元组，表示 person1 有名字为 'Ryan'
g.add((dog, dp.hasName, Literal('lucy')))
g.add((person, op.own, dog))

# 把图插入到 Fuseki 中
fuseki = FusekiUpdate('http://localhost:3030', 'test_db')
fuseki.insert_graph(g)
```

