# 63898

import json, urllib.request
import module_trimStr
import pymongo
client = pymongo.MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE
jin_movie_info = db_ttolae.jin_movie_info
pageNum =1
count = (pageNum - 1) * 10
chk = 0
total_chk = 0
while True :

    key = "1f8dd071c754fe2fa0f307024086cc7e"
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key="+key+"&curPage=" + str(pageNum)
    data = urllib.request.urlopen(url).read()

    dictList = json.loads(data)['movieListResult']['movieList']
    print(dictList)
    print(len(dictList))
    print("페이지 : ",pageNum)

    if chk == 10:
        total_chk = total_chk +1

    if len(dictList) == 0 or total_chk == 3:
        break
    chk = 0
    for i in dictList :
        dict= i

        if "movieNm" not in dict.keys():
            dict["movieNm"] = ''
        if "nationAlt" not in dict.keys():
            dict["nationAlt"] = ''
        if "openDt" not in dict.keys():
            dict["openDt"] = ''
        if "genreAlt" not in dict.keys():
            dict["genreAlt"] = ''
        if len(dict["directors"]) == 0 :
            dict["directors"] = [{"peopleNm" : ''}]

        insert_movie = {"_id" : dict["movieCd"],
         "movie_title" : dict["movieNm"],
         "nation" : dict["nationAlt"],
         "open_date" : dict["openDt"],
         "genre" : dict["genreAlt"],
         "director" : dict["directors"][0]["peopleNm"]
         }
        result = module_trimStr.trimStr(insert_movie['movie_title'])
        insert_movie.update({"inte_title" :result})

        d_result = module_trimStr.trimStr(insert_movie['director'])
        insert_movie.update({"inte_director" :d_result})

        print("## " + str(count) + "번째 영화 입력 : " + str(insert_movie))
        try:
            jin_movie_info.insert(insert_movie)
        except pymongo.errors.DuplicateKeyError as e:

            doc = jin_movie_info.find_one({"_id" : insert_movie["_id"]})
            if doc["movie_title"] != insert_movie["movie_title"] or doc["nation"] != insert_movie["nation"] or doc["open_date"] != insert_movie["open_date"] or doc["genre"] != insert_movie["genre"] or doc["director"] != insert_movie["director"] :
                jin_movie_info.save(insert_movie)
            else :
                chk = chk+1

        count = count + 1


    pageNum = pageNum+1


