"""

@Time: 2021/1/20 14:16
@Author:
@File: fuseki_resp.py
"""
import httpx
from typing import List, Dict, Mapping
from pyfuseki.model.BindingItem import BindingItem


class AsyncFusekiResp:
    def __init__(self, resp: httpx.Response):
        self.resp = resp

    def get_vars(self):
        return self.resp.json().get('head').get('vars')

    def get_bindings(self):
        return self.resp.json().get('results').get('bindings')

    @staticmethod
    def binding_to_models(binding: dict) -> Dict[str, BindingItem]:
        """
        Converts the Binding dict to a dict with the value of BindingItem.
        :param binding: The target to be converted.
        :return: The converted dict.
        """
        return {
            var: BindingItem(**value) for (var, value) in binding.items()
        }

    def to_bindingItemModels(self) -> List[Mapping[str, BindingItem]]:
        """
        Gets the result of the query consisting of BindingItem values
        """
        bindings = self.get_bindings()
        return [
            self.binding_to_models(binding) for binding in bindings
        ]
