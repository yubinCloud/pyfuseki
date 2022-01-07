## 插入多条 RDF 的简写方法

+ 当多条陈述为同一主语时，可以使用 `RdfUtils.add_dict_to_graph`，示例如下：

```python
from rdflib import Graph, RDF, Literal
from pyfuseki.utils import RdfUtils

g = Graph()

person = rp.Person['12345']
dog = rp.Dog['56789']

RdfUtils.add_dict_to_graph(g, person, {
    RDF.type: rp.Person.to_uri(),
    dp.hasName: Literal('Ryan'),
    op.own: dog
})
```

+ 多条陈述可以组成一个列表，从而使用 `RdfUtils.add_list_to_graph`，示例如下：

```python
from rdflib import Graph, RDF
from pyfuseki.utils import RdfUtils

g = Graph()

person = rp.Person['12345']
dog = rp.Dog['56789']

RdfUtils.add_list_to_graph(g, [
    (person, RDF.type, rp.Person.to_uri()),
    (dog, RDF.type, rp.Dog.to_uri()),
    (person, op.own, dog)
])
```

## 注册全局公有前缀

也许你已经发现了，我们在书写 RdfPrefix、DataProperty 和 ObjectProperty 时，都在装饰器上传入了相同的参数 `http://example.org/`，
如果再定义更多的类的话，可能就需要在更多的地方书写重复的代码， **解决方式** 是注册一个公有的前缀：

```python
import pyfuseki

pyfuseki.register.register_common_prefix('http://expample.com/')
```

这样，在定义 RdfPrefix、DataProperty 和 ObjectProperty 时，我们只需要：

```python
@rdf_prefix()
class RdfPrefix():
    ...


@rdf_property()
class ObjectProperty:
    ...
```

无需再传入参数了。