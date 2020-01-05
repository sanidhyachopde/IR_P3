# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse

core = "DFR"
filepath = '/Users/sanidhya/1st Sem/Information Retreival/Projects/Project3/project3_data/queries.txt'
with open(filepath) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.split()
        query = ' '.join(line[1:])
        query = urllib.parse.quote(query)
        fields = ['text_en','text_de','text_ru']

        for field_type in fields:
            inurl = 'http://3.133.85.28:8983/solr/'+core+'/select?q='+field_type+'%3A'+query+'&fl=id%2Cscore&wt=json&indent=true&rows=20&defType=edismax&qf='+field_type+'^3'
            outfn = '/Users/sanidhya/1st Sem/Information Retreival/Projects/Project3/Submissibles/DFR/'+line[0]+'.txt'

            qid = line[0]
            IRModel='DFR'
            outf = open(outfn, 'a')
            data = urllib.request.urlopen(inurl)

            docs = json.load(data)['response']['docs']
            # the ranking should start from 1 and increase
            rank = 1
            for doc in docs:
                outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
                rank += 1
            outf.close()
