import couchdb
from faker import Faker
fake = Faker()

couch = couchdb.Server('http://admin:bienengebenhonig@93.180.156.188:5984/')
db = couch['simdata']

doc = {
    'type': 'item',
    'schemaversion': '1',
    'id': fake.uri(),
    'link': fake.uri(),
    'published': fake.iso8601(),
    'updated': '',
    'title': fake.sentences(nb=1)[0],
    'summary': fake.text(),
    'content': fake.text(max_nb_chars=5000),
    'author': {'name': 'Chat Faker'}
}
result = db.save(doc)
print(result)
