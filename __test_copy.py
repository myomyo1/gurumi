# # from pymongo import MongoClient
# import pymongo
#
# client = pymongo.MongoClient("mongodb://192.168.1.56:27017")
# db_ttolae = client.TTOLAE
# #
# # find_cursor = db_ttolae.filmography.find()
# #
# # for i in range(0,20000) :
# #     db_ttolae.modify_test.save(find_cursor.next())
# jin_movie_info = db_ttolae.jin_movie_info
#
#
# testDocument = { "_id" : "19188001", "movie_title" : "개의 일생", "nation" : "미국", "open_date" : "", "genre" : "코미디", "director" : "찰리 채플린", "inte_title" : "개의일생", "inte_director" : "찰리채플린" }
# while True :
#     try :
#         jin_movie_info.insert(testDocument)
#     except pymongo.errors.DuplicateKeyError as e:
#         print("에러")
#         break

# { "_id" : "19188001", "movie_title" : "개의 일생", "nation" : "미국", "open_date" : "", "genre" : "코미디", "director" : "찰리 채플린", "inte_title" : "개의일생", "inte_director" : "찰리채플린" }
#
#
#
# client.close()
#
import module_makeWord
import module_dicPos
import re



hi = ['d','aaa','aaaaaaaaa','afasdfasd']

print(hi[0::-1])

a = module_dicPos.TTOLAEDic()


# review = [('아쉽', 'VA'), ('ㄴ', 'ETM'),('스포츠', 'NNG')]
review = [('스포츠', 'NNG'),('슬프', 'VA')]

# print(Def_making_final_final.fml("안녕하세요"))
print(module_makeWord.wordMakingFunction(review))
str = "말이 필요없다"
print("안녕" in str)

print(a.userDic)
idx = a.addDicList(["말이","필요","없다"])
print(idx)
# print(a.addDicList(["말이 필요없다"]))
print(a.userDic)
print(a.dicPos(str))
a.resetDic()
print(a.userDic)

if "안녕" in str :
    str = str.replace("안녕","@")

print(str)

a = ['a b','c d']
b = []

a += b
s1 =  "      안 녕112~~::-     "
print(re.sub( "\W","",re.sub("[0-9]","",s1)).strip())
print(re.sub("\W","",s1))
print(' 'in s1)
print("ㅁㅁㅁㅁ".split())

# print(module_dicPos.dicPos(str))
