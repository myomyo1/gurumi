from pymongo import MongoClient

client = MongoClient('mongodb://192.168.1.56:27017')
db_ttolae = client.TTOLAE
collection = db_ttolae.mapReduce_naver_movie_info
cursor = collection.find()

target_collection = db_ttolae.naver_movie_info_distinct


# {'_id': "", 'movie_id': [], 'inte_title': '', 'movie_title': '', 'poster': '', 'inte_director': ''
#     , 'director': '', 'review_cnt': [], 'score': [],
#  'person': [{'person_id': 71649, 'person_name': '마리 바우머', 'role': '주연', 'part': ' '}], 'gender_ratio': [{'site': 'naver', 'male': 0}],
#  'age': []}
#

count = collection.count()
for i in range(0 , count) :
    document = cursor.next()
    dict = {'_id': "", 'movie_id': [], 'inte_title': '', 'movie_title': '', 'poster': '', 'inte_director': '' , 'director': '',
            'review_cnt': [], 'score': [], 'person': [], 'gender_ratio': [], 'age': []}
    print(document)
    document_value = document['value']

    dict['_id'] = str(document_value['movie_id'][0]['id'])
    dict['movie_id'] = document_value['movie_id']
    dict['movie_id'][0]['id'] = str(dict['movie_id'][0]['id'])
    dict['poster'] = document_value['poster']
    dict['inte_title'] = document_value['inte_title']
    dict['movie_title'] = document_value['movie_title']
    dict['inte_director'] = document_value['inte_director']
    dict['director'] = document_value['director']
    dict['review_cnt'] = document_value['review_cnt']
    dict['review_cnt'][0]['cnt'] = int(dict['review_cnt'][0]['cnt'])
    dict['gender_ratio'] = document_value['gender_ratio']
    dict['age'] = document_value['age']
    dict['person'] = document_value['person']
    dict['score'] = document_value['score']
    dict['score'][0]['grade'] = float(dict['score'][0]['grade'])

    target_collection.save(dict)
    print(dict)
