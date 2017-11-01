#coding:utf-8
import init
import custom_download
import userinfo
import respose
import time
print u"使用须知：请将utorrent下载文件前的询问关闭\n"
def run():
    if not respose.if_login_success():
        init.login()
    if not custom_download.if_utorrent_path_right():
        init.get_utorrent_path()
    print u"当前用户信息:\n"
    userinfo.print_user_info()
    custom_download.start_download()
if __name__ == "__main__":
    while(True):
        print u"系统运行中\n"
        run()
        print u"系统休眠中\n"
        time.sleep(180)