#codinf:utf-8
import requests
import pickle
import re
def get_respose(url):
    session = requests.session()
    with open("cookie", 'rb') as f:
        content=f.read()
        f.close()
    if(content):
        with open("cookie", 'rb') as f:
            cookies=pickle.load(f)
        respose=session.get(url,cookies=cookies)
    else:
        respose=session.get(url)
    return respose
def if_login_success():

    testpage = get_respose("http://bt.byr.cn/userdetails.php?id=247525").content
    testpattren = "lsqlsq"
    test_result = re.findall(testpattren, testpage)
    if test_result:
        return True
    else:
        return False
