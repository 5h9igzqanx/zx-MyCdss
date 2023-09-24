"""
这里是命令定义文档
您可以在这里管理在使用命令之前要输入的命令
在此处定义的是系统定义的命令和用户定义的命令
如果您已经自定义了一个命令,请将其添加到此处.但是,无论如何都不要修改(不是创建)代码!!!
"""


import time,os,sys,colorama
import commands.default as z_dft
import commands.user_custom as z_user
import docs.help as z_dft_hp
def welcome():
    colorama.init(autoreset=False)
    for i in [colorama.Fore.RED,"欢","迎","!\n"]:
        print(i,end="",flush=True)
        time.sleep(0.02)
    time.sleep(1)
    welcome = [colorama.Fore.RED,"正","如","您","看","到","的",",","这","是","一","个","特","别","简","单","的","命","令","行","终","端\n",colorama.Fore.YELLOW,"*您","可","以","在","\">>\"","后","输","入","一","些","命","令","来","达","成","您","的","一","些","目","的\n",colorama.Fore.YELLOW,"*如","果","您","认","为","它","有","问","题",",","您","可","以","在","\">>\"","后","输","入","\"help\"","来","获","取","帮","助","文","档",",","或","在","\"https://github.com/5h9igzqanx/zx-MyCdss/issues\"","联","系","作","者\n",colorama.Fore.YELLOW,"*如","果","您","想","退","出",",","您","可","以","在","\">>\"","后","输","入","\"exit\"",",","或","点","击","右","上","角","的","\"X\"\n"]
    for i in welcome:
        print(i,end="",flush=True)
        time.sleep(0.02)
    colorama.init(autoreset=True)
    time.sleep(1)
    input_z()
def input_z():
    input_zz = input(colorama.Fore.GREEN + '>>' + colorama.Fore.BLUE)
    while not (input_zz):
        input_zz = input(colorama.Fore.GREEN + '>>' + colorama.Fore.BLUE)
    judge_z(input_zz)
def judge_z(input_zz):
    if not(input_zz):
        pass
    elif input_zz in ["exit","quit","退出"]:     # 底层命令:退出
        z_dft.exit()
    elif input_zz in ["Help","help","帮助"]:     # 底层命令:帮助
        z_dft_hp.z_help()
    elif input_zz in ["bell"]:
        z_dft.bell()
    elif input_zz in ["file"]:
        z_dft.fIle()
    elif input_zz in ["practice","practise"]:
        z_dft.practice()
    elif input_zz in ["test"]:
        z_dft.test()
    elif input_zz in ["tool"]:
        z_dft.tool()
    elif input_zz in ["widget"]:
        z_dft.widget()
    elif input_zz in ["毁灭地球","核弹","爆炸"]:
        z_dft.rickroll()
    else:
        z_dft.noCommand(input_zz)
    print(colorama.Fore.GREEN + "↓")
    input_z()