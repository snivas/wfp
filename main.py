from client import ONAClient
from DB import DB 
import ijson


client = ONAClient('https://api.ona.io/api/v1/')
dbconn = DB('elasticsearch')
resp_obj = client.getFORM('185260')


#Inserts metadata list items as seperate record under 'metadata'
rec = ijson.items(resp_obj, 'metadata.item')
for r in rec:
    dbconn.insertRecord('metadata', r['id'], r)


#Inserts users list items as seperate record under 'users'
rec = ijson.items(resp_obj, 'users.item')
for r in rec:
    dbconn.insertRecord('users', r['user'], r)

#Other common docs are inserted in to 'forms' index
dbconn.insertRecord('forms', r['formid'], resp_obj.read())
