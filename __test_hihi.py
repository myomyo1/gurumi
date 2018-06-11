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
collection_people = db_ttolae.people

#############################################################################################


# driver = webdriver.Chrome('driver/chromedriver.exe')
n = 1207
errorPage = set()

while n < 417252  :
    try:
        page = urlopen('https://movie.naver.com/movie/bi/pi/filmo.nhn?code={0}'.format(n))
        soup = BeautifulSoup(page, 'html.parser')
        if soup.find(class_='h_movie') == None:
            n = n+1
            continue
        name = soup.find(class_='h_movie').get_text()
        poster = soup.find(class_='poster').find('img').attrs['src']

        person = {"_id" : n, "name" : name, "people_img" : poster ,"test":[{"a":1, "b" : ["1","2"]}]}
        print(person)

        with open('C:/Users/bit/Desktop/test/test.txt', 'a') as data:
            data.write(str(person))
        # collection_people.save(person)

    except HTTPError as e:
        print(e)
        #에러난 페이지 추가하기
        errorPage.add(n)
        n = n+1
        continue
    n = n + 1