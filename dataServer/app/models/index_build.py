#创建index
from elasticsearch_dsl import DocType, Date, Boolean, analyzer, Completion, Keyword, Text, Integer
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])

class JobType(DocType):
    job_id = Keyword()
    job_url = Keyword()
    job_name = Text(analyzer='ik_max_word')
    company = Text(analyzer='ik_max_word')
    salary = Keyword()
    work_location = Text(analyzer='ik_max_word')
    required = Text(analyzer='ik_max_word')
    welfare_list = Text(analyzer='ik_max_word')
    job_describe = Text(analyzer='ik_max_word')
    publish_time = Date(format='yyyy-MM-dd HH:mm:ss')
    crawl_time = Date(format='yyyy-MM-dd HH:mm:ss')

    class Meta:
        index = 'job_data2'
        doc_type = 'job'

if __name__ == '__main__':
    JobType.init()
    # pass
