
def pickup(wordlist,final_list):
    for idx, word in enumerate(wordlist):
        if idx + 1 == len(wordlist):
            break
        if word[1] == 'NNG' or word[1] =='VA' or word[1] == 'NNP' or word[1] =='NNB' or word[1] == 'NA' or word[1] =='NF' or word[1] == 'NV':
            # final_word_list.append([word])
            final_list.append([word])