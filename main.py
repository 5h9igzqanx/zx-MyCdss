import colorama,time,os,webbrowser

file = ["commands/__init__.py","commands/default.py","docs/help.py","docs/help.txt","package/update.py"]
isfile=[]
for i in file:
    if not (os.path.exists(i)):
        isfile.append(i)
    else:
        pass
if (isfile):
    colorama.init(autoreset=True)
    print(colorama.Fore.RED + "↓→软件似乎被破坏,请重新安装")
    print(colorama.Fore.YELLOW + "↓*丢失的文件:" , isfile)
    print(colorama.Fore.RED + "↓→我们将为您打开软件下载页,请稍后...")
    webbrowser.open("https://github.com/5h9igzqanx/zx-MyCdss/releases",new=0,autoraise=True)
    print(colorama.Fore.RED + "↓→如果未自动打开,请复制" + colorama.Fore.BLUE + "\"https://github.com/5h9igzqanx/zx-MyCdss/releases\"" + colorama.Fore.RED + "到浏览器手动下载")
    print(colorama.Fore.RED + "↓→再见,这是最后一次与您道别了")
    os.system("pause")
else:
    import cmds as cmd_zx
    # import package.update as upd_zx
    # upd_zx.update(0)
    cmd_zx.welcome()