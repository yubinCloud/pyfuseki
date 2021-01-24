## Map your owl classes into Python

Depending on your task requirements, you may already have an OWL ontology model. In order to use them in Python, you should create a mapping that enables a Python program to map to the ontology model.

For the various entity classes, we call the ontology entity class **RDF Prefix** because we need to prefix it when we instantiate an object of that type.

How to accomplish this mapping? It's very easy. All you need to do is define an enumeration class which derived from `BaseRdfPrefixEnum` and decorate it with `rdf_prefix`.

Assuming that I have two types of "brand project" and "company" in my ontology model, I should do this:

```python
from pyfuseki.ontology_mapper import rdf_prefix, BaseRdfPrefixEnum
from rdflib import Namespace
from pyfuseki import config

@rdf_prefix
class RdfPrefix(BaseRdfPrefixEnum):
    BrandProject = Namespace(config.COMMON_PREFIX + 'BrandProject')
    Firm = Namespace(config.COMMON_PREFIX + 'Firm')
```



## Map your entity properties into Python

Similar to class mapping in an ontology model, relationships need to be mapped. According to the OWL specification, we divide the relationship into Data Property and Object Property.

You need to do the same as above, just inherit `BaseProperty`.

For example:

```python
from pyfuseki.ontology_mapper import BaseProperty
from rdflib import Namespace
from pyfuseki import config


kg = Namespace(config.COMMON_PREFIX)

class ObjectProperty(BaseProperty):
    """
    本体中所有Object properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    subordinateTo = kg.subordinateTo   # 从属于


class DataProperty(BaseProperty):
    """
    本体中所有Data properties的枚举
    name 为该 property 的 display name， value 为包装了该 property IRI 的 URIRef 对象
    """
    createTime = kg.createTime
    enName = kg.enName
```

