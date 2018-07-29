#把mysql数据倒到elasticsearch
import elasticsearch.helpers
from elasticsearch import Elasticsearch
import json, os, time
# from w3lib.html import remove_tags 

with open(os.path.abspath('../../../../jobdata.json'), 'r') as f:
    print('读取json中....')
    jobdata = json.load(f)
    es = Elasticsearch(hosts=['localhost'], timeout=60)

    print('生成actions中....')
    #60w+ too much....

    index = 0
    count = 50
    tryAgainCount = 3
    index_name = 'job_data'

    dataLen = len(jobdata)
    print('开始bulk....')
    while index * count < dataLen:
        print('插入第[%d]批数据' % index)

        actions = [
            {
                '_op_type': 'index',
                '_index': index_name,
                '_type': 'job',
                '_source': d
            }   
            for d in jobdata[index * count: (index+1) * count]
        ]

        errCount = 0
        while errCount < tryAgainCount:
            try:
                elasticsearch.helpers.bulk(es, actions)
                time.sleep(2)
                errCount = tryAgainCount
            except Exception as err:
                print('error count '+ str(errCount) +' times', err)
                
                errCount +=1

        index +=1
    
    print('bulk 结束 !!!!!')
