#coding:utf-8
import respose
from bs4 import BeautifulSoup
import re
import torrent_info
import os
import excsv
import json
def get_have_download_list():
    with open('downloaded','r') as f:
            list=[]
            downloadeds=f.read()
            downloadeds=downloadeds.split()
            for downloaded in downloadeds:
                list.append(downloaded)
            f.close()
            return list
def get_torrent_list():
    html = BeautifulSoup(respose.get_respose("http://bt.byr.cn/").content, 'lxml')
    table = html.find(name='table',attrs={'width': '100%', 'border': '1', 'cellspacing': '0', 'cellpadding': '5'})
    pattern=re.compile(r'details.php\?id=(.*?)&')
    idlist=list(set(re.findall(pattern,str(table))))
    torrentlist = []
    for id in idlist:
        torrentinfo=torrent_info.get_torrent_info(id)
        downloadedid=get_have_download_list()
        have_downloaded=id in downloadedid
        #(id,name, size, seeder, downloader, iffree)
        if  torrentinfo[4]>=4 and torrentinfo[3]<=2 and torrentinfo[5] and (not have_downloaded):
            torrentlist.append(torrentinfo)
            excsv.add(torrentinfo)
    return torrentlist
def download(torrentlist):
    path = os.getcwd() + "\\torrentfile"
    if_path = os.path.isdir(path)
    if not if_path:
        os.mkdir(path)
    for torrent in torrentlist:
        id=torrent[0]
        downloadlink="http://bt.byr.cn/download.php?id="+str(id)
        torrent_file=respose.get_respose(downloadlink).content
        name=torrent[1]
        torrent_path=path+'\\'+name
        with open(torrent_path,'wb') as f:
            f.write(torrent_file)
            f.close()
        with open('downloaded', 'a') as f:
            f.write(str(id) + '\n')
            f.close()
        with open("pathconfig", 'rb') as f:
            software_path = f.read()
            f.close()
        cmd=software_path+' '+torrent_path
        os.system(cmd)
        print (u"下载%s成功"%name)
def if_utorrent_path_right():
    with open("pathconfig",'rb') as f:
        software_path=f.read()
        f.close()
    return os.path.isfile(software_path)
def start_download():
   torrentlist=get_torrent_list()
   download(torrentlist)