import module_makeWord
def pickup(wordlist,final_list):
    for word in wordlist:
        if word[1] == 'NNG' or word[1] == 'NNP' or word[1] == 'NA' or word[1] =='NF' or word[1] == 'NV'or word[1] == 'IC':
            # final_word_list.append([word])
            final_list.append(word[0])
        elif word[1] =='VA' :
            final_list.append(module_makeWord.vaChange(word)[0])