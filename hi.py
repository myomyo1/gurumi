import os
import sys
from stat import *

import json

from pymongo import MongoClient

# print(sys.path)
sys.path.append("C:\\Users\\bit\\PycharmProjects\\pymongo_test")
# import bs4
# from konlpy.tag import Komoran
import module_chk
# k = Komoran()

module_chk.chk("hi")
client = MongoClient('mongodb://192.168.1.56:27017/')

db_ttolae = client.TTOLAE
collection_people = db_ttolae.people

print("hi")
print(collection_people.find().next())


# activate_this = '/path/to/env/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
# "C:\\ProgramData\\Anaconda3\\envs\\gurumi"