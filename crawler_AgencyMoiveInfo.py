# 63898

import json, urllib.request
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.1.56:27017/')
db_ttolae = client.TTOLAE
jin_movie_info = db_ttolae.jin_movie_info
pageNum =5363
count = (pageNum - 1) * 10
while True :
    key = "1f8dd071c754fe2fa0f307024086cc7e"
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key="+key+"&curPage=" + str(pageNum)
    data = urllib.request.urlopen(url).read()

    dictList = json.loads(data)['movieListResult']['movieList']
    print(dictList)
    print(len(dictList))
    print("페이지 : ",pageNum)


    if len(dictList) == 0:
        break

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
         "directors" : dict["directors"][0]["peopleNm"]
         }
        jin_movie_info.save(insert_movie)
        count = count + 1
        print("## "+str(count)+"번째 영화 입력 : "+str(insert_movie))

    pageNum = pageNum+1



#
# {
# 'movieCd': '20183084',
# 'movieNm': '피터 래빗',
# 'movieNmEn': 'Peter Rabbit',
# 'prdtYear': '2018',
# 'openDt': '20180517',
# 'typeNm': '장편',
# 'prdtStatNm': '개봉예정',
# 'nationAlt': '미국,영국,호주',
# 'genreAlt': '애니메이션,가족',
# 'repNationNm': '미국',
# 'repGenreNm': '애니메이션',
# 'directors': [{'peopleNm': '윌 글럭'}],
# 'companys': []},

