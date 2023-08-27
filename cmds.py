# Here is the command definition document.
# Here you can manage what commands to enter before using them.
# System defined commands and user-defined commands can be defined here.
# If you have customized a command, please add it here. However, you cannot modify (not create) the code in any case!!!


import time,os,sys
import commands.default as z_sys
import commands.user_custom as z_user
import docs.help as z_sys_hp
def welcome():
    print("欢迎！")
    time.sleep(1)
    print("正如您所看到的，这是一个特别简单的命令行终端")
    print("*您可以在\">>\"之后输入一些命令以达成你的一些目的。")
    print("*如果您对它有问题，您可以在\">>\"之后输入\"help\"来获取帮助文档，或者在\"https://5h9igzqanx.github.io/TRDWBST\"联系作者。")
    print("*如果您想退出，您可以在\">>\"之后输入\"exit\"或点击右上角的关闭按钮")
    time.sleep(1)
    input_z()
def input_z():
    input_zz = input('>>')
    while input_zz == '':
        input_zz = input('>>')
    judge_z(input_zz)
def judge_z(input_zz):
    if input_zz == "":
        pass
    elif input_zz in ["exit","quit","退出"]:
        z_sys.exit()
    elif input_zz in ["Help","help"]:
        z_sys_hp.z_help()
    elif input_zz in ["practice","practise"]:
        z_sys.practice()
    elif input_zz in ["test"]:
        z_sys.test()
    elif input_zz in ["tool"]:
        z_sys.tool()
    else:
        z_sys.no_command(input_zz)
    print()
    input_z()