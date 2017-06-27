from tkinter import*
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter.font import*
from ip import *
from __init__ import *
class MyText:   #文本输入/输出框
    def __init__(self,root,type):
        self.root=root
        self.frame1=Frame(root)
        if type==0:
            self.lb=Label(self.frame1,text='分词原文')
            self.lb.pack()
            self.frame1.pack()
        if type==1:
            self.lb=Label(self.frame1,text='快速分词结果')
            self.lb.pack()
            self.frame1.pack()
        if type==2:
            self.lb=Label(self.frame1,text='hmm分词结果')
            self.lb.pack()
            self.frame1.pack()
        self.frame=Frame(root)
        self.T=Text(self.frame,width=100,height=12)
        self.sl=Scrollbar(self.frame)
        self.sl.pack(side=RIGHT,fill=Y)
        self.T['yscrollcommand']=self.sl.set
        self.T.pack(side=LEFT)
        self.sl['command'] = self.T.yview
        self.frame.pack()
    def insert(self,r):
        self.T.insert(1.0,r)
    def clear(self):
        self.T.delete(1.0,END)
    def get(self):
        return self.T.get(1.0,END)
        #精准分词

class Mybottun:  #主界面按钮
    def __init__(self,root,text1,text2,text3,menu):
        self.root=root
        self.text1=text1
        self.text2=text2
        self.text3=text3
        self.menu=menu
        self.frame=Frame(root)
        self.text=StringVar()
        self.text.set('')
        #self.label=Label(self.frame,textvariable=self.text,fg='red',image=self.bm,compound='left',width=200,height=75)
        #self.label.pack(side=LEFT)
        self.bottun1=Button(self.frame,text='开始分词',command=self.start,width=12)
        self.bottun1.pack(side=LEFT,padx=15)
        self.bottun2=Button(self.frame,text='清空原文',command=self.clean1,width=12)
        self.bottun2.pack(side=LEFT,padx=15)
        self.bottun3=Button(self.frame,text='清空结果',command=self.clean2,width=12)
        self.bottun3.pack(side=LEFT,padx=15)
        self.frame.pack(side=BOTTOM,ipady=10)
    def start(self):
        result=[]
        trans, emit, init = load_data()
        trans = ExtendDict.MakeExtendDict(trans)
        emit = ExtendDict.MakeExtendDict(emit)
        init = ExtendDict.MakeExtendDict(init)
        states = 'BMES'
        hmm_model = HMM(trans, emit, init, states)

        #简单
        cidian=rf('199801.txt')
        trie={}
        gen_trie(cidian,trie)
        if self.text1.get()=='\n':
            showerror(title='错误',message='分词输入内容不能为空！')
        else:
            sentences=self.text1.get()
            for i in range(len(sentences)):
                result.append(sentences[i])
            self.text2.clear()
            self.text2.insert(left_seg(sentences,trie))
            path = hmm_model.viterbi(sentences)
            self.text3.clear()
            self.text3.insert(cut(sentences, path))
            self.text.set('分词完毕')
    def clean1(self):
        if askquestion(title='提示',message='真的要清空分词原文么？') == 'yes':
            self.text1.clear()
    def clean2(self):
        if askquestion(title='提示',message='真的要清空分词结果么？') == 'yes':
            self.text2.clear()
            self.text.set('')

class MyMenu:   #主菜单
    def __init__(self,root,text1,text2,text3):
        self.root=root
        self.text1=text1
        self.text2=text2
        self.text3=text3
        self.v=IntVar()
        self.v.set(2)        
    def quit(self):
        root.destroy()

            
if __name__=='__main__':
    root=Tk()
    root.title('fmm与bmm简单分词')
    text1=MyText(root,0)
    text2=MyText(root,1)
    text3=MyText(root,2)
    menu=MyMenu(root,text1,text2,text3)
    bottun=Mybottun(root,text1,text2,text3,menu)
    root.mainloop()
