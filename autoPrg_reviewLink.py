from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE

collection_movie_info = db_ttolae.movie_info

collection_review = db_ttolae.raw_daum_review
# collection_review = db_ttolae.test_review_update
collection_review_save =db_ttolae.daum_review
cursor_review = collection_review.find()
cnt = cursor_review.count()
print(cnt)


# 12398

for i in range(0, cnt) :
    print("\n=======================",i,"번째 값 =======================")
    document = cursor_review.next()
    print(document)

    # ref 요소 추출 (fk 역할)
    site = document['site']
    print("site",site)
    movie_id = document['movie_id']
    print("movie_id",movie_id)

    # 사이트별 movie_id를 이용해 공통 id찾기(movie_info에서 찾기)
    pipline = [{"$match": {"movie_id": {"site": site, "id": movie_id}}}, {"$project": {"_id": 1}}]
    c = collection_movie_info.aggregate(pipline)
    common_id = c.next()['_id']


    # ref 객체 만들기
    link = {
        "$ref": "movie_info",
        "$id": common_id,
        "$db": "TTOLAE"
    }
    print(link)


    # _id 에 들어갈 객체
    review_id = {
        "movie_ref": link,
        "user_id": document['user_id']
    }
    print(review_id)

    # _id에 review_id를 저장(링크를 포함하고있음)
    document['_id']=review_id
    collection_review_save.save(document)





