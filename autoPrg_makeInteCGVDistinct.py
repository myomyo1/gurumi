import module_CGVDistinctMovieComparator
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE

#진흥원 영화정보 Collection
jin = db_ttolae.jin_movie_info
#cgv 영화정보 Collection
cgv = db_ttolae.cgv_movie_info_distinct
cgv_cursor = cgv.find()

inte_cgv_movie_info = db_ttolae.inte_cgv_movie_info_distinct


matched = []
false  = []
# needChk = []
count = cgv_cursor.count()
#cgv건 수만큼 반복
for i in range(0,count) :
    current_document = cgv_cursor.next()
    res = module_CGVDistinctMovieComparator.compare(jin, current_document, "inte_title", "director")

    if type(res) == dict :
        #Mongo DB에 save로 업데이트
        print("원본 : ",current_document)

        dictTemp = {'_id': '', 'movie_id': [], 'inte_title': '', 'movie_title': '', 'director': '', 'review_cnt': [],
                    'gender_ratio': [{'site': 'cgv', 'male': 0.0}],
                    'age': [{'site': 'cgv', 'teen': 0.0, 'twenty': 0.0, 'thirty': 0.0, 'forty': 0.0}], 'score': [], 'nation': '', 'open_date': '', 'genre': ''}
        dictTemp.update(res)

##잘못된 크롤링에 대한 후속조치
        if  type(res['age']) == dict:
            dictTemp['age'].update([{'site': 'cgv', 'teen': 0.0, 'twenty': 0.0, 'thirty': 0.0, 'forty': 0.0}])
            dictTemp['age'][0]['teen'] = res['age']['teen']
            dictTemp['age'][0]['twenty'] = res['age']['twenty']
            dictTemp['age'][0]['thirty'] = res['age']['thirty']
            dictTemp['age'][0]['forty'] = res['age']['forty']

##
        print("가공 : ", dictTemp)
        #테스트용
        # if res['_id'] in matched :
        #     inserted = inte_movie_info.find({"_id":res['_id']}).next()
        #     inserted['movie_id'].append(res['movie_id'])
        #     inserted['review_cnt'].append(res['review_cnt'])
        #     inserted['gender_ratio'].append(res['gender_ratio'])
        #     inserted['age'].append(res['age'])
        #     inserted['score'].append(res['score'])
        #     print("@@@@@가공 : ", inserted)
        #
        #     needChk.append(res)

        inte_cgv_movie_info.save(dictTemp)
        matched.append(res['_id'])

    else:
        dictTemp = {'_id': '', 'movie_id': [], 'inte_title': '', 'movie_title': '', 'inte_director': '', 'director': '', 'review_cnt': [],
                    'gender_ratio': [{'site': 'cgv', 'male': 0.0}],
                    'age': [{'site': 'cgv', 'teen': 0.0, 'twenty': 0.0, 'thirty': 0.0, 'forty': 0.0}], 'score': [], 'nation': '', 'open_date': '', 'genre': ''}
        current_document['_id'] = "c" + str(current_document['_id'])
        dictTemp.update(current_document)

        ##잘못된 크롤링에 대한 후속조치
        if type(current_document['age']) == dict:
            dictTemp['age']=[{'site': 'cgv', 'teen': 0.0, 'twenty': 0.0, 'thirty': 0.0, 'forty': 0.0}]
            dictTemp['age'][0]['teen'] = current_document['age']['teen']
            dictTemp['age'][0]['twenty'] = current_document['age']['twenty']
            dictTemp['age'][0]['thirty'] = current_document['age']['thirty']
            dictTemp['age'][0]['forty'] = current_document['age']['forty']

        ##

        print("가공(매칭x)",dictTemp)
        inte_cgv_movie_info.save(dictTemp)
        false.append([(dictTemp, res)])



    print(len(matched))
    print(len(false))
    # print(needChk)

    # print(len(needChk))
# for a in false :
#     print(a)
print(count)