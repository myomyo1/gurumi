def fml(split_word_list) :

    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                     'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    result = []
    for j in range(0, len(split_word_list)):
        # 한글 여부 check 후 분리
        char_code = ord(split_word_list[j]) - BASE_CODE  # 한 단어에 대한 ord(아스킷코드로변환) 후 초성중성나누기 위해 베이스코드 빼줌

        char1 = int(char_code / CHOSUNG)
        result.append(CHOSUNG_LIST[char1])

        char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
        result.append(JUNGSUNG_LIST[char2])

        char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
        result.append(JONGSUNG_LIST[char3])

    return result

####################################################################################################################################################################################


def makeChar(chosung, jungsung, jongsung) :

    # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                     'ㅣ']
    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    cho = CHOSUNG_LIST.index(chosung)
    jung = JUNGSUNG_LIST.index(jungsung)
    jong = JONGSUNG_LIST.index(jongsung)
    result = jong + (JUNGSUNG * jung) + (CHOSUNG * cho) + BASE_CODE

    return chr(result)

def wordMakingFunction(wordList) :
    finalWord = ""
    i = 0
    while i < len(wordList) :
        if wordList[i][1] == 'ETM' and wordList[i][0] == 'ㄴ' :
            splitWord = fml(wordList[i-1][0])
            if splitWord[-1::][0] == ' ' :
                splitWord[len(splitWord)-1] = 'ㄴ'
                del wordList[i]
            elif splitWord[-1::][0] == 'ㅂ' :
                splitWord[len(splitWord) - 1] = ' '
                wordList[i] = ("운", "GURUMI")
            temp = ""
            j = 0
            while j < len(splitWord)/3 :
                temp += makeChar(splitWord[j*3],splitWord[j*3+1],splitWord[j*3+2] )
                j = j+1
            gurumiWord = (temp, "GURUMI")
            wordList[i-1] = gurumiWord
        if i == len(wordList) - 1 and wordList[i][1] == 'VA' :
            wordList[i] = vaChange(wordList[i]);

        i = i+1


    for word in wordList :
        finalWord += word[0]
    return finalWord

def vaChange(tupleVa) :
    va = list(tupleVa)
    splitWord = fml(va[0])

    # 1 : 음
    # 0 : 움
    # -1 : x
    chk = 1;

    if splitWord[-1::][0] == ' ' :
        splitWord[len(splitWord) - 1] = 'ㅁ'
        chk = -1
    elif splitWord[-1::][0] == 'ㅂ' :
        splitWord[len(splitWord) - 1] = ' '
        chk = 0

    temp = ""
    j = 0
    while j < len(splitWord) / 3:
        temp += makeChar(splitWord[j * 3], splitWord[j * 3 + 1], splitWord[j * 3 + 2])
        j = j + 1
    if chk == 1:
        temp += "음"
    elif chk == 0:
        temp += "움"
    va[0] = temp

    return (va[0],va[1])
