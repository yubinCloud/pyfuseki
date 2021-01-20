"""

@Time: 2021/1/20 14:14
@File: exceptions.py
"""

class FusekiConnectError(Exception):
    """连接Fuseki时出错"""

    def __init__(self, message: str) -> None:
        super().__init__(message)