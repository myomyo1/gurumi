#-*- coding:utf-8 -*-
from konlpy.tag import Komoran
from pymongo import MongoClient

ko = Komoran()

client = MongoClient("mongodb://192.168.1.56:27017/")
db_ttolae = client.TTOLAE
collection_review = db_ttolae.review_test

find_movie = collection_review.find({"movie_id" : 42886})
count = find_movie.count()
test_review_list = []

for i in range(0,count) :
    current_document = find_movie.next()
    test_review_list.append(current_document)

sum = [ r['review_contents'] for r in test_review_list  ]
sample_list = sum[400:500]

# global global_index
# global_index = 0
# idx = 0
final_list=[]
def chk(wordlist, idx, conList):
    if idx + 1 == len(wordlist) :
        print("끝지점 도달")
        print(idx+1)
        global global_index
        global_index  = idx
        return

    else :
        if wordlist[idx][1] == 'NNG' :
            if wordlist[idx + 1][1] == 'NNG' or wordlist[idx + 1][1] == 'MAG' :
                conList.append(wordlist[idx + 1])
                print('NNGNNG : ',conList)
                final_list.append(conList)
                chk(wordlist, idx + 1, conList)

        elif wordlist[idx][1] == 'VA':
            if wordlist[idx + 1][1] == 'NNG' :
                conList.append(wordlist[idx+1])
                final_list.append(conList)
                print('VANNG : ', conList)
                chk(wordlist, idx + 1, conList)
                if wordlist[idx + 2][1] == 'NNG' or wordlist[idx + 2][1] == 'MAG':
                    conList.append(wordlist[idx + 2])
                    print('야이러너넌너넌: ',conList)
                    final_list.append(conList)
                    chk(wordlist, idx + 1, conList)

            elif wordlist[idx + 1][1] == 'ETM':
                conList.append(wordlist[idx + 1])
                # conList.append(wordlist[idx + 1] + wordlist[idx + 2])
                if wordlist[idx + 2][1] == 'NNG':
                    conList.append(wordlist[idx + 2])
                    print('VAETMNNG : ', conList)
                    final_list.append(conList)
                    chk(wordlist, idx + 1, conList)

        elif wordlist[idx][1] == 'MAG':
            if wordlist[idx + 1][1] == 'VA':
                conList.append(wordlist[idx+1])
                print('MAGVA : ', conList)
                final_list.append(conList)
                chk(wordlist, idx + 1, conList)


n=0
for sample in sample_list:
    wordlist = ko.pos(sample)
    i = 0
    n = n+1
    while i < len(wordlist) :
        print(chk(wordlist, i, [wordlist[i]]))
        i = i+1
        # print(i)
    print(n,"번째","list :", wordlist)
    print('짠',final_list)
    print("----------------------------------------------")