from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')

db_ttolae = client.TTOLAE

collection_movie = db_ttolae.movie


obj_movie = collection_movie.find({"movie_title": "꼴찌부터 일등까지 우리반을 찾습니다 "})

import module_MovieComparator

dict_test = { "movie_id" : [ { "site" : "daum", "id" : 659 } ], "movie_title" : "꼴찌부터 일등까지 우리반을 찾습니다", "director" : "황규덕", "attendance" : 2, "score" : [ { "site" : "daum", "grade" : "4.0" } ] }

module_MovieComparator.compare(collection_movie, dict_test, "movie_title", "director")


i = 0
while i < obj_movie.count():
    print(obj_movie.count())
    print(obj_movie.next())
    i = i+1
