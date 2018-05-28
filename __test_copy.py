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
import module_makeWord
import module_dicPos


hi = ['d','aaa','aaaaaaaaa','afasdfasd']

print(hi[0::-1])


# review = [('아쉽', 'VA'), ('ㄴ', 'ETM'),('스포츠', 'NNG')]
review = [('스포츠', 'NNG'),('슬프', 'VA')]

# print(Def_making_final_final.fml("안녕하세요"))
print(module_makeWord.wordMakingFunction(review))
str = "크리스티나"
print("안녕" in str)

if "안녕" in str :
    str = str.replace("안녕","@")

print(str)

print(module_dicPos.dicPos(str))
