# from pymongo import MongoClient
#
# client = MongoClient("mongodb://192.168.1.56:27017")
# db_ttolae = client.TTOLAE
#
# find_cursor = db_ttolae.filmography.find()
#
# for i in range(0,20000) :
#     db_ttolae.modify_test.save(find_cursor.next())
#
#
#
#
#
# client.close()
#
c ={}
a = {'_id': '108', 'movie_id': [{'site': 'cgv', 'id': '108'}], 'inte_title': '범죄의재구성', 'movie_title': '범죄의 재구성(야호)', 'review_cnt': [{'site': 'cgv', 'cnt': 36}],  'age': [{'site': 'cgv', 'teen': 1.0, 'twenty': 25.2, 'thirty': 44.2, 'forty': 5.7}], 'score': [{'site': 'cgv', 'grade': 8.0}], 'nation': '한국', 'open_date': '20040415', 'genre': '스릴러'}
b = {'_id': '1011', 'movie_id': [{'site': 'cgv', 'id': '1011'}], 'inte_title': '범죄의재구성', 'movie_title': '범죄의 재구성(테스트1)', 'director': '최동훈', 'gender_ratio': [{'site': 'cgv', 'male': 38.2}], 'age': [{'site': 'cgv', 'teen': 0.0, 'twenty': 45.2, 'thirty': 45.2, 'forty': 9.7}], 'score': [{'site': 'cgv', 'grade': 0.0},{'site' : 'daum'}], 'nation': '한국', 'open_date': '20040415', 'genre': '스릴러'}

a.update(b)



a = [1,2,3,4,5,6,7,8,9,10]
b = [5,6,7,8]

del a[b]
a.remove(b)

print(a)

## 키가 동일하면 업데이트
print(a)