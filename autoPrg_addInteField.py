import module_trimStr
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE


###########다음##########
# collection_daum_movie_info = db_ttolae.daum_movie_info
# daum_cursor = collection_daum_movie_info.find()
# # collection_inte_daum_movie_info = db_ttolae.inte_daum_movie_info
#
# for i in range(0,daum_cursor.count()) :
#     document = daum_cursor.next()
#     result = module_trimStr.trimStr(document['movie_title'])
#     document.update({"inte_title" :result})
#
#     d_result = module_trimStr.trimStr(document['director'])
#     document.update({"inte_director" :d_result})
#
#     print(document)
#     collection_daum_movie_info.save(document)


############진흥원##########
# collection_jin_movie_info = db_ttolae.jin_movie_info
# # collection_inte_jin_movie_info = db_ttolae.inte_jin_movie_info
# jin_cursor = collection_jin_movie_info.find()
#
# for i in range(0,jin_cursor.count()) :
#     document = jin_cursor.next()
#     result = module_trimStr.trimStr(document['movie_title'])
#     document.update({"inte_title" :result})
#
#     d_result = module_trimStr.trimStr(document['director'])
#     document.update({"inte_director" :d_result})
#
#     print(document)
#     collection_jin_movie_info.save(document)


############CGV##########

# collection_cgv_movie_info = db_ttolae.cgv_movie_info
# cgv_cursor = collection_cgv_movie_info.find()
# # collection_inte_cgv_movie_info = db_ttolae.inte_cgv_movie_info
#
# for i in range(0,cgv_cursor.count()) :
#     document = cgv_cursor.next()
#     result = module_trimStr.trimStr(document['movie_title'])
#     document.update({"inte_title" :result})
#
#     d_result = module_trimStr.trimStr(document['director'])
#     document.update({"inte_director" :d_result})
#
#     print(document)
#     collection_cgv_movie_info.save(document)


###########네이버##########
collection_naver_movie_info = db_ttolae.naver_movie_info
naver_cursor = collection_naver_movie_info.find()

for i in range(0,naver_cursor.count()) :
    document = naver_cursor.next()
    result = module_trimStr.trimStr(document['movie_title'])
    document.update({"inte_title" :result})

    d_result = module_trimStr.trimStr(document['director'])
    document.update({"inte_director" :d_result})
#
    print(document)
    collection_naver_movie_info.save(document)