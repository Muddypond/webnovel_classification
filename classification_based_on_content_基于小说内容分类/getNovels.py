from pydoc import describe
import requests
import time
from lxml import etree
from sympy import N
from time import sleep
existedTags = {"言情","都市","玄幻","历史"}
def timing(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        ret = f(*args,**kwargs)
        print("该条用时",end="")
        print(time.time()-start)
        print("")
        return ret
    return wrapper

def getTag(name):
    baike_url = "https://baike.baidu.com/item/"+name
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
    with requests.request('GET',baike_url,headers = {'User-agent':ua}) as baikeres:
        content = baikeres.text          #获取HTML的内容
        html = etree.HTML(content)  #分析HTML，返回DOM根节点
        # for i in range(25,12)
        descriptionSpace = html.xpath( "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dt[4]/text()")  #使用xpath函数，返回文本列表

        # descriptionSpace = html.xpath( "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[1]/text()")  #使用xpath函数，返回文本列表
        try:
            print(descriptionSpace[0])
            return [True,descriptionSpace[0]]
        except:
            return [False]

@timing
def download(id,name):
    # tagFV = getTag(name)
    # if not tagFV[0]:
    #     return
    # tag = tagFV[1]
    # global existedTags
    # existedTags.add(tag)
    novel_url = "https://www.55txt.cc/api/txt_down.php?articleid="+str(id)+"&articlename="+name
    response = requests.get(url=novel_url)  
    novel_bytes = response.content
    temp_novel_path = name+'.txt'
    with open(temp_novel_path, 'wb') as f:
        f.write(novel_bytes)
    print("done for",name)
    


# download(1,"惊悚乐园")
# print(existedTags)
tstart = time.time()
for id in range(300,500):
    print(id)
    url = "https://www.55txt.cc/read/txt"+str(id)+".html"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session() 
    s.keep_alive = False
    with requests.request('GET',url,headers = {'User-agent':ua}) as res:
        content = res.text          #获取HTML的内容
        html = etree.HTML(content)  #分析HTML，返回DOM根节点
        nameSapce = html.xpath( "/html/body/div[2]/section/div[1]/div/h1/text()")  #使用xpath函数，返回文本列表
        name = nameSapce[0]
        print("try to download",name)
        download(id,name)
    sleep(1)
print("总时长",time.time()-tstart)