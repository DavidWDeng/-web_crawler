#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:wei.deng
@file: settings.py
@time: 2017/10/16
"""
tableIds = {
    'pay2.0':57737,
    'pay2.1':76733,
    'fee2.1':53140,
    'emergency_payment':76735,
    'mkt_design':99791,
    'software_add_func':99789,
    'software_account':99787,
    'stamp2.0':77121,
    'product_apply':66260,
    'print_apply':62547,
    'IT_account':60669,
    'meeting_room_apply':60492,
    'training_needs':52946,
    'training_apply':44191,
    'labor_cost':44190,
    'manpower_needs':33099,
    'fee':32588,
    'pay':32562,
    'invoice':39526,
    'flow':33085,
    'out_table':33081,
    'contract':32560,
    'purchase_request':32655,
    'stamp1.0':33072,
    'business_travel':32632,
    'order':46198,
    'borrowing':33080,
    'invest':33074,
    'pay0.1':32998,
    'project_apply':39977
}
#请求配置信息
token_url = 'https://clouddata.dingtalkapps.com/alid/sst/csrf/getCsrfToken'
token_header = {
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'cookie':'########',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

data_url = 'https://clouddata.dingtalkapps.com/alid/sst/tableInfo/queryDatas'
data_header = {
    'accept':'application/json',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'content-length':'139',
    'content-type':'application/json',
    'cookie':'#######',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'x-csrf-token':'######'
}

#数据库配置
MONGO_URL = '172.16.0.58'
MONGO_DB = 'dingtalk'
USERNAME = 'root'
PASSWORD = 'ezlife'
MONGO_TABLES = {
    57737:'pay2.0',
    76733:'pay2.1',
    53140:'fee2.1',
    76735:'emergency_payment',
    99791:'mkt_design',
    99789:'software_add_func',
    99787:'software_account',
    77121:'stamp2.0',
    66260:'product_apply',
    62547:'print_apply',
    60669:'IT_account',
    60492:'meeting_room_apply',
    52946:'training_needs',
    44191:'training_apply',
    44190:'labor_cost',
    33099:'manpower_needs',
    32588:'fee',
    32562:'pay',
    39526:'invoice',
    33085:'flow',
    33081:'out_table',
    32560:'contract',
    32655:'purchase_request',
    33072:'stamp1.0',
    32632:'business_travel',
    46198:'order',
    33080:'borrowing',
    33074:'invest',
    32998:'pay0.1',
    39977:'project_apply'
}


