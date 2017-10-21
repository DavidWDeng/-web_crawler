# -*- coding: utf-8 -*-
import os,datetime,MySQLdb
#响应信息配置
headers = {
    'Accept':'application/json, text/plain, */*',
    'Origin':'https://aflow.dingtalk.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer':'https://aflow.dingtalk.com/dingtalk/web/query/processDesign',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie':'##########################'
}
appkey ='##########'

#时间参数配置
create_from = '2017-09-13'
current_date = datetime.date.today()

#流程编码配置
processCode = {
    '付款2.0':'PROC-EF6YRO35P2-UYCKQJC0PZPTVE9CF3TX1-CMYF672J-832',
    '报销2.1':'PROC-FF6YLZF1N2-Z0XJ7RIEN0BHM1V29YRB3-ADZXKD1J-6F'
}

#爬去链接配置
saveDataExportUrl = 'https://aflow.dingtalk.com/dingtalk/web/query/instdata/saveDataExportJobForInstances.json'
searchUrl = 'https://aflow.dingtalk.com/dingtalk/web/query/instdata/getInstancesByQuery.json'
instanceDataUrl = 'https://aflow.dingtalk.com/dingtalk/pc/query/form/getInstDetailData.json'
getFileInfoUrl = 'https://aflow.dingtalk.com/dingtalk/web/query/instdata/getDataExportRecords.json'
downloadFileUrl = 'https://aflow.dingtalk.com/dingtalk/web/instdata/filehandle?'

#保存路径配置
filePath = os.getcwd()+'\\dingding\\'

#服务器配置
MONGO_URL = '172.16.0.70'
MONGO_DB = 'dingtalk'
MONGO_TABLES = {
    '付款2.0' : 'pay',
}
conn = MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306,db='test',charset='utf8')


#基本字段配置
basicFields = [u'pmc_business_id',u'procInstTitle',u'result',u'createTime',u'finishTime',u'originatorDeptName']
