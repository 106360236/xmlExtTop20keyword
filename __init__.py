import re, xml.etree.ElementTree
def __not_empty__(s): return s and s.strip()    #檢測元素是否為空
def __rm_alpha__(lst):   #刪除list中數字元素
    [lst.remove(i) for i in lst if type(i) == type(1450)]
    return lst
def __Print_keywd__(wd_dict):
    lst=list()
    print('|===========Top 20 of keywords in this file===========|') 
    print('|===Rank==========Word==========Number of occurrence==|')
    for rk in range(20):
       print('{:<1}{:>6}{:>1}{:^23}{:<1}{:^22}{:>1}'.format('|',str(rk+1),'|',wd_dict[rk][0],'|',wd_dict[rk][1],'|'))
       lst.extend( __rm_alpha__( list(wd_dict[rk])))	#創建出現次數前20的單字list
    print('|=====================================================|') 
    return lst
def __Print_combkw__(top20_lst,wd_lst):
    comb_wd_dict=dict()
    print('|============Combination words in this file===========|')
    for i in range(20):
        for j in range(20):
            if j!=i:
                sub_str=top20_lst[i]+' '+top20_lst[j]
                str1=' '.join(wd_lst)
                comb_wd_dict.setdefault(sub_str,str1.count(sub_str))
    comb_wd_dict=sorted( comb_wd_dict.items(), key=lambda comb_wd_dict:comb_wd_dict[1], reverse=True) 
    for rk in range(20):
        if comb_wd_dict[rk][1] > 10:
            print('{:<1}{:>6}{:>1}{:^23}{:<1}{:^22}{:>1}'.format('|',str(rk+1),'|',comb_wd_dict[rk][0],'|',comb_wd_dict[rk][1],'|'))
    print('|=====================================================|') 
	
    assign=input('The combination words with assigned length:')
    print('|=====================================================|')
    for rk in range(20):
        if len( comb_wd_dict[rk][0]) == int(assign) and ( comb_wd_dict[rk][1] > 10):
            print('{:<1}{:>6}{:>1}{:^23}{:<1}{:^22}{:>1}'.format('|',str(rk+1),'|',comb_wd_dict[rk][0],'|',comb_wd_dict[rk][1],'|'))
    print('|=====================================================|')
def __kwd_search__(lst):   #印出每篇前20的關鍵字、組合關鍵字
    wd_dict, top20_lst=dict(), list()
    [wd_dict.setdefault(i,lst.count(i)) for i in set(lst) if i not in wd_dict.keys()]   #計算list相同的元素出現次數         
    [wd_dict.pop(x, None) for x in comm_wd]         #從list中刪除常見單字
    wd_dict=sorted(wd_dict.items(), key=lambda wd_dict:wd_dict[1] ,reverse=True)   #依出現次數做排序
    top20_lst=__Print_keywd__(wd_dict)
    __Print_combkw__(top20_lst,lst)
    lst.clear()
    return top20_lst
def __Ext_for_XML__(XML,txt):
    wd_lst=list()
    print(XML)
    filename.append(XML)
    with open( XML, 'r', encoding = 'utf8') as f0, open( txt, 'w+', encoding = 'utf8') as f1:
        for event,elem in xml.etree.ElementTree.iterparse(f0):
            if  event == 'end':
                if ( elem.tag in text_lst ) and ( elem.text != None ): f1.write(elem.text+'\n')                 
                if ( elem.tag in tail_lst ) and ( elem.tail != None ): f1.write(elem.tail)                   
            elem.clear()
        f1.seek(0)
        for li in f1.readlines():        ##將文章轉換成單字list
            li_lst=re.sub("[,.;'\n]"," ",li.lower()).split(' ')
            wd_lst.extend(filter(__not_empty__, li_lst))  
    return __kwd_search__(wd_lst)