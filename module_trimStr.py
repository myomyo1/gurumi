import re

def trimStr(str) :
    # 소문자로 통일하기
    result = str.lower()

    # : , - _ ! . [] 띄어쓰기 지우기
    result = re.sub("[\+\,\-_!?.: ' ''\[' '\]']","",result)
    result = re.sub("[\&]","앤",result)

    # ()안에 내용 지우기
    result = re.sub("(['(']\w*[')']){1}","",result)
    return result

