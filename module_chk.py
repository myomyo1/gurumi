import module_makeWord

def chk(wordlist, idx, conList,final_list):
    if idx + 1 == len(wordlist) :
        print("끝지점 도달")
        print(idx+1)
        global global_index
        global_index  = idx
        return

    else :
        if wordlist[idx][1] == 'NNG' or wordlist[idx][1] == 'NNP' or wordlist[idx][1] == 'NNB':
            if idx+1 < len(wordlist) and (wordlist[idx + 1][1] == 'NNG' or wordlist[idx+1][1] == 'NNP'or wordlist[idx+1][1] == 'NNB'):
                conList.append(wordlist[idx + 1])
                final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                chk(wordlist, idx + 1, conList, final_list)

            elif idx + 1 < len(wordlist) and wordlist[idx + 1][1] == 'JKG':

                if idx + 2 < len(wordlist) and (wordlist[idx + 2][1] == 'NNG' or wordlist[idx+2][1] == 'NNP' or wordlist[idx+2][1] == 'NNB'):
                    conList.append(wordlist[idx + 1])
                    conList.append(wordlist[idx + 2])
                    final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                    chk(wordlist, idx + 2, conList, final_list)

            elif idx + 1 < len(wordlist) and wordlist[idx + 1][1] == 'VA':
                conList.append(wordlist[idx + 1])
                final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                chk(wordlist, idx + 1, conList, final_list)

        elif wordlist[idx][1] == 'VA':
            if idx+1 < len(wordlist) and (wordlist[idx + 1][1] == 'NNG' or wordlist[idx+1][1] == 'NNP' or wordlist[idx+1][1] == 'NNB'):
                conList.append(wordlist[idx+1])
                final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                chk(wordlist, idx + 1, conList, final_list)

                if idx+2 < len(wordlist) and wordlist[idx + 2][1] == 'MAG':
                    conList.append(wordlist[idx + 2])
                    final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                    chk(wordlist, idx + 2, conList, final_list)

            elif idx+2 < len(wordlist) and wordlist[idx + 1][1] == 'ETM' \
                        and (wordlist[idx + 2][1] == 'NNG'or wordlist[idx+2][1] == 'NNP'or wordlist[idx+2][1] == 'NNB'):
                    conList.append(wordlist[idx + 1])
                    conList.append(wordlist[idx + 2])
                    final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                    chk(wordlist, idx + 2, conList, final_list)

        elif wordlist[idx][1] == 'MAG':
            if idx + 1 < len(wordlist) and (wordlist[idx + 1][1] == 'VA' or wordlist[idx + 1][1] == 'XR'):
                conList.append(wordlist[idx+1])
                final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                chk(wordlist, idx + 1, conList, final_list)

        elif wordlist[idx][1] == 'XR':
            if idx + 3 < len(wordlist) and wordlist[idx + 1][1] == 'XSA' and wordlist[idx + 2][1] == 'ETM'\
                    and(wordlist[idx + 3][1] == 'NNG' or wordlist[idx + 3][1] == 'NNP' or wordlist[idx + 3][1] == 'NNB'):
                conList.append(wordlist[idx + 1])
                conList.append(wordlist[idx + 2])
                conList.append(wordlist[idx + 3])
                final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                chk(wordlist, idx + 3, conList, final_list)

        elif wordlist[idx][1] == 'SN':
            if idx+1 < len(wordlist) and (wordlist[idx + 1][1] == 'NNG' or wordlist[idx+1][1] == 'NNP'or wordlist[idx+1][1] == 'NNB'):
                conList.append(wordlist[idx + 1])
                final_list.append(module_makeWord.wordMakingFunction(conList.copy()))
                chk(wordlist, idx + 1, conList, final_list)