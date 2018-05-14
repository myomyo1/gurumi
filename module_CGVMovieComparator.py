# std.py
## std_dic
#{'movie_id': [{'site': 'daum', 'id': 698}], 'movie_title': '금강선법 ', 'director': '남기남', 'attendance': 4, 'score': [{'site': 'daum', 'grade': '3.3'}]}

# 1번째 파라미터 : pymongo에서 기준 collection
# 2번째 파라미터 : MongoDB에 insert될 Document(Dict)
# return 코드

# ------------ 변경전 코드 코드 -----------------
# 0 : 반영 (append) : 영화명으로 일치하는 영화 1건
# 1 : 반영 (append) : 영화명으로 일치하는건 1건 이상, 감독 조건 추가하여 검색으로 일치하는건 1건
# 2 : 반영안됨 (collection에 없는 영화)
# 3 : 반영안됨 (compareDict 에 fieldName 없음)
# 4 : 반영안됨 : 영화명으로 일치하는건 1건 이상, 감독 조건 추가하여 검색으로 일치하는건 0건
# 5 : 반영안됨 : 영화명으로 일치하는건 1건 이상, 감독 조건 추가하여 검색으로 일치하는건 1건 이상


# ------------ 결과 코드(수정 후 4/27) -----------------
# 0 : 반영 (append) : 영화명, 감독명으로 일치하는 영화 1건
# (X) 1 : 반영 (append) : 영화명으로 일치하는건 1건 이상, 감독 조건 추가하여 검색으로 일치하는건 1건
# 2 : 반영안됨 (collection에 없는 영화)
# 3 : 반영안됨 (compareDict 에 fieldName 없음)
# (X) 4 : 반영안됨 : 영화명으로 일치하는건 1건 이상, 감독 조건 추가하여 검색으로 일치하는건 0건
# (X) 5 : 반영안됨 : 영화명으로 일치하는건 1건 이상, 감독 조건 추가하여 검색으로 일치하는건 1건 이상

def compare( collection , compareDict, fieldName,fieldName1) :

    # # 파라미터 반영 확인
    print("collection:",collection)
    print("compareDict:",compareDict)
    print("fieldName:",fieldName)
    print("compareDict[fieldName]:",compareDict[fieldName])

    # 3 : 반영안됨 (compareDict 에 fieldName 없음)
    if fieldName not in compareDict:
        print("code : 3")
        return 3
    find = collection.find({fieldName: compareDict[fieldName], fieldName1: compareDict[fieldName1]})
    findCnt = find.count()

    # 2 : 반영안됨 (collection에 없는 영화)
    if findCnt == 0 :
        print("code : 2, '"+compareDict[fieldName]+"'")
        return 2

    elif findCnt == 1 :
        stdDict = find.next()
        # # 업데이트 대상 필드 확인
        # insertMovieId = stdDict["movie_id"]+compareDict["movie_id"]
        # insertScore = stdDict["score"]+compareDict["score"]
        # # insertReviewCnt = stdDict["review_cnt"]+compareDict["review_cnt"]
        #
        # print(insertMovieId,insertScore)


        # 업데이트 구문 작성 필요
        # collection.update({}{$set : {}})
        # print("-------------",concat(stdDict,compareDict))
        print("code : 0")
        return concat(stdDict,compareDict)









    reFind = collection.find({fieldName: compareDict[fieldName], fieldName1: compareDict[fieldName1]})
    reFindCnt = reFind.count()

    if reFindCnt == 0:
        print("code : 4")
        return 4
    elif reFindCnt > 1 :
        print("code : 5")
        return 5
    else :
        stdDict = reFind.next()


        # 업데이트 구문 작성 필요
        # collection.update({}{$set : {}})
        # print("-------------", concat(stdDict, compareDict))
        print("code : 1")
        return concat(stdDict,compareDict)

def concat(stdDict,compareDict) :
    # 성비의 사이트 개별로 수정 필요#################################
    dictTemp =  {'_id': '', 'movie_id': [], 'inte_title': '','movie_title': '', 'director': '', 'review_cnt': [], 'gender_ratio': [{'site' : 'cgv', 'male': 0.0 }], 'age': [{'site' : 'cgv', 'teen': 0.0, 'twenty': 0.0, 'thirty': 0.0, 'forty': 0.0}], 'score': []}


    if "movie_id" not in compareDict.keys() :
        compareDict["movie_id"] = []

    if "score" not in compareDict.keys() :
        compareDict["score"] = []

    if "review_cnt" not in compareDict.keys() :
        compareDict["review_cnt"] = []

    if "movie_id" not in stdDict.keys() :
        stdDict["movie_id"] = []

    if "score" not in stdDict.keys() :
        stdDict["score"] = []

    if "review_cnt" not in stdDict.keys() :
        stdDict["review_cnt"] = []



    # print("--------------------------------------------------------")
    # print("stdDict['movie_id'] :", stdDict["movie_id"])
    # print("compareDict['movie_id'] :", compareDict["movie_id"])
    #
    # print("--------------------------------------------------------")
    #
    # print("stdDict['score'] :", stdDict["score"])
    # print("compareDict['score'] :", compareDict["score"])
    #
    # print("--------------------------------------------------------")
    #
    # print("stdDict['review_cnt'] :", stdDict["review_cnt"])
    # print("compareDict['review_cnt'] :", compareDict["review_cnt"])
    # # print("stdDict['attendance'] :", stdDict["attendance"])
    # # print("compareDict['attendance'] :", compareDict["attendance"])
    # print("--------------------------------------------------------")

    insertMovieId = stdDict["movie_id"] + compareDict["movie_id"]
    insertScore = stdDict["score"] + compareDict["score"]
    insertReviewCnt = stdDict["review_cnt"]+compareDict["review_cnt"]
    stdDict["movie_id"] =  insertMovieId
    stdDict["score"] = insertScore
    stdDict["review_cnt"] =  insertReviewCnt
    stdDict["_id"] = compareDict["_id"]
    dictTemp.update(stdDict)

    dictTemp['gender_ratio'][0]['male'] = compareDict["male"]
    dictTemp['age'][0]['teen'] = compareDict['age']['teen']
    dictTemp['age'][0]['twenty'] = compareDict['age']['twenty']
    dictTemp['age'][0]['thirty'] = compareDict['age']['thirty']
    dictTemp['age'][0]['forty'] = compareDict['age']['forty']
    return dictTemp


#
# from pymongo import MongoClient
# client = MongoClient('mongodb://192.168.1.56:27017/')
#
# db_ttolae = client.TTOLAE
#
# collection_movie = db_ttolae.movie
#
# obj_movie = collection_movie.find()
# i = 0
# while i < obj_movie.count():
#     print(obj_movie.count())
#     print(obj_movie.next())
#     i = i+1
