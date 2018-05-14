import module_DaumMovieComparator
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE

add = db_ttolae.raw_daum_movie_info_add
#daum 영화정보 Collection
daum = db_ttolae.daum_movie_info
daum_cursor = daum.find()


# inte_movie_info = db_ttolae.inte_daum_movie_info


matched = []
false  = []

#daum건 수만큼 반복
for doc in daum_cursor :
    document = doc
    print(document)
    print(document["movie_id"][0]['id'])
    print(add.find({"_id" : str(document["movie_id"][0]['id'])}).count())
    #
    a = add.find({"_id": str(document["movie_id"][0]['id'])})
    if a.count() == 1:
        matched.append(doc["movie_id"])
        backId = doc['_id']
        doc.update(a.next())
        doc['_id'] = backId
        print(doc)
        daum.save(doc)
    else :
        false.append(doc["movie_id"])
    #     #Mongo DB에 save로 업데이트
    #     print("원본 : ",current_document)
    #     print("가공 : ",res)
    #     inte_movie_info.save(res)
    #
    #     #테스트용
    #     matched.append(res)
    # else:
    #     dictTemp = {'_id': '', 'movie_id': [], 'inte_title': '', 'movie_title': '', 'director': '', 'review_cnt': [],
    #                 'running_time':0,
    #                 'score': [],'nation': '', 'open_date': '', 'genre': ''}
    #     current_document['_id'] = "d" + str(current_document['_id'])
    #     dictTemp.update(current_document)
    #
    #     print("가공(매칭x)",dictTemp)
    #     inte_movie_info.save(dictTemp)
    #     false.append([(dictTemp, res)])
    #
    # # if current_document['_id'] == 431 :
    # #     break
    #

    print("matched",len(matched))
    print("false",len(false))
    print(false)
# for a in false :
#     print(a)


