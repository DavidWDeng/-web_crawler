# -*- coding: utf-8 -*-
import json
from urllib import urlencode
import datetime
import requests
from settings import *
from multiprocessing import pool

#导出当天数据文件
def save_Data_Export(currentDate):
    data = {
            'appkey': 'ding88876b821fabfb16',
            'createFrom':2017-01-01,
            'createTo': currentDate,
            'finishFrom':'2017-09-08',
            'finishTo':'2017-09-08',
            'limit':10,
            'processCode':'PROC-EF6YRO35P2-UYCKQJC0PZPTVE9CF3TX1-CMYF672J-832'
    }
    res = requests.post(url=saveDataExportUrl,data=data,headers=headers)
    if res.status_code == 200:
        print res.text
    return None

#获取导出文件信息字段
def get_fileInfo():
    data = {
        'limit':10,
        'page':1
    }
    res = requests.post(url=getFileInfoUrl,data=data,headers = headers)
    result = json.loads(res.text)
    data = result.get('data')
    values = data.get('values')
    for value in values:
        print value.get('fileId'),value.get('processName'),value.get('fileName')[0:17]

#下载数据文件
def download_file(fileId,processName,fileName):
    filename = {
        'fileId':fileId
    }
    geturl = downloadFileUrl+urlencode(filename)
    res2 = requests.get(url=geturl,headers = headers)
    result = res2.content
    with open(filePath+processName+'_'+fileName+'.xls', 'wb') as file:
        file.write(result)
        file.close()

def main():
    currentDate = datetime.date.today()
    print currentDate
    save_Data_Export(currentDate)
    '''for fileId, processName,fileName in'''
    # get_fileInfo()
        # download_file(fileId,processName,fileName)

if __name__ == '__main__':
    main()
