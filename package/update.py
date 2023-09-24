"""
这里是软件自动更新程序,主要为自动获取更新和下载安装包
但是不知道由于什么原因报错信息上面会有"HTTP Error 404:Not Found",所以我就先禁用了
"""

import time,os,sys,wget
def update(mode):
    old_ver = "0.1.4-beta"#version
    wget.download("https://5h9igzqanx.github.io/project-version/version/zx-MyCdss.txt")
    vn = open("zx-MyCdss.txt")
    vern = vn.readlines()
    new_ver = vern[0]
    download_link = vern[1]
    vn.close
    os.system("del package\\zx-MyCdss.txt")
    if old_ver != new_ver:
        print("New version found,update?(y/n)")
        time.sleep(0.1)
        update_cmd = input(">>")
        if update_cmd in ["y","Y"]:
            print("Downloading updates...")
            wget.download(download_link)
            print("Setup is about to run.Please close the program manually...")
            #os.system("MyCdss Setup.exe")
            time.sleep(0.1)
            #sys.exit()
        else:
            print("You canceled the update. We will prompt you for the update next time you start.")
    else:
        os.remove("zx-MyCdss.txt")
        if mode == 0:
            pass
        elif mode == 1:
            print("↓→No update.")
    print()
    time.sleep(0.1)
update(1)