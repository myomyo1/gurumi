## 작성중
import module_MovieComparator
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE

#daum 영화정보 Collection
raw_daum = db_ttolae.raw_daum_movie_info
raw_daum_cursor = raw_daum.find()

daum = db_ttolae.daum_movie_info

for i in range(0,raw_daum_cursor.count()):
    document = raw_daum_cursor.next()
    document['_id'] = document['movie_id'][0]['id']

    daum.save(document)
    print(document)
