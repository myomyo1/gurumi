import module_concatDocument
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE

collection_std = db_ttolae.movie_info
collection_target = db_ttolae.inte_cgv_movie_info_distinct
# collection_target = db_ttolae.inte_daum_movie_info
# collection_target = db_ttolae.inte_naver_movie_info

stdCursor = collection_std.find({"_id" : {'$regex' : '^\d'}},{"_id" : 1})
targetCursor = collection_target.find({"_id" : {'$regex' : '^\d'}},{"_id" : 1})


concat_list = []
insert_list = []
# std_id_list = collection_std.distinct("_id")
std_id_list = list(stdCursor)
std_id_list = [ x['_id'] for x in std_id_list ]


# target_id_list = collection_target.distinct("_id")
target_id_list = list(targetCursor)
target_id_list = [ x['_id'] for x in target_id_list ]

print(target_id_list)

## 디비에서 차집합을 구할수 있다면 성능개선이 가능할 것으로 보임

for t in target_id_list :
   if t in  std_id_list :
       concat_list.append(t)
       ## 속도를 위해서 비교 리스트에서 제거
       std_id_list.remove(t)
   else :
       insert_list.append(t)

   print("concat_list : ",concat_list)
   print("insert_list : ",insert_list)

for id in concat_list :
    # 테스트
    # pass
    collection_std.save(module_concatDocument.concat_doc(collection_std.find({"_id" : id }).next(),collection_target.find({"_id" : id }).next()))
    print(module_concatDocument.concat_doc(collection_std.find({"_id" : id }).next(),collection_target.find({"_id" : id }).next()))

for id in insert_list :
    collection_std.save(collection_target.find({"_id" : id }).next())

    # 테스트
    print(collection_target.find({"_id" : id }).next())
    # pass

print(len(concat_list))
print(len(insert_list))
