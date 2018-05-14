from pymongo import MongoClient

client = MongoClient('mongodb://192.168.1.56:27017')
db_ttolae = client.TTOLAE
collection = db_ttolae.mapReduce_daum_movie_info
cursor = collection.find()

target_collection = db_ttolae.daum_movie_info_distinct

count = collection.count()
for i in range(0 , count) :
    document = cursor.next()
    dict = {'_id': "",'movie_id': [] , 'inte_title': '','movie_title': '',
            'inte_director': '','director': '', 'review_cnt': [], 'running_time':0 ,'score': [],
            'genre': '', 'open_date': '', 'watching_rate': '', 'nation': ''
            }


    document_value = document['value']

    dict['_id'] = str(document_value['movie_id'][0]['id'])
    dict['movie_id'] = document_value['movie_id']
    dict['movie_id'][0]['id'] = str(dict['movie_id'][0]['id'])
    dict['inte_title'] = document_value['inte_title']
    dict['movie_title'] = document_value['movie_title']
    dict['inte_director'] = document_value['inte_director']
    dict['director'] = document_value['director']
    dict['review_cnt'] = document_value['review_cnt']
    dict['review_cnt'][0]['cnt'] = int(dict['review_cnt'][0]['cnt'])
    dict['score'] = document_value['score']
    dict['score'][0]['grade'] = float(dict['score'][0]['grade'])
    dict['running_time'] = document_value['running_time']

    dict['genre'] = document_value['genre']
    dict['open_date'] = document_value['open_date']
    dict['watching_rate'] = document_value['watching_rate']
    dict['nation'] = document_value['nation']

    target_collection.save(dict)
    print(dict)
