#coding:utf-8
import respose
import re
from bs4 import BeautifulSoup
def tran_to_GB(row_size):
    row_size=row_size.split()
    num=float(row_size[0])
    unit=row_size[1]
    unit_dic={"KB":0.000001,"MB":0.001,"GB":1,"TB":1000,"PB":1000000}
    size=num*unit_dic[unit]
    return size
def num_tool(string):
    #string=str(string)
    pattern=re.compile(r'\d*')
    num=re.findall(pattern,string)
    num=num[0]
    return int(num)
def get_torrent_info(id):
    url="http://bt.byr.cn/details.php?id="+str(id)+"&hit=1"
    page=BeautifulSoup(respose.get_respose(url).content,"lxml")
    name=page.find('a',attrs={"href":"download.php?id=%s"%str(id)}).string
    size=tran_to_GB(page.find('b',text=u"大小：").next_element.next_element.next_element.strip())#单位是GB
    seeder=page.find(attrs={'id':"peercount"}).b
    downloader=num_tool(seeder.next_element.next_element.next_element.string)
    seeder=num_tool(seeder.string)
    iffree = False
    twofree = page.find_all(name='font', attrs={'class': 'free'})
    free = page.find_all(name='font', attrs={'class': 'twoupfree'})
    if (free or twofree):
        iffree = True
    id=int(id)
    return (id,name,size,seeder,downloader,iffree)
def print_torent_info(id):
    info=get_torrent_info(id)
    print u"ID:%s 名称：%s  \n大小：%s GB  做种人数：%s  下载人数：%s 免费：%s "%info


