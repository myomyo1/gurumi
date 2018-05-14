import json
import  module_chk
from konlpy.tag import Komoran
import module_pickup


ko = Komoran()

with open('C:/MONGODB/BAK/JSON_BAK/review_0510.json', encoding='UTF8') as data_file :
# with open('C:/MONGODB/BAK/JSON_BAK/cgv_movie_info_0502.json', "r", encoding='UTF8') as data_file :
    i = 0
    for a in data_file :
        data = json.loads(a)
        wordlist = ko.pos(data["review_contents"])
        pos_analyze = {"pos_analyze": wordlist}
        data.update(pos_analyze)
        print(data)
        j = 0
        final_list = []
        while j < len(wordlist):
            # print(j)
            module_chk.chk(wordlist, j, [wordlist[j]],final_list)

            j = j+1
        print(final_list)
        module_pickup.pickup(wordlist,final_list)
        print(final_list)
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
