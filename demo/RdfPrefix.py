"""

@Time: 2021/1/20 18:07
@Author:
@File: RdfPrefix.py
"""
from pyfuseki.ontology_mapper import rdf_prefix, BaseRdfPrefixEnum
from rdflib import Namespace
from pyfuseki import config

@rdf_prefix
class RdfPrefix(BaseRdfPrefixEnum):
    BrandProject = Namespace(config.COMMON_PREFIX + 'BrandProject')
    Firm = Namespace(config.COMMON_PREFIX + 'Firm')
