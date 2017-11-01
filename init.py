#coding:utf-8
import requests
import re
import requests.utils
import pickle
import os
import getpass
import json
headers={
    "Cookie": "_ga=GA1.2.111167924.1509423972; _gid=GA1.2.812648973.1509423972; _gat=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Host":"bt.byr.cn",
    "Referer":"http://bt.byr.cn/"
    }
def login():
    login_success=False
    print ("*"*20+u"请初始化登陆系统"+"*"*20+"\n")
    data={
    'username': "",
    'password': "",
    'imagehash': '',
    'imagestring': '',
    }
    while(not login_success):
        print u"输入您的用户名:\n"
        username=raw_input()
        print u"输入您的密码:\n"
        password=raw_input()
        data[ 'username']=username
        data['password']=password
        session=requests.session()
        page=session.get("http://bt.byr.cn/login.php",headers=headers).text
        pattern = r'img src="image\.php\?action=regimage&amp;imagehash=(\S*)"'
        __imagehash=re.findall(pattern,page)
        imagehash=__imagehash[0]
        imgurl="http://bt.byr.cn/image.php?action=regimage&imagehash="+str(imagehash)
        __imgpage=session.get(imgurl,headers=headers)
        img=open("code.jpg",'wb')
        img.write(__imgpage.content)
        img.close()
        print u"输入%s下code.jpg中的验证码\n"%os.getcwd()
        imagestring=raw_input()
        data["imagehash"]=imagehash
        data["imagestring"]=imagestring
        loginpage=session.post("http://bt.byr.cn/takelogin.php",data=data,headers=headers)
        testpage=session.get("http://bt.byr.cn/userdetails.php?id=247525").content
        testpattren="lsqlsq"
        test_result=re.findall(testpattren,testpage)
        if (test_result):
            with open("cookie", 'wb') as f:
                pickle.dump(session.cookies, f)
            login_success=True
            print (u"%s，您已成功登陆"%username)
        else:
            print (u"登陆失败,请重新登陆\n")


def get_utorrent_path():
    if_default_path=os.path.isdir("C:\Users\%s\AppData\Roaming\uTorrent"% getpass.getuser())
    if if_default_path:
        utorrent_path="C:\Users\%s\AppData\Roaming\uTorrent"% getpass.getuser()+"\uTorrent.exe"
    else:
        print u"输入本机utorrent的安装目录:\n"
        install_path=raw_input()
        utorrent_path=install_path+"\uTorrent.exe"
    with open("pathconfig", 'wb') as f:
        f.write(utorrent_path)
        f.close()
