"""
配置文件
@Time: 2021/1/20 15:12
@Author:
@File: config.py
"""
from motor.motor_asyncio import AsyncIOMotorDatabase
# the common prefix of OWL
COMMON_PREFIX: str = "http://www.kg.com/"

mongo_db: AsyncIOMotorDatabase = None

MONGO_COLLECTION: str = 'uid_store'