import time,os,sys,wget
def update():
    old_ver = "0.1.4-beta"#version
    wget.download("https://5h9igzqanx.github.io/project-version/version/zx-MyCdss.txt")
    vn = open("zx-MyCdss.txt")
    vern = vn.readlines
    new_ver = vern[0]
    download_link = vern[1]
    vn.close
    os.system("del package\\zx-MyCdss.txt")
    if old_ver != new_ver:
        print("New version found, update?(y/n)")
        update_cmd = input(">>")
        if update_cmd == "y" or update_cmd == "Y":
            print("Downloading updates...")
            wget.download(download_link)
            print("Setup is about to run. Please close the program manually...")
            os.system("MyCmds Setup.exe")
            time.sleep(0.1)
            sys.exit()
        else:
            pass
    else:
        pass
    time.sleep(0.1)