An asynchronous query on Fuseki requires the use of Python's async / await syntax. This query is implemented with the help of the [httpx](https://www.python-httpx.org/) open source library which can send requests asynchronously.

## 1. Initialize the instance

```python
from pyfuseki import AsyncFuseki

async_fuseki = AsyncFuseki('localhost:3030', 'test_db')
```

## 2. Construct SPARQL statement

```python
sparql_str = """
    SELECT *
    WHERE { ?s ?p ?o };
"""
```

## 3. Run the SPARQL statement

Note that unlike synchronous, we need the await keyword to get the result of the query. 

The query result is of type `AsyncFusekiResp` which is a type that wraps the query response.

```python
query_result = await async_fuseki.query_sparql(sparql_str)
```

## 4. Call it with asyncio

Because it is asynchronous, it cannot be run directly as a normal program. You need to wrap it with the **async function** and run it with **asyncio**.

For example:

```python
from pyfuseki import AsyncFuseki
import asyncio

async def select_all():
    async_fuseki = AsyncFuseki('localhost:3030', 'test_db')

    sparql_str = """
        SELECT *
        WHERE { ?s ?p ?o };
    """

    return await async_fuseki.query_sparql(sparql_str)

query_result = asyncio.run(select_all())
```

