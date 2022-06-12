### download the trained network through
链接：https://pan.baidu.com/s/16FSll_JWFf3ByUdV6rwpRQ?pwd=uymb 
提取码：uymb

### run the following instruments

```
pip install torch===1.7.1 torchvision===0.8.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install bert_seq2seq
```

after configuring the environment



run 

```
python 小说简介分类.py
```

Enter some introduction of the novel, then push the buttom, the result will show in the right pannel.

You can try:

　　传说，在那古老的星空深处，伫立着一道血与火侵染的红色之门。
　　传奇与神话，黑暗与光明，无尽传说皆在这古老的门户中流淌。
　　俯瞰星门，热血照耀天地，黑暗终将离去！

It should output 玄幻.

Or you can get the test data in www.qidian.com.