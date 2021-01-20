"""

@Time: 2021/1/20 16:51
@Author:
@File: global_namespace_manager.py
"""
from rdflib.namespace import NamespaceManager
from rdflib import Graph

from pyfuseki.ontology_mapper.prefixes import get_prefix_enum_store


class GlobalNamespaceManager:
    """
    The class used to get the global namespace manager. It cannot be instantiated.
    """
    def __new__(cls, *args, **kwargs):
        raise Exception('GlobalNamespaceManager class cannot be instantiated')

    __has_produce_manager = False  # 标识是否已经生成了全局的namespace manager
    __global_namespace_manager = None  # 保存全局的namespace manager

    @staticmethod
    def get() -> NamespaceManager:
        """
        获取到类中保存的全局namespace manager
        :return: 全局namespace manager

        Examples
        --------
        >>> nm = GlobalNamespaceManager.get()
        """
        if GlobalNamespaceManager.__has_produce_manager == False:
            nm = NamespaceManager(Graph())
            prefix_enum_store = get_prefix_enum_store()
            for PrefixEnumType in prefix_enum_store:
                for name, member in PrefixEnumType.__members__.items():
                    nm.bind(name, member.value)
            GlobalNamespaceManager.__global_namespace_manager = nm
        return GlobalNamespaceManager.__global_namespace_manager