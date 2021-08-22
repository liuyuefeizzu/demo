from Bio import Entrez
my_mail='228701844@qq.com'
db='pubmed'
term='python and bioinformatics'
term2='Exosome surface protein'
h_search=Entrez.esearch(db=db,email=my_mail,term=term2)
record=Entrez.read(h_search)
#print record


'''for key,value in record.iteritems():
                print key+'----'
                print value
                print'''
h=Entrez.esummary(db=db,id=record['IdList'][9],email=my_mail)
sum=Entrez.read(h)
#print sum
for key,value in sum[0].iteritems():
                print key
                print value
                print

res_ids=record['IdList']
for r_id in res_ids:
                h_summ=Entrez.esummary(db=db,id=r_id,email=my_mail)
                summ=Entrez.read(h_summ)
                #print summ
                print summ[0]['Title']
                print ('======================================================')
