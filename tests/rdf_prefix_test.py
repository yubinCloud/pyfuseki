import unittest

from pyfuseki import FusekiUpdate
from pyfuseki.rdf import rdf_prefix, NameSpace as ns, rdf_property
from rdflib import URIRef, Graph, Literal, RDF

uri = URIRef

class RdfCase(unittest.TestCase):
    def test_rdf_prefix(self):
        """
        测试 rdf_prefix.py 部分
        """

        @rdf_prefix(prefix='http://example.org/')
        class FirmRdfPrefix1:
            BrandProject: ns

        rp1 = FirmRdfPrefix1()
        self.assertEqual(rp1.BrandProject['123'], URIRef('http://example.org/BrandProject/123'))
        self.assertEqual(rp1.BrandProject.to_uri(), URIRef('http://example.org/BrandProject'))

        @rdf_prefix()
        class FirmRdfPrefix2:
            Event: ns

        rp2 = FirmRdfPrefix2()
        self.assertEqual(rp2.Event.buy, URIRef('http://www.kg.com/Event/buy'))

        def connect_end_with_number_symbol(prefix: str, attr_name: str):
            return prefix + attr_name + '#'

        @rdf_prefix(prefix_connect_strategy=connect_end_with_number_symbol)
        class FirmRdfPrefix3:
            Event: ns

        rp3 = FirmRdfPrefix3()
        self.assertEqual(rp3.Event['1234'], URIRef('http://www.kg.com/Event#1234'))

    def test_rdf_property(self):

        @rdf_property('http://example.org/')
        class DataProperty:
            hasName: uri

        dp = DataProperty()
        self.assertEqual(dp.hasName, URIRef('http://example.org/hasName'))

        @rdf_property()
        class ObjectProperty:
            hasFriend: uri

        op = ObjectProperty()
        self.assertEqual(op.hasFriend, URIRef('http://www.kg.com/hasFriend'))

    def test_fuseki_insert(self):
        @rdf_prefix('http://expample.com/')
        class RdfPrefix():
            Person: ns
            Dog: ns
        rp = RdfPrefix()

        @rdf_property('http://example.org/')
        class ObjectProperty:
            own: uri
        op = ObjectProperty()

        @rdf_property('http://example.org/')
        class DataProperty:
            hasName: uri
        dp = DataProperty()

        g = Graph()
        person = rp.Person['12345']  # 假设 '12345' 是这个人的唯一身份证号
        dog = rp.Dog['56789']  # 假设这只狗也有唯一的 ID 为 ‘56789’
        g.add((person, RDF.type, rp.Person.to_uri()))
        g.add((dog, RDF.type, rp.Dog.to_uri()))
        g.add((person, dp.hasName, Literal('Ryan')))  # 加入了一条三元组，表示 person1 有名字为 'Ryan'
        g.add((dog, dp.hasName, Literal('lucy')))
        g.add((person, op.own, dog))

        fuseki = FusekiUpdate('http://localhost:8500', 'test_db')
        fuseki.insert_graph(g)



if __name__ == '__main__':
    unittest.main()
