#把mysql数据倒到elasticsearch
import elasticsearch.helpers
from elasticsearch import Elasticsearch
import json, os, time, sys
# from w3lib.html import remove_tags 

def dumpes(data_name, start=0, count=50):
    with open(os.path.abspath('../../../../jobdata.json'), 'r') as f:
        print('读取json中....')
        jobdata = json.load(f)
        es = Elasticsearch(hosts=['localhost'], timeout=60)

        print('生成actions中....')
        #60w+ too much....

        index = start
        tryAgainCount = 3
        index_name = data_name

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

            elasticsearch.helpers.bulk(es, actions)
            time.sleep(2)

            index +=1
        
        print('bulk 结束 !!!!!')

if __name__ == '__main__':
    data_name = None
    start = 0
    count = 50
    try:
        data_name = sys.argv[1]
        start = int(sys.argv[2])
        count = int(sys.argv[3])
    except Exception as e:
        print('first param is index name; second is start; third is count')
    if not data_name:
        dumpes(data_name, start, count)
    else:
        print('index name is must')
