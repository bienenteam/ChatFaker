import couchdb
import time
from faker import Faker
fake = Faker()

couch = couchdb.Server('http://admin:bienengebenhonig@93.180.156.188:5984/')
db = couch['beehive']

while True:

    doc = {
        'type': 'item',
        'schemaversion': '2',
        'id': fake.uri(),
        'link': fake.uri(),
        'published': fake.iso8601(),
        'updated': '',
        'title': fake.sentences(nb=1)[0],
        'summary': fake.text(),
        'content': fake.text(max_nb_chars=5000),
        'author': {'name': 'Chat Faker'},
        'feedId': '8e8b81a1f813c572d15a2551bef1b74b'
    }

    result = db.save(doc)
    print(result[0] + ' - ' + doc['title'])
    time.sleep(5);
