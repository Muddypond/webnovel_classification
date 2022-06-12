# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 23:10:01 2021

@author: 烂泥塘
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import time
import tkinter.filedialog

import torch 
import sys
from bert_seq2seq.tokenizer import Tokenizer, load_chinese_base_vocab
import os
import json
import time
import bert_seq2seq
from bert_seq2seq.utils import load_bert
#  from sklearn.metrics import f1_score
# import pandas as pd

LOG_LINE_NUM = 0


class MY_GUI():
    
    
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("小说简介分类")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待分类小说简介")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="类别")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=20)  #原始数据录入框
        self.init_data_Text.grid(row=0, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="分类", bg="lightblue", width=10,command=self.classify)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
        #选择csv文件
        # self.str_trans_to_md5_button = Button(self.init_window_name, text="选择文件", bg="lightblue", width=10,command=self.classify)  # 调用内部方法  加()为直接调用

        self.str_trans_to_md5_button.grid(row=10, column=11)


    #功能函数
    # def getTestData(self,filename):
    #     data=pd.read_excel(filename,index_col=0)
    #     #清洗数据
    #     sents_src = []   
    #     data['content']=data['content'].str.replace('【.*】','',regex=True)
    #     data['content']=data['content'].str.replace('\t','',regex=True)
    #     data['content']=data['content'].str.replace('\n','',regex=True)
    #     data['content']=data['content'].str.replace('当时使用浏览器版本过低，请升级','',regex=False)
    #     data['content']=data['content'].str.replace(' ','')
    #     data['content']=data['content'].str.replace('本文由游民星空制作发布，未经允许禁止转载。','')
    #     data['content']=data['content'].str.replace('{.*}','')
    #     data['content']=data['content'].str[:200]
    #     data['title']=data['title'].str.replace('【.*】','',regex=True)
    #     data['title']=data['title'].str.replace('\t','',regex=True)
    #     data['title']=data['title'].str.replace('\n','',regex=True)
    #     data['title']=data['title'].str.replace(' ','')
    #     data['title']=data['title'].str.replace('“','')
    #     data['title']=data['title'].str.replace('”','')
    #     data['title']=data['title'].str.replace('"','')
    #     data["新闻"] = data["title"].map(str)+data["content"].map(str) 
    #     for i in range(len(data)):
    #       sents_src.append(data['新闻'].iloc[i])
          
    #     return sents_src
    # def choose(self):
    #     filename=tkinter.filedialog.askopenfilename()
    #     if filename == '':
    #         self.write_log_to_Text('您没有选择任何文件')
    #         return
    #     self.write_log_to_Text('您选择的文件是'+filename)
    #     cls_model = "novel.bin"
    #     device = torch.device("cpu")
    #     target = ["都市", "言情", "仙侠", "军事", "科幻", "历史","奇幻","轻小说","体育","武侠","仙侠","现实","玄幻","悬疑","游戏","诸天无限"]
    #     vocab_path = "vocab.txt"  # roberta模型字典的位置
    #     model_name = "roberta"  # 选择模型名字
    #     # 加载字典
    #     word2idx = load_chinese_base_vocab(vocab_path, simplfied=False)
    #     tokenizer = Tokenizer(word2idx)
    #     # 定义模型
    #     bert_model = load_bert(word2idx, model_name=model_name, model_class="cls", target_size=len(target))
    #     bert_model.set_device(device)
    #     bert_model.eval()
    #     ## 加载训练的模型参数～
    #     bert_model.load_all_params(model_path=cls_model, device=device)
    #     test_data = self.init_data_Text.get(1.0,END).strip().replace("\n","").split("\n")
        
    #     test_data = self.getTestData(filename)
    #     y_pred=[]
    #     for text in test_data:
    #         temp=text
    #         with torch.no_grad():
    #             text, text_ids = tokenizer.encode(text)
    #             text = torch.tensor(text, device=device).view(1, -1)
    #             y_pred.append(torch.argmax(bert_model(text)).item())
        
    #     data=pd.read_excel(filename,index_col=0)
    #     newTarget = ["都市", "言情", "仙侠", "军事", "科幻", "历史","奇幻","轻小说","体育","武侠","仙侠","现实","玄幻","悬疑","游戏","诸天无限"]
    #     channelList=[]
    #     for i in y_pred:
    #         channelList.append(newTarget[i])
    #     data['channelName']=channelList
    #     data.to_excel("测试结果输出.xlsx",encoding='utf_8')
    #     self.write_log_to_Text("INFO:classify success")
    #     self.write_log_to_Text("INFO:带有预测标签的excel文件已存在当前文件夹  文件名:测试结果输出.xlsx")
    #     print("done")


 
    def classify(self):

        cls_model = "novel.bin"
        device = torch.device("cpu")
        target = ["都市", "言情", "仙侠", "军事", "科幻", "历史","奇幻","轻小说","体育","武侠","仙侠","现实","玄幻","悬疑","游戏","诸天无限"]
        vocab_path = "vocab.txt"  # roberta模型字典的位置
        model_name = "roberta"  # 选择模型名字
        # 加载字典
        word2idx = load_chinese_base_vocab(vocab_path, simplfied=False)
        tokenizer = Tokenizer(word2idx)
        # 定义模型
        bert_model = load_bert(word2idx, model_name=model_name, model_class="cls", target_size=len(target))
        bert_model.set_device(device)
        bert_model.eval()
        ## 加载训练的模型参数～
        bert_model.load_all_params(model_path=cls_model, device=device)
        test_data = self.init_data_Text.get(1.0,END).strip().replace("\n","").split("\n")


        for text in test_data:
            if text:
                try:
                    text, text_ids = tokenizer.encode(text)
                    text = torch.tensor(text, device=device).view(1, -1)
                    #print(myMd5_Digest)
                    #输出到界面
                    self.result_data_Text.delete(1.0,END)
                    self.result_data_Text.insert(1.0,target[torch.argmax(bert_model(text)).item()])
                    self.write_log_to_Text("INFO:classify success")
                except:
                    self.result_data_Text.delete(1.0,END)
                    self.result_data_Text.insert(1.0,"其他")
            else:
                self.write_log_to_Text("ERROR:classify failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
