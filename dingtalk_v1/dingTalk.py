# -*- coding: utf-8 -*-

from saveToMongo import *
from multiprocessing import pool
import pandas as pd
from dingCrawler import dingTalkDataCrawler
from payData import payData,feeData


def main():
    payId,feeId = '付款2.0','报销2.1'
    pay = dingTalkDataCrawler(current_date, payId)
    fee = dingTalkDataCrawler(current_date, feeId)
    cursor = conn.cursor()
    approve = ''
    # for data in pay.get_data():
    #     basic = payData(data).getBasicField()
    #     payRow = payData(data).getPayRow()
    #     approveInfo = payData(data).getApproveInfo()
    #     for item in approveInfo:
    #         if approve is not '':
    #             approve = approve+'/'+item
    #         else:
    #             approve = item
    #     sql = "insert into test (id,name,status,createtime,finishtime,depart,fee_depart,cat,item,project,money,paytime,paytype,payobject,paybank,payaccount,backup,approve) " \
    #           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql,(basic[0],basic[1],basic[2],basic[3],basic[4],basic[5],payRow[0],payRow[1],payRow[2],payRow[4],payRow[5],payRow[6],payRow[7],payRow[8],payRow[9],payRow[10],payRow[12],approve))
    #     conn.commit()

    for data in fee.get_data():
        basic = feeData(data).getBasicField()
        payRow = feeData(data).getPayRow()
        # for i in payRow:
        #     print i
        approveInfo = feeData(data).getApproveInfo()
        for item in approveInfo:
            if approve is not '':
                approve = approve+'/'+item
            else:
                    approve = item
        sql = "insert into test1 (id,name,status,createtime,finishtime,depart,fee_depart,paytype,cat,item,project,money,backup,approve) " \
                  "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(basic[0],basic[1],basic[2],basic[3],basic[4],basic[5],payRow[0],payRow[1],payRow[2],payRow[3],payRow[5],payRow[6],payRow[8],approve))
        conn.commit()


if __name__ == '__main__':
    main()