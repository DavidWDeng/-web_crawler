# -*- coding: utf-8 -*-

from paserData import parserData

class payData(parserData):

    def getPayRow(self):
        list = []
        l = []
        for row in self.getRowValue():
            for item in row:
                field = item.get('value')
                label = item.get('label')
                if label == u'归属部门':
                    result = field[0]
                elif label != u'说明' and type(field) != dict:
                    result = field
                else:
                    result = None
                list.append(result)
        return list

class feeData(parserData):

    def getPayRow(self):
        list = []
        l = []
        for row in self.getRowValue():
            for item in row:
                field = item.get('value')
                label = item.get('label')
                if label == u'归属部门':
                    result = field[0]
                elif label != u'说明' and type(field) != dict:
                    result = field
                else:
                    result = None
                list.append(result)
        return list
