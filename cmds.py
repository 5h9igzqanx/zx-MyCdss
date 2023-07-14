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
    print("您可以在\">>\"之后输入一些命令或问我一些问题。")
    print("如果您不熟悉它，您可以在QQ上搜索\"2109511809\"来找我，或者在\">>\"之后输入\"help\"来获取帮助文档。")
    print("如果您想退出，您可以在\">>\"之后输入\"exit\"或按右上角的关闭按钮")
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
    elif input_zz in ["exit","bye","quit","退出"]:
        z_sys.exit()
    elif  input_zz in ["Help","help"]:
        z_sys_hp.z_help()
    elif input_zz in ["practice","practise","Practice","Practise"]:
        z_sys.practice()
    elif input_zz == "system":
        z_sys.system()
    elif input_zz == "test":
        z_sys.test()
    else:
        z_sys.no_command(input_zz)
    input_z()