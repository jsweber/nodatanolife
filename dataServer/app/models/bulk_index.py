#es bulk插入数据demo
#查询练习
# client = Elasticsearch()
# resp = client.search(
#     index='jobtest2',
#     body= {
#         "query": {
#             "match": {
#                 "job_name": "web"
#             }
#         }
#     }
# )

# for hit in resp['hits']['hits']:
#     print(hit['_source'])

import elasticsearch.helpers
from elasticsearch import Elasticsearch

testData = [
    {'request_list': ['html5', '扎实的就是js基础'], 'salary': '30万', 'company': {'name': '百度', 'tags': ['bat', '世界500强', '互联网']}, 'work_location': '北京', 'pushlish_time': '2018-12-10 08:00:00', 'job_name': 'web前端工程师_bulk9'},
    {'request_list': ['html5', '扎实的就是js基础'], 'salary': '30万', 'company': {'name': '百度', 'tags': ['bat', '世界500强', '互联网']}, 'work_location': '北京', 'pushlish_time': '2018-12-10 08:00:00', 'job_name': 'web前端工程师_bulk9_2'},
    {'request_list': ['html5', '扎实的就是js基础'], 'salary': '30万', 'company': {'name': '百度', 'tags': ['bat', '世界500强', '互联网']}, 'work_location': '北京', 'pushlish_time': '2018-12-10 08:00:00', 'job_name': 'web前端工程师_bulk9_3'}]

actions = [
    {
        '_op_type': 'index',
        '_index': 'jobtest2',
        '_type': 'job',
        '_source': d
    }   
    for d in testData
]

es = Elasticsearch(hosts=['localhost'])
elasticsearch.helpers.bulk(es, actions)
# elasticsearch.helpers.streaming_bulk(es, actions)

