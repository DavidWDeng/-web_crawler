#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:wei.deng 
@file: dingtalkCrawler.py 
@time: 2017/10/17 
"""

import requests,json,pymongo
from settings import *

def get_token():
    res = requests.get(url=token_url,headers=token_header)
    result = json.loads(res.text)
    data = result.get('data')
    token = data.get('token')
    return token

def crawler(func):
    for tableId in tableIds.values():

        payload = {
            "tableId": tableId, "pageSize": 200, "offset": 0, "orderBy": [],
            "condition": [{"type": "DATE_AREA", "value": "2016-01-01,2017-10-25", "name": "finish_time"},
                          {"type": "DEPT_IDS", "value": ""}, {"type": "CREATOR_USER_IDS", "value": ""}]
        }
        data_header = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'content-length': '139',
            'content-type': 'application/json',
            'cookie': 'JSESSIONID=2D84ADF3A80770A3AAD3BCF9793F18CF; sid=2D84ADF3A80770A3AAD3BCF9793F18CF; USER_TOKEN=eyJ2YWx1ZSI6IncwODE1NDgzNDdjYmJlM2Q2ZTVhZDViMWYwMDgzYTgyNDA1MDExNDM2NGYwNDE4ZGRmNWMwNjdlMjRlN2YyN2M3ZjE2NzIzY2JiMDJlYjg1ZmM0NGU1ZDVkNTkzMTM2ZGY1YWVmZmI0YjhhNWMwNTE0ZDllOGEzN2Q5ZmE0MGRhMDYiLCJjb3JwSWQiOiJkaW5nODg4NzZiODIxZmFiZmIxNiJ9; cna=4fNSEc8+tlwCAXeDjnhxNPhs; isg=AlBQD1fCPTZaMuF1X823gfczIZ5isWwHmvukWUohHKt-hfAv8ikE86a3K3ue',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'x-csrf-token': get_token()
        }
        res = requests.post(url=data_url, json=payload, headers=data_header)
        res = json.loads(res.text)
        results = res.get('data')
        datas = results.get('data')
        for data in datas:
            client = pymongo.MongoClient(MONGO_URL)
            db_auth = client.admin
            db_auth.authenticate(USERNAME, PASSWORD)
            db = client[MONGO_DB]
            if db[MONGO_TABLES.get(tableId)].insert(data):
                print('存储成功')

def main():
    token = get_token()
    crawler(token)


if __name__ == '__main__':
    main()