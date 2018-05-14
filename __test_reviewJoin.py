# from pymongo import MongoClient
#
# client = MongoClient("mongodb://192.168.1.56:27017")
# db_ttolae = client.TTOLAE
# collection = db_ttolae.review_test
# cursor = collection.find()
# data_list = []
# for d in cursor :
#     data_list.append(d)
#     print(data_list)
#     print(len(data_list))

#
# site = "cgv"
# movie_id = "55743"
#
#
# pipline = [{"$match" : { "movie_id" :  { "site" : site , "id" : movie_id } } }, {"$project": {"_id" : 1}} ]
#
# cursor = collection.aggregate(pipline)
# dict = cursor.next()
# print(dict['_id'])
#
#
#
# link = {
#     "$ref" : "movie_info",
#     "$id" : dict['_id'],
#     "$db" : "TTOLAE"
# }
#
# review_id = {
#     "movie_ref" : link ,
#     "user_id" : user_id
# }
#
# print(link)
