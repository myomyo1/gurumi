from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE

#cgv 영화정보 Collection
raw_cgv = db_ttolae.raw_cgv_movie_info
raw_cgv_cursor = raw_cgv.find()

cgv = db_ttolae.cgv_movie_info

for i in range(0,raw_cgv_cursor.count()):
    document = raw_cgv_cursor.next()
    document['_id'] = document['movie_id'][0]['id']

    cgv.save(document)
    print(document)
