# -*- coding: utf-8 -*-
import random
import requests
from proxy_util import logger
from run import fifo_queue
from settings import USER_AGENT_LIST
from proxy_util import base_headers

# 测试地址
url = 'http://blog.csdn.net/pengjunlee/article/details/90174453'

# 获取代理
proxy = fifo_queue.pop(schema='http')
proxies = {proxy.schema:proxy._get_url()}

# 构造请求头
headers = dict(base_headers)
if 'User-Agent' not in headers.keys():
    headers['User-Agent'] = random.choice(USER_AGENT_LIST)

response = None
successed = False
try:
    response = requests.get(url,headers=headers,proxies = proxies,timeout=5)
    print(response.content.decode())
    if (response.status_code == 200):
        successed = True
        logger.info("使用代理< "+proxy._get_url()+" > 请求 < "+url+" > 结果： 成功 ")
except:
    logger.info("使用代理< "+proxy._get_url()+" > 请求 < "+url+" > 结果： 失败 ")

# 根据请求的响应结果更新代理
proxy._update(successed)
# 将代理返还给队列，返还时不校验可用性
fifo_queue.push(proxy,need_check=False)
