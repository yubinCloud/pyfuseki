## 基本概念

Apache Jena Fuseki 是一个可以接收和处理 SPARQL 的服务，能够存储 RDF 数据。

RDF 以三元组的形式来表达知识，形式为 `<subject predicate object>`，即由主谓宾三部分构成，也称为一条 **陈述** 。

主语和谓语都是由 IRI 表示，但由于 IRI 与 URI 十分相似，所以我们常常将这两个术语混用，在 rdflib 库中使用 `URIRef` 来表示。宾语可以是 URI，也可以是文字型，在 rdflib 库中使用 `Literal` 表示。

让我们观察一下一个 URI，假设一个叫做 Ryan 的人为 `<http://example.org/person/Ryan>` ，另一个叫做 Daisy 的人为 `<http://example.org/person/Daisy>`，由此我们可以发现，一个 URI 可以将其拆成两部分来看待： **URI = 前缀 + 后缀** ，其中所有表示“人”这个概念的个体都拥有前缀 `http://example.org/person/`，而不同的个体有不同的唯一后缀，从而实现了每个 URI 的唯一性。

!!! note     
    这种看待方法并不是 RDF 标准所规定的，只是为了方便我们用 python 编程来表达 RDF 数据而发明的。

**关系**（或叫做 **属性** ）在 OWL 中分成了数据属性和对象属性，其中对象属性用来连接两个实例个体，对象属性用来连接个体和文字值。

更多关于语义网的概念可参考 [语义网基础](https://yubincloud.github.io/notebook/pages/d02e4e)

## 启动 Jena Fuseki

下载 Apache Jena Fuseki 后，在目录下运行如下命令行即可启动 Fuseki：
```bash
java -jar fuseki-server.jar -port=PORTNUM
```

+ Fuseki 默认的端口号为 3030