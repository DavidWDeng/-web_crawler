# -*- coding: utf-8 -*-
import json
import requests
from settings import *


class dingTalkDataCrawler(object):

    def __init__(self, current_date, processName):
        self.currentDate = current_date
        self.processName = processName

    def get_data(self):
        data = {
            'appkey': appkey,
            'createFrom': create_from,
            'createTo': self.currentDate,
            'finishFrom': create_from,
            'finishTo': self.currentDate,
            'limit': 20,
            'page':1,
            'processCode': processCode.get(self.processName)
        }
        res = requests.post(url=searchUrl,data=data,headers=headers)
        if res.status_code == 200:
            print '查询成功'
            search_result = json.loads(res.text)
            search_data = search_result.get('data')
            values = search_data.get('values')
            for value in values:
                processInstanceId = value.get('processInstanceId')
                data = {
                    'procInstId': processInstanceId
                }
                res = requests.post(url=instanceDataUrl, data=data, headers=headers)
                if res.status_code == 200:
                    print '获取数据成功'
                    result = json.loads(res.text)
                    datas = result.get('data')
                    yield datas