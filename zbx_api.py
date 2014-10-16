#!/usr/bin/python
#coding:utf-8

#author:leon
#用来实现zabbix api


import requests
import json
import sys
import random

PASS = ''
URL = 'http://xxx/api_jsonrpc.php'
headers = {'content-type': 'application/json'}

def get_auth():
    login_req = { "jsonrpc": 2.0, 
        "method": 
        "user.login", 
        "params": { 
            "user": "admin", 
            "password": PASS
        }, 
        "id": random.randrange(10)  
    }
    
    r = requests.post(URL, data=json.dumps(login_req), headers=headers)
    return r

def get_json(auth_token='1', auth_id=1, method={}):
    method['id'] = auth_id
    method['auth'] = auth_token
#    print method
#    print "#"*30

    res_method = requests.get(URL,data=json.dumps(method), headers=headers)
    print json.dumps(res_method.json(), indent=2)


try:
    fname = sys.argv[1]
    data = json.loads(open(fname,'r').read())
#    print '='*30
#    print data
#    print type(data)
#    print '='*30
except IndexError:
    print "输入json数据的文件名"
    sys.exit(1)

r = get_auth()

auth_token = r.json()['result']
auth_id = r.json()['id']

get_json(auth_token, auth_id, data)
