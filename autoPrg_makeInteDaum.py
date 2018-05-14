import module_DaumMovieComparator
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE

#진흥원 영화정보 Collection
jin = db_ttolae.jin_movie_info
#daum 영화정보 Collection
daum = db_ttolae.daum_movie_info_distinct
daum_cursor = daum.find()

inte_movie_info = db_ttolae.inte_daum_movie_info


matched = []
false  = []

#daum건 수만큼 반복
for i in range(0,daum_cursor.count()) :
    current_document = daum_cursor.next()
    res = module_DaumMovieComparator.compare(jin, current_document, "inte_title", "inte_director")

    if type(res) == dict :
        #Mongo DB에 save로 업데이트
        print("원본 : ",current_document)
        print("가공 : ",res)
        inte_movie_info.save(res)
        
        #테스트용
        matched.append(res)
    else:
        dictTemp = {'_id': '', 'movie_id': [], 'inte_title': '', 'movie_title': '', 'director': '', 'review_cnt': [],
                    'running_time':0,
                    'score': [], 'genre': '', 'open_date': '', 'watching_rate': '', 'nation': ''}
        current_document['_id'] = "d" + str(current_document['_id'])
        dictTemp.update(current_document)

        print("가공(매칭x)",dictTemp)
        inte_movie_info.save(dictTemp)
        false.append([(dictTemp, res)])

    # if current_document['_id'] == 431 :
    #     break


    print(len(matched))
    print(len(false))
# for a in false :
#     print(a)


