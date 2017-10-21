# -*- coding: utf-8 -*-
import pymongo
from settings import *

def saveToMongo(data, processname):
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    if db[MONGO_TABLES.get(processname)].insert(data):
        print('存储成功')
        return True
    return False