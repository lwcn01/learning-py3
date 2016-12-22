#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"
import re
import socket
import json
import requests

def pageData(url,page = 0,SN = None):
    if page < 0:
        page = 0
    else:
        page = int(page)
    payload = {'SN': '%s' % SN, 'results_per_page': '%s' % page}
    r = requests.get(url, params=payload)
    return r.json()

def analyseJson(path,url,page = 0,SN = None,ip = None):
    get_json = pageData(url,page = 0,SN = None)  # json格式的文本
    #get_json.keys()
    data = get_json['channel_list']
    json_list = []
    for value in data:
        json_dict = {}
        for k,v in value.items():
            if k == 'title':
                json_dict.setdefault(k,v)
            elif k == 'third_party_address':
                json_dict.setdefault(k,v)
        json_list.append(json_dict)
    with open(path,'w') as json_file:
        for json_value in json_list:
            json_file.write(json.dumps(json_value,ensure_ascii=False))
            json_file.write("\n")
    saveFile(path,ip)
    
def saveFile(path,ip):
    ip_path = "C:\\Users\\Administrator\\Desktop\\ip.json"
    if ip == "ip":
        ip_file = open(ip_path,'w')
        with open(path,'r') as txt_file:
            for txt_value in txt_file.readlines():
                # 一行一行读取json文件,返回的是str
                json_value = json.loads(txt_value)
                value = json_value["third_party_address"]
                url_list = []
                for v in value:
                    domain_list = re.findall(r"://([a-zA-Z0-9]+?\S*?)/",v)
                    # 将域名转换为ip
                    domain = domain_list[0]
                    ip = socket.gethostbyname(domain)
                    # 替换url中域名
                    v = v.replace(domain,ip)
                    url_list.append(v)
                json_value["third_party_address"] = url_list
                ip_file.write(json.dumps(json_value,ensure_ascii=False))
                ip_file.write("\n")
        ip_file.close()

if __name__ == '__main__':
    url = "http://four.epg.com:8080/api/phone/aggregator/epg/live/product/922719cd-afdc-3756-8620-270acde64a78/category/a552e83a-d852-4df8-b746-32d9e8751e9c/program"
    path = "C:\\Users\\Administrator\\Desktop\\json.json"
    analyseJson(path,url)
    #analyseJson(path,url,ip='ip')