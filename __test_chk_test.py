#-*- coding:utf-8 -*-
from konlpy.tag import Komoran
from pymongo import MongoClient
import module_chk
import module_pickup

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
sample_list = sum[400:450]

final_list=[]

n=0
for sample in sample_list:
    wordlist = ko.pos(sample)
    module_pickup.pickup(wordlist)
    # into_words.append(final_word_list)
    i = 0
    n = n+1
    while i < len(wordlist) :
        module_chk.chk(wordlist, i, [wordlist[i]])
        # into_words.append(final_list)
        i = i+1
        # print(i)
    print(n,"번째","list :", wordlist)
    print('FINAL_LIST',final_list)
    # print('WORD_LIST', final_word_list)
    final_list = []

    print("----------------------------------------------")
