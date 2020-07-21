#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: cxa
@contact: 1598828268@qq.com
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: http_request.py
@time: 2020/7/6 20:40
"""

import requests
def http_request(url,data,token=None,method="post"):
    headers= {"X-Lemonban-Media-Type": "lemonban.v2", "Authorization":token}
    if method=="get":
        result = requests.get(url, json=data, headers=headers)
    else:
        result = requests.post(url, json=data, headers=headers)
    return result.json()

if __name__ == '__main__':

    log_url= "http://120.78.128.25:8766/futureloan/member/login"
    log_data= {"mobile_phone": "18833030719", "pwd": "123456789"}
    response=http_request(log_url,log_data)
    token=response["data"]["token_info"]["token"]
    rec_url="http://120.78.128.25:8766/futureloan/member/recharge"
    rec_data={"member_id":2268,"amount":"5000"}
    print(http_request(rec_url,rec_data,"Bearer "+token))
