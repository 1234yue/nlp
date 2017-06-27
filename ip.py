# -*- coding: utf-8 -*-
# duqu yuliao

def rf(name):
    f=open(name,'r',encoding='GBK')
    ciwo=[]
    for line in f.readlines():
        word=line.split()
        for w in word:
            if w.split('/')[0]!='w':
                ciwo.append(w.split('/')[0])
    return ciwo

# trie 
def gen_trie(cidian,trie):
    lfreq = {}        
    ltotal = 0.0
    for word in cidian:
        
        p=trie
        for c in word:
            if c not in p:
                p[c]={}
            p=p[c]
        p['']=''

#trie can or not find word
def find_word(word,trie):
    p=trie
    for w in word:
        if w not in p:
            return False
        p=p[w]
    if '' in p and p['']=='':
        return True
        
#分词
def left_seg(text,trie):
    length=5
    if len(text)<=1:
        return text
    if len(text)<length:
        length=len(text)
    while length>1:
        if(find_word(text[:length],trie)):
            return text[:length]+'/'+left_seg(text[length:],trie)
        length=length-1
    return text[0]+'/'+left_seg(text[1:],trie)
            

        
if __name__=='__main__':
    cidian=rf('199801.txt')
    trie={}
    gen_trie(cidian,trie)
    name='ok'
    while name!='end':
        name = input("请输入：");
        print(len(name))
        print(left_seg(name,trie))

