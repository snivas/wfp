from elasticsearch import Elasticsearch

class DB(object):

    def __init__(self, url):
        self.dbconn = Elasticsearch(url)

    def insertRecord(self, idx, recid, rec):
        if not rec:
            rec = {}
        self.dbconn.create(index=idx, doc_type="default", 
                id= recid, body={"doc": rec})

