import json
import module_chk
from konlpy.tag import Komoran
import module_pickup
from pymongo import MongoClient
import module_dicPos
client = MongoClient("mongodb://192.168.1.56:27017/")
db_ttolae = client.TTOLAE
collection_review = db_ttolae.test_review
collection_movie_info = db_ttolae.movie_info

ko = Komoran()
movieId = None
with open('C:/MONGODB/BAK/JSON_BAK/naver_review_linked_0531.json', encoding='UTF8') as data_file :
# with open('C:/MONGODB/BAK/JSON_BAK/cgv_movie_info_0502.json', "r", encoding='UTF8') as data_file :
    i = 0
    ttolaeDic = module_dicPos.TTOLAEDic()
    for a in data_file :
        data = json.loads(a)
        if movieId == None or str(data["movie_id"]) !=  movieId :
            movieId = str(data["_id"]["movie_ref"]["$id"])
            movieInfo = collection_movie_info.find_one({'_id': movieId})
            print(movieInfo)
            addList = []
            addList.append(movieInfo['inte_title'])
            addList.append(movieInfo['director'])
            try:
                addList += [element['person_name']for element in movieInfo['person']]
            except KeyError as e :
                print("person 없음",e)

            try:
                addList += [element['part'] for element in movieInfo['person'] if element['part'] !=' ' ]
            except KeyError as e:
                print("part 없음", e)

            print(addList)
            ttolaeDic.resetDic()
            ttolaeDic.addDicList(addList)
            print(ttolaeDic.userDic)

        wordlist = ttolaeDic.dicPos(data["review_contents"])
        data["user_grade"] = int(data["user_grade"])
        data["movie_id"] = str(data["movie_id"])
        # wordlist = ko.pos(data["review_contents"])
        ##단순반복 제거
        i = 3
        while i < len(wordlist):
            # print("i", i)
            if wordlist[i] == wordlist[i - 1] and wordlist[i] == wordlist[i - 2] and wordlist[i] == wordlist[i - 3]:
                del wordlist[i]
            else:
                i = i + 1

        j = 0
        final_list = []
        while j < len(wordlist):
            # print(j)
            module_chk.chk(wordlist, j, [wordlist[j]],final_list)

            j = j+1
        module_pickup.pickup(wordlist,final_list)

        pos_analyze = {"pos_analyze": wordlist}
        data.update(pos_analyze)
        gurumi_word = {"gurumi_word":final_list}
        data.update(gurumi_word)
        print(data)
        # print(final_list)
        # collection_review.save(data)

        i = i+1
        print(i)


    # print(data_file.readline())
    # print(data_file.readline())
    # print(data_file.read())
# pprint(data)

#
# from pathlib2 import Path
# contents = Path('C:/MONGODB/BAK/JSON_BAK/movie_info_0502.txt', encoding='UTF8')
# # print(contents.count("\n"))
