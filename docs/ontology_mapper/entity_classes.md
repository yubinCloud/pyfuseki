## Map your ontology into python Enum

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



