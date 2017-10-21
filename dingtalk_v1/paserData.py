# -*- coding: utf-8 -*-
import json
from settings import *


class parserData(object):

    def __init__(self,data):
        self.data = data

    def getBasicField(self):
        list =[]
        for basicField in basicFields:
            if basicField == u'createTime' or basicField == u'finishTime':
                field = self.data.get(basicField)
                field = datetime.datetime.fromtimestamp(field/1000)
                # yield field
            elif basicField == u'pmc_business_id' or basicField == u'procInstTitle'or basicField == u'originatorDeptName':
                formData = self.data.get('formData')
                field = (formData.get(basicField)).get('value')
                # yield field
            else:
                field = self.data.get(basicField)
                # yield field
            list.append(field)
        return list

    def getRowValue(self):
        formData = self.data.get('formData')
        TableField_MINGXI = formData.get('TableField-MINGXI')
        values = json.loads(TableField_MINGXI.get('value'))
        for value in values:
            rowValue = value.get('rowValue')
            yield rowValue

    def getApproveInfo(self):
        approveInfo = self.data.get('approveInfo')
        list = []
        for item in approveInfo:
            action = item.get(u'action')
            operateTime = datetime.datetime.fromtimestamp((item.get(u'operateTime')/1000))
            operatorName = item.get(u'operatorName')
            a = operatorName+'_'+action+'_'+str(operateTime)
            list.append(a)

        return list