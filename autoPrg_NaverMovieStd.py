# 네이버 영화 크롤링한 문서를 표준화하기위한 프로그램
# poster를 고유로 비교하여 인물을 임베디드 타입으로 변경
# 인물 번호를 인물 collection과 Linking
# _id값을 네이버 moive_id값으로 지정 ( 네이버를 기준으로 다음, 왓챠를 크롤링할 예정)

from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')

db_ttolae = client.TTOLAE

find_cursor = db_ttolae.modify_test.find()
std = None
save_document = {}
for n in  range(0,20000) :

    compare = find_cursor.next()

    if std == None or std['movie_id'][0]['id'] != compare['movie_id'][0]['id'] :

        print("새로 딕셔너리 만듦")
        std = compare
        save_document.update({"_id": std['movie_id'][0]['id']})
        save_document.update({'movie_id': std['movie_id']})
        save_document.update({'movie_title': std['movie_title']})
        save_document.update({'poster': std['poster']})
        save_document.update({'director': std['director']})
        save_document.update({'review_cnt':
                                  [{'site': 'naver', 'cnt': std['review_cnt']}]
                              })
        save_document.update({'score': std['score']})
        save_document.update({'person': []})
        print("최초 생성 딕셔너리 : ",save_document)
    else :
        std = compare


    concat_people = {}
    for i in range(0,4) :
        # print(std['person'][i])
        # print(std['person'][i].values() )
        #

        if std['person'][i] == None or ' ' in std['person'][i].values()  :
            continue
        concat_people.update(std['person'][i])
    # print("추가 예정 인물 딕셔너리 : ", concat_people)
    # print("추가 전 인물 리스트: " ,  save_document['person'])


    ######################    MonogDB 입력부     #############################################
    save_document['person'].append(concat_people)
    db_ttolae.modify_insert_test.save(save_document)

    print("인물 추가 완료 후 딕셔너리 : ", save_document)
client.close()