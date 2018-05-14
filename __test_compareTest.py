# 1) db.modify_insert_test_copy - db.modify_insert_test를 비교 검증

from pymongo import MongoClient
import module_MovieComparator
client = MongoClient('mongodb://192.168.1.56:27017/')

db_ttolae = client.TTOLAE

collection_jin_movie_info = db_ttolae.jin_movie_info
collection_jin_movie_info_cursor = collection_jin_movie_info.find()



collection_test = db_ttolae.modify_insert_test
collection_test_copy = db_ttolae.modify_insert_test_copy

test_cursor = collection_test.find()
test_copy_cursor = collection_test_copy.find()

# compare( collection , compareDict, fieldName,fieldName1) :

# print(current_document)
# print(module_MovieComparator.compare(collection_test,current_document ,"movie_title", "director") )
matched = []
false  = []
for i in range(0,collection_test.count()):
    current_document = test_cursor.next()
    # print(current_document)
    res = module_MovieComparator.compare(collection_jin_movie_info,current_document ,"movie_title", "director")
    if type(res) == dict :

        matched.append(res)
    else :
        false.append([(current_document, res)])
    print(len(matched))
    print(len(false))


# print(matched)
print(len(matched))

print(false)
print(len(false))