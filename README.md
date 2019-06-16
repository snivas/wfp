# Simple ONA FORM Client

## Technologies Used

Python 3.6
Elasticsearch 6.x
Elasticsearch python client
ijson python library

## DB Schema

3 indexes,
1. forms - contains all other items
2. users   -  contains items in users array as a seperate record
3. metadata - contains items in metadata array as a seperate record

/metadata/<id> - where 'id' is the id of metadata. ID is used as document id too
/users/<user> - - where 'user' is the id of metadata. USER is used as document id
/forms/<formid>


## Containerization

All were containerized and was running in a separate docker network

