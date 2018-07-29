#把mysql数据倒到elasticsearch
import elasticsearch.helpers
from elasticsearch import Elasticsearch
import json, os
# from w3lib.html import remove_tags 

with open(os.path.abspath('../../../../jobdata.json'), 'r') as f:
    print('读取json中....')
    jobdata = json.load(f)
    es = Elasticsearch(hosts=['localhost'], request_timeout=100)

    print('生成actions中....')
    #60w+ too much....

    index = 0
    count = 50
    dataLen = len(jobdata)
    print('开始bulk....')
    while index * count < dataLen:
        print('插入第[%d]批数据' % index)

        actions = [
            {
                '_op_type': 'index',
                '_index': 'job_data',
                '_type': 'job',
                '_source': d
            }   
            for d in jobdata[index * count: (index+1) * count]
        ]

        elasticsearch.helpers.bulk(es, actions)

        index +=1
    
    print('bulk 结束 !!!!!')
