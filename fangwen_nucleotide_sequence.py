# -*- coding: cp936 -*-




def main(name):

           


                
                from liuyuefei import duxiewenjian
                from Bio import Entrez
                n='nucleotide'
                l=duxiewenjian.dwj()
                print l
                seq=''
                a=0
                for ids in l:
                                handle=Entrez.efetch(db=n,id=ids,rettype='fasta',email='user@qq.com')
                                result=handle.read()
                                print result
                                seq+=result
                                a+=1
                if a == len(l):
                                duxiewenjian.xwj(seq,name)
                                return True
                else:
                                return False
                
 


                
