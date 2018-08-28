# -*- coding: UTF-8 -*-
"""
Question Description:
input: different person's info with names、classes and scores
output: print person's info and classes info based on the name given by user
"""
def get():
    '''
    :return: person info dict
    '''
    nameScore = {}
    name = raw_input("please input name: ")
    while(name != "exit"):
        nameScore[name] = {}
        subject = raw_input("please input subject: ")
        while(subject != "exit"):
            score = raw_input("please input score: ")
            score = int(score)
            nameScore[name][subject] = score
            subject = raw_input("please input subject: ")
        name = raw_input("please input name: ")
    return nameScore

def search(nameScore, name = "zhou"):
    '''
    :param nameScore: dict stored person's info and key is name and value is a dict with class and score
    :param name: the name to search
    :return: 
    '''
    sum = 0.0; num = 0
    print "name %s" % (name,)
    for key in nameScore[name].keys():
        print "subject: %s, score: %d" % (key, nameScore[name][key])
        sum += nameScore[name][key]
        num += 1
    print "avg: %.2f" % (sum*1.0/num,)


nameScore = get()
print nameScore
name = raw_input("please input a name to search: ")
search(nameScore, name)