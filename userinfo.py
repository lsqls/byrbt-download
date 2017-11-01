#coding:utf-8
import respose
from bs4 import BeautifulSoup
def getmyinfo():
    url="http://bt.byr.cn/index.php"
    page=BeautifulSoup(respose.get_respose(url).content,"lxml")
    info=page.find_all(attrs={"class":"color_bonus"})
   # magic=info[0].next_element.next_element.next_element.next_element.next_element
    upload_rank=info[1].next_element.next_element.strip()
    share_rate=page.find(attrs={"class":"color_ratio"}).next_element.next_element.strip()
    upload_size=page.find(attrs={"class":"color_uploaded"}).next_element.next_element.strip()
    download_size=page.find(attrs={"class":"color_downloaded"}).next_element.next_element.strip()
    download_num=page.find(attrs={"class":"arrowdown"}).next_element.strip()
    seeder_num=page.find(attrs={"class":"arrowup"}).next_element.strip()
    return (upload_rank,share_rate,upload_size,download_size,download_num,seeder_num)
def print_user_info():
    info=getmyinfo()
    print u"上传排名：%s  分享率：%s  上传量：%s  下载量：%s  当前下载数：%s   当前做种数：%s\n"%info

