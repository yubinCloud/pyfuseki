from rdflib import Namespace
from pyfuseki import config
from pyfuseki.ontology_mapper import rdf_prefix, BaseRdfPrefixEnum, show_all_prefixes

@rdf_prefix
class MyPrefix(BaseRdfPrefixEnum):
    Company = Namespace(config.COMMON_PREFIX + "Company")


if __name__ == '__main__':
    show_all_prefixes()