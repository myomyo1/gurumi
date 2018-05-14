from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from selenium import webdriver
from urllib.request import HTTPError
import time
import datetime
#############################################################################################
# Mongo DB 연동
from pymongo import MongoClient

client = MongoClient('mongodb://192.168.1.56:27017/')


db_ttolae = client.TTOLAE
print(client.database_names())
print(db_ttolae.collection_names(include_system_collections=False))

#############################################################################################

driver = webdriver.Chrome('C:/Users/bit/PycharmProjects/pymongo_test/driver/chromedriver.exe')

# ##########################################################################################
# startIndex =110000
# lastIndex = 0
# count = 0
# while True :
# #for n in range(1,11):
#     if count == 5 :
#         break
#     try:
#         page = urlopen('http://movie.daum.net/moviedb/main?movieId={0}'.format(startIndex))
#         soup = BeautifulSoup(page, 'html.parser')
#         lastIndex = startIndex
#         startIndex = startIndex + 500
#         count = 0
#
#     except HTTPError as e:
#         count = count +1
#         continue
# ##########################################################################################
# print(lastIndex)

n = 658
errorPage = set()

while True :
    try:
        time.sleep(0.25)
        page = urlopen('http://movie.daum.net/moviedb/main?movieId={0}'.format(n))
        soup = BeautifulSoup(page, 'html.parser')

        movie_things = soup.find(class_='movie_detail')

    except HTTPError as e:
        print(e)
        #에러난 페이지 추가하기
        errorPage.add(n)
        n = n+1
        continue

    movie_id = n
    movie_title = re.sub("\(\d{4}\)","", movie_things.find(class_='tit_movie').get_text())
    direc = movie_things.find('dd', class_="type_ellipsis").find('a').get_text()

    print('================',n,'번째==========')
    print('제목:',movie_title, 'Movie_Id:',movie_id, 'director:', direc)


    # 네티즌 평점 및 사용자 리뷰
    pg = 1
    #people =0
    m_review_name = []
    m_review_content = []

    while True:
        driver.get('http://movie.daum.net/moviedb/grade?movieId={0}&type=netizen&page={1}'.format(n, pg))
        time.sleep(0.25)
        review_page = driver.page_source
        soup2 = BeautifulSoup(review_page, 'html.parser')

        m_things = soup2.find(class_= 'movie_detail')

        m_rating = [ movie_rate.get_text() for movie_rate in m_things.find_all('span', class_='num_grade')[:3] ]
        movie_ratings = ''.join(m_rating)
        people = int(re.sub('\D','',m_things.find('span', class_='txt_menu').get_text()))
        #reviews ={}
        if m_things.find('p', class_='txt_nonerating'):
            #print('ㄴ리뷰')
            break
        else:
            #print('리뷰잇당')
            m_review_name.extend([ name.get_text() for name in m_things.find_all('em', class_='link_profile') ])
            m_review_content.extend([content.get_text().replace('\n','').replace('\t','').strip() for content in m_things.find_all('p', class_='desc_review')])
            review_names = tuple(m_review_name)
            review_content = tuple(m_review_content)

            reviews = dict(zip(review_names,review_content))
            #people = len(review_names)
            pg += 1

    daum_movie = {'movie_id' : [{'site':'daum','id':movie_id}],
                    'movie_title' : movie_title,
                    'director': direc,
                    'attendance' : people,
                    'score':[{'site':'daum','grade': movie_ratings}]
                      }

    #############################################################################################
    print("-------------", daum_movie)

    collection_movie = db_ttolae.movie

    # db_ttolae['movie'].insert(dict(daum_movie))
    now = datetime.datetime.now()
    print(now)


    #############################################################################################


    # print('평점 :', movie_ratings)
    # print('리뷰', reviews)
    # print('평점준 사람 :', people)
    n = n+1

    print('오류 페이지 개수 : ', len(errorPage))
    if len(errorPage) == 300:
        break