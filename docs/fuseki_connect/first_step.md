## Overview

We provide two ways to connect **Fuseki**: sync and async. You can use one of the two ways depending on your program structure.

+ For synchronous methods, we have `FusekiQuery` and `FusekiUpdate` for you to use.

+ For asynchronous methods, we have `AsyncFuseki` for you to use.

>  Notice, Asynchronous requires Python's async / await syntax.

## Initialize your instance

### Sync Fuseki

It is a easy way for you to connect Fuseki, and it's easier to use our library. If you want to query data from Jena, you should use `FusekiQuery`. But if you want to insert RDF data into Jena, the `FusekiUpdate` may suit for you.

They have the same form of parameters: `fuseki_url` and `dataset_name`.

For example, if my Fuseki endpoint URL is `localhost:3030`, and my dataset's name is `test_db`, I should initialize my Fuseki instance like this:

```python
from pyfuseki import FusekiUpdate, FusekiQuery

fuseki_update = FusekiUpdate('localhost:3030', 'test_db')
fuseki_query = FusekiQuery('localhost:3030', 'test_db')
```

### Async Fuseki

If you want to use Fuseki as a coroutine way, `AsyncFuseki` will be a favorite.

```python
from pyfuseki import AsyncFuseki

async_fuseki = AsyncFuseki('localhost:3030', 'test_db')
```

