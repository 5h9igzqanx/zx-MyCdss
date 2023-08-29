# Here is the command definition document.
# Here you can manage what commands to enter before using them.
# System defined commands and user-defined commands can be defined here.
# If you have customized a command, please add it here. However, you cannot modify (not create) the code in any case!!!


import time,os,sys,colorama
#from colorama import Fore,Back,Style,init
import commands.default as z_dft
import commands.user_custom as z_user
import docs.help as z_dft_hp
def welcome():
    colorama.init(autoreset = True)
    print(colorama.Fore.RED + "欢迎！")
    time.sleep(1)
    print(colorama.Fore.RED + "正如您所看到的,这是一个特别简单的命令行终端")
    print(colorama.Fore.YELLOW + "*您可以在\">>\"之后输入一些命令以达成你的一些目的")
    print(colorama.Fore.YELLOW + "*如果您对它有问题,您可以在\">>\"之后输入\"help\"来获取帮助文档,或者在\"https://5h9igzqanx.github.io/TRDWBST\"联系作者")
    print(colorama.Fore.YELLOW + "*如果您想退出,您可以在\">>\"之后输入\"exit\"或点击右上角的关闭按钮")
    time.sleep(1)
    input_z()
def input_z():
    input_zz = input(colorama.Fore.GREEN + '>>')
    while not (input_zz):
        input_zz = input(colorama.Fore.GREEN + '>>')
    judge_z(input_zz)
def judge_z(input_zz):
    if not (input_zz):
        pass
    elif input_zz in ["exit","quit","退出"]:     #内置命令:退出
        z_dft.exit()
    elif input_zz in ["Help","help","帮助"]:     #内置命令:帮助
        z_dft_hp.z_help()
    elif input_zz in ["practice","practise"]:
        z_dft.practice()
    elif input_zz in ["test"]:
        z_dft.test()
    elif input_zz in ["tool"]:
        z_dft.tool()
    elif input_zz in ["毁灭地球","核弹","爆炸"]:
        z_dft.rickroll()
    else:
        z_dft.no_command(input_zz)
    print(colorama.Fore.GREEN + "↓")
    input_z()