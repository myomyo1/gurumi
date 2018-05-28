from konlpy.tag import Komoran
ko = Komoran()
userdic = ["강추","기대","노잼","봉준호감독님"]
# userdic = []

def dicPos(string) :
    index = 0
    while index < len(userdic) :
        if userdic[index] in string:
            sn = " 홠"+ str(index)+ " "
            string = string.replace(userdic[index], sn)
        index = index+1
    result = ko.pos(string)

    i = 0
    while i < len(result) :
        if "홠" in result[i][0] :
            # print(result[i])
            index = int(result[i][0][1::])
            # print(userdic[index])
            result[i] = (userdic[index],"NNG")
        i = i + 1
    return result