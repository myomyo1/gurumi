#module_concatDocument

def concat_doc(stdDoc, targetDoc) :
    resDoc = stdDoc.copy()
    targetKeyList = targetDoc.keys()
    
    for ty in targetKeyList :
        if ty in resDoc.keys() :
            if type(resDoc[ty]) == list :
                resDoc[ty]+=targetDoc[ty]
        else :
            resDoc.update({ty:targetDoc[ty]})
    return resDoc


# test1 = {'_id': '1011', 'movie_id': [{'site': 'cgv', 'id': '1011'}], 'inte_title': '범죄의재구성', '기준한테만있음' : "헿", '얘는 리스트': ['ㅁㅁㅁ']}
# test2 = {'_id': '1011', 'movie_id': [{'site': 'cgv', 'id': '1012'}], 'inte_title': '범죄의재구성', 'target' : 'aaaa','추가될 리스트' : []}
# test3 = concat_doc(test1, test2)
#
# print(test3)

