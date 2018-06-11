from konlpy.tag import Komoran
ko = Komoran()
import re

class TTOLAEDic:
    userDic = []
    originDic = []
    def __init__(self):
        # self.* : 인스턴스변수
        self.originDic = ["강추","기대","노잼","지루해","대박","존잼","꿀잼","개별로","개꿀잼","말이필요","청불", "명작","졸작","망작"]
        self.userDic = self.originDic.copy()

    def dicPos(self,string) :
        index = 0
        while index < len(self.userDic) :
            if self.userDic[index] in string:
                sn = " 홠"+ str(index)+ " "
                string = string.replace(self.userDic[index], sn)
            index = index+1
        result = ko.pos(string)
        print(result)
        i = 0
        while i < len(result) :
            if "홠" in result[i][0] :
                # print(result[i])
                index = int(result[i][0][1::])
                # print(userDic[index])
                result[i] = (self.userDic[index],"NNG")
            i = i + 1
        return result

    def addDicList(self, addList):
        for el in addList :
            el = el.replace(" 역","")
            # el = re.sub("\W", "", re.sub("[0-9]", "", el)).strip()
            self.userDic.append(el.replace(" ",""))
            if ' ' in el :
                self.userDic += el.split()

    def resetDic(self):
        self.userDic = self.originDic.copy()