Synchronously querying Fuseki can often be a performance bottleneck, so we prefer to use asynchronous querying. However, this approach to synchronization is often simpler. Therefore, we first try to use synchronous mode to connect Jena Fuseki and query the data.

## 1. Initialize the instance

The method of initialization was introduced in the previous section. All we need here is an instance of FusekiQuery.

```python
from pyfuseki import FusekiQuery

fuseki_query = FusekiQuery('localhost:3030', 'test_db')
```

## 2. Construct SPARQL statement

Jena Fuseki supports SPARQL statements for direct queries, so we need to construct the appropriate query statements as needed.

```python
sparql_str = """
    SELECT *
    WHERE { ?s ?p ?o };
"""
```

## 3. Run the SPARQL statement

Our connection and query with Fuseki actually relied on another open source library: [SPARQLWrapper](https://sparqlwrapper.readthedocs.io/en/stable/). `FusekiQuery` actually acts as an proxy for this process. So, you can find that the type of `query_result` actually is `SPARQLWrapper.Wrapper.QueryResult`. If you want to parse this result, we also provide some useful tools for you. But if you want study it deeply, the document of **SPARQLWrapper** will be a good idea.

```python
query_result = fuseki_query.run_sparql(sparql_str)
```

