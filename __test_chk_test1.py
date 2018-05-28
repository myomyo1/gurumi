from konlpy.tag import Komoran
import module_chk
k = Komoran()

str = '''굿굿굿굿굿굿굿굿굿굿굿굿굿굿굿굿굿굿굿굿굿'''
# wordlist = [('여기', 'NP'), ('영화1', 'NNG'), ('분위기1', 'NNG'),('영화2', 'NNG'), ('분위기2', 'NNG'),('영화3', 'NNG'), ('분위기3', 'NNG'),('영화4', 'NNG'), ('분위기4', 'NNG'), (',', 'SP'), ('전개', 'NNG'), ('흐름', 'NNG'), (',', 'SP'), ('성질', 'NNG'), ('하', 'XSV'), ('구', 'EC'), ('일맥상통', 'NNG'), ('하', 'XSV'), ('구', 'EC'), ('연상', 'NNG'), ('시키', 'XSV'), ('구', 'EC'), ('들어맞', 'VV'), ('는', 'ETM'), ('음악', 'NNG'), ('이', 'JKS'), ('클래식', 'NNG'), ('곡', 'NNG'), ('에', 'JKB'), ('도', 'JX'), ('있', 'VV'), ('음', 'ETN'), ('.', 'SF'), ('"', 'SS'), ('베를리오즈', 'NNP'), ('의', 'JKG'), ('환상교향곡', 'NNP'), ('!', 'SF'), ('!', 'SF'), ('!', 'SF'), ('"', 'SS')]
# wordlist = [('여기', 'NP'), ('1', 'NNG'), ('2', 'NNG'),('3', 'NNG'), ('4', 'NNG'),('5', 'NNG'), ('6', 'NNG'),('7', 'NNG'), ('8', 'NNG'), (',', 'SP'), ('전개', 'NNG'), ('흐름', 'NNG'), (',', 'SP'), ('성질', 'NNG'), ('하', 'XSV'), ('구', 'EC'), ('일맥상통', 'NNG'), ('하', 'XSV'), ('구', 'EC'), ('연상', 'NNG'), ('시키', 'XSV'), ('구', 'EC'), ('들어맞', 'VV'), ('는', 'ETM'), ('음악', 'NNG'), ('이', 'JKS'), ('클래식', 'NNG'), ('곡', 'NNG'), ('에', 'JKB'), ('도', 'JX'), ('있', 'VV'), ('음', 'ETN'), ('.', 'SF'), ('"', 'SS'), ('베를리오즈', 'NNP'), ('의', 'JKG'), ('환상교향곡', 'NNP'), ('!', 'SF'), ('!', 'SF'), ('!', 'SF'), ('"', 'SS')]
wordlist = k.pos(str)
print(wordlist)


##단순반복 제거
i = 3
while i < len(wordlist) :
    print( "i", i)
    if wordlist[i] == wordlist[i-1] and wordlist[i] == wordlist[i-2] and wordlist[i] == wordlist[i-3] :
        del wordlist[i]
    else:
        i = i + 1


print(wordlist)
final_list = []
i = 0
while i < len(wordlist) :
    module_chk.chk(wordlist, i, [wordlist[i]],final_list)
    # into_words.append(final_list)
    i = i+1
print(len(final_list))
print(final_list)
    # print(i)

# lista = [['a']]
# listb = ['b']
# listc = []
# lista.append(listb)
#
# print(lista)