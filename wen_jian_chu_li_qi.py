# -*- coding: cp936 -*-
import xml.etree.ElementTree as ET
import os
#######################
fh=open("CESC.csv",'w')
################################################################
zi_qing_dan=['race','clinical_stage','clinical_T','clinical_N','clinical_M','gender','agent_total_dose_count','age_at_initial_pathologic_diagnosis','pathologic_stage','pathologic_T','pathologic_M','pathologic_N']
fh.write(','.join(zi_qing_dan)+'\n')
###################################
def wjclq(path,zi_qing_dan):
    record=''
    tree=ET.parse(path)
    root=tree.getroot()
    for i in root.getiterator():#先将标签处理一下，删掉url,很重要
        i.tag=i.tag.split('}',1)[1]
    for i in zi_qing_dan:
        if root.getiterator(i):
            for x in root.getiterator(i):
                record+=(str(x.text)+',')
    record=record[:-1]
    record+='\n'
    return record
#################################
import os
lst=os.walk(os.getcwd())#生成root,dirs,files三元组列表，根据路径递归获得
for root, dirs, files in lst:
    for f in files:
        if os.path.splitext(f)[1] == '.xml':
            path=os.path.join(root,f)#获得路径加文件名
            record=wjclq(path,zi_qing_dan)
            fh.write(record)
####################################
fh.close()
