# 这是内置的命令定义文档
# 如果您不是专业人士,请不要修改这里的文件,这可能会伤害您的电脑！
# 展示时间
# ==================================================================================================================================================
# ==================================================================================================================================================
# 导入
import time,os,sys,wget,webbrowser,colorama
# ========================
# 特殊符号
# ==================================================================================================
# A
def a():
    print("↓→aassxsw114514")
# ==================================================================================================
# B
def b():
    print("↓→bseuxqy114514")
# ==================================================================================================
# C
def c():
    print("↓→chyewiq114514")
# ==================================================================================================
# D
def d():
    print("↓→dqshsui114514")
def deselect(level):                     #附属于任何带有"exit"的elif分支
    print(colorama.Fore.RED + "→" + level*"--" + "→选择已取消")
    return
# ==================================================================================================
# E
def e():
    print("↓→edysjsi114514")
def exit():                              #系统退出
    print(colorama.Fore.RED + "→→再见")
    time.sleep(1)
    sys.exit(0)
# ==================================================================================================
# F
def f():
    print("↓→fsialxq114514")
def fIle():
    print(colorama.Fore.RED + "↓→这是一个文件操作命令\n↓→你可以在这里对你的文件进行一些操作")
    directory = input(colorama.Fore.GREEN + "↓→请选择一个目录>>" + colorama.Fore.BLUE)
    while (not(os.path.exists(directory))) or directory in ["exit"]:
        if directory in ["exit"]:
            deselect(0)
            return
        directory = input(colorama.Fore.GREEN + "↓→目录无效,请重新选择>>" + colorama.Fore.BLUE)
    print(colorama.Fore.YELLOW + "↓→请选择你想执行的任务...")
    print(colorama.Fore.YELLOW + "↓*[...]")
    i = input(colorama.Fore.GREEN + ">file>>" + colorama.Fore.BLUE)
    while i not in ["exit"]:
        i = input(colorama.Fore.GREEN + ">file>>" + colorama.Fore.BLUE)
    if i in["114514"]:
        uncultivated()
    elif i in []:
        fIle_delete(directory = directory)
    elif i in ["exit"]:
        deselect(0)
def fIle_delete(directory):              #附属于 fIle()
    uncultivated()
# ==================================================================================================
# G
def g():
    print("↓→gqeanxz114514")
# ==================================================================================================
# H
def h():
    print("↓→hexuaqi114514")
# ==================================================================================================
# I
def i():
    print("↓→i love u(bushi)")
# ==================================================================================================
# J
def j():
    print("↓→jntm,jnszstm(bushi)")
# ==================================================================================================
# K
def k():
    print("↓→我妹K")
# ==================================================================================================
# L
def l():
    print("↓→lshznga114514")
# ==================================================================================================
# M
def m():
    print("↓→mshanxg114514")
# ==================================================================================================
# N
def n():
    print("↓→nxiwlaz114514")
def noCommand(input_zz):                #不附属于任何命令
    print(colorama.Fore.YELLOW + "↓→很抱歉,此命令 \"{0}\" 未出现在您的定义文档中,或者我们不支持此命令\n→→您可以尝试重新输入此命令或在\"user_costom.py\"自定义此命令,或在\">>\"后输入\"help\"以获取帮助".format(input_zz))
# ==================================================================================================
# O
def o():
    print("↓→o point o")
    print("↓→\"Whook whook\"")
    time.sleep(1)
    print("↓→\"Ay look at that moving eye eyes\"")
    time.sleep(2.5)
    print("↓→\"봤니 shoog shoog shoog\"")
    time.sleep(2.3)
    print("↓→\"Hook 들어와 내게 좀 더\"")
    time.sleep(2.4)
    print("↓→\"좋아 zoom zoom good\"")
# ==================================================================================================
# P
def p():
    print("↓→psabxgz114514")
def practice():
    print(colorama.Fore.RED + "↓→这条命令用于您练习\n↓→顾名思义,此命令可以帮助您熟悉此软件")
    print(colorama.Fore.YELLOW + "↓*如果您想练习,请在下面输入\"present\"；如果这是您第一次使用它,请在下面输入\"learn\"")
    time.sleep(0.1)
    i = input(colorama.Fore.GREEN + ">practice>>" + colorama.Fore.BLUE)
    while i not in ["present","learn","exit"]:
        i = input(colorama.Fore.GREEN + ">practice>>" + colorama.Fore.BLUE)
    if i in ["present"]:
        uncultivated()
    elif i in ["learn"]:
        uncultivated()
    elif i in ["exit"]:
        deselect(0)
# ==================================================================================================
# Q
def q():
    print("↓→qixznug114514")
# ==================================================================================================
# R
def r():
    print("↓→riznxco114514")
def rickroll():                          #附属于任何彩蛋
    print(colorama.Fore.YELLOW + "→→RICKROLL!")
    webbrowser.open("https://www.bilibili.com/video/BV1GJ411x7h7?t=5.2",new=0,autoraise=True)
# ==================================================================================================
# S
def s():
    print("↓→sxczhag114514")
# ==================================================================================================
# T
def t():
    print("↓→tsanzhx114514")
def test():
    print(colorama.Fore.RED + "↓→这是一个测试命令,用于测试这个软件是否可以正常使用")
    print(colorama.Fore.YELLOW + "↓*试着在这里随便打些什么吧,例如输入\"114514\"就输出\"114514114514114514\",输入exit以退出")
    while True:
        i = input(">test>>")
        if i == "exit":
            break
        else:
            print("↓→" + i * 3)
def tool():
    print(colorama.Fore.RED + "↓→这里有一些工具,其中的一些可能会帮到您")
    print(colorama.Fore.YELLOW + "↓→请选择类别...")
    print(colorama.Fore.YELLOW + "↓*[system,user,...]")
    i = input(colorama.Fore.GREEN + ">tool>>" + colorama.Fore.BLUE)
    while i not in ["system","user","exit"]:
        i = input(colorama.Fore.GREEN + ">tool>>" + colorama.Fore.BLUE)
    if i in["system"]:
        tool_system()
    elif i in ["user"]:
        uncultivated()# TODO 还没做好
    elif i in ["exit"]:
        deselect(0)
def tool_system():                       #附属于 tool()
    print(colorama.Fore.RED + "↓--→这里是系统工具\n↓--→这里备了一些常用的系统命令,所以您不用再东跑西跑了")
    print(colorama.Fore.YELLOW + "↓--→请选择您想执行的任务...")
    print(colorama.Fore.YELLOW + "↓  *[shutdown,open,...]")
    i = input(colorama.Fore.GREEN + ">tool>system>>" + colorama.Fore.BLUE)
    while i not in ["shutdown", "open","exit"]:
        i = input(colorama.Fore.GREEN + ">tool>system>>" + colorama.Fore.BLUE)
    if i in ["shutdown"]:
        tool_system_shutdown()
    elif i in ["open"]:
        tool_system_open()
    elif i in ["exit"]:
        deselect(1)
def tool_system_open():                  #附属于 tool_system()
    print(colorama.Fore.RED + "↓----→这里可以打开一些系统管理程序,或许在计算机被勒索时可以用?")
    print(colorama.Fore.YELLOW + "↓----→选择您想打开的系统管理程序")
    print(colorama.Fore.YELLOW + "↓    *[taskmgr,regedit,...]")
    j = input(colorama.Fore.GREEN + ">tool>system>open>>" + colorama.Fore.BLUE)
    while j not in ["taskmgr", "regedit","exit"]:
        j = input(colorama.Fore.GREEN + ">tool>system>open>>" + colorama.Fore.BLUE)
    if j in ["taskmgr", "任务管理器"]:
        print(colorama.Fore.YELLOW + "→----→执行成功")
        os.system("taskmgr.exe")
    elif j in ["regedit", "注册表编辑器"]:
        print(colorama.Fore.YELLOW + "→----→执行成功")
        os.system("regedit.exe")
    elif j in ["exit"]:
        deselect(2)
def tool_system_shutdown():              #附属于 tool_system()
    print(colorama.Fore.RED + "↓----→这条命令用于关机等命令的执行,但注意\"…等命令…\",额……\n↓---→所以您是想关机还是想进行其他类似的命令(注销,睡眠)")
    print(colorama.Fore.YELLOW + "↓----→请选择你想执行的任务...")
    print(colorama.Fore.YELLOW + "↓    *[shutdown,restart,logoff,sleep]")
    i = input(colorama.Fore.GREEN + ">tool>system>shutdown>>" + colorama.Fore.BLUE)
    while i not in ["shutdown", "restart", "logoff", "sleep","exit"]:
        i = input(colorama.Fore.GREEN + ">tool>system>shutdown>>" + colorama.Fore.BLUE)
    if i in ["shutdown"]:
        j = input(colorama.Fore.GREEN + "↓------→确定关机吗(y/n)>>" + colorama.Fore.BLUE)
        while j in ["y", "Y", "n", "N"]:
            j = input(colorama.Fore.GREEN + "↓------→确定关机吗(y/n)>>" + colorama.Fore.BLUE)
        if j in ["y", "Y"]:
            print(colorama.Fore.RED + "↓------→5秒后关机")
            time.sleep(5.5)
            os.system("shutdown /s")
        elif j in ["n", "N"]:
            deselect(3)
    elif i in ["restart"]:
        j = input(colorama.Fore.GREEN + "↓------→确定重启吗(y/n)>>" + colorama.Fore.BLUE)
        while j in ["y", "Y", "n", "N"]:
            j = input(colorama.Fore.GREEN + "↓------→确定重启吗(y/n)>>" + colorama.Fore.BLUE)
        if j in ["y", "Y"]:
            print(colorama.Fore.RED + "↓------→5秒后重启")
            time.sleep(5.5)
            os.system("shutdown /r")
        elif j in ["n", "N"]:
            deselect(3)
    elif i in ["logoff"]:
        j = input(colorama.Fore.GREEN + "↓------→确定注销吗(y/n)>>" + colorama.Fore.BLUE)
        while j in ["y", "Y", "n", "N"]:
            j = input(colorama.Fore.GREEN + "↓------→确定注销吗(y/n)>>" + colorama.Fore.BLUE)
        if j in ["y", "Y"]:
            print(colorama.Fore.RED + "↓------→5秒后注销")
            time.sleep(5.5)
            os.system("shutdown /l")
        elif j in ["n", "N"]:
            deselect(3)
    elif i in ["sleep"]:
        j = input(colorama.Fore.GREEN + "↓------→确定将此电脑设定为睡眠状态吗(y/n)>>" + colorama.Fore.BLUE)
        while j in ["y", "Y", "n", "N"]:
            j = input(colorama.Fore.GREEN + "↓------→确定将此电脑设定为睡眠状态吗(y/n)>>" + colorama.Fore.BLUE)
        if j in ["y", "Y"]:
            print(colorama.Fore.RED + "↓------→5秒后睡眠此电脑")
            time.sleep(5.5)
            os.system("shutdown /h")
        elif j in ["n", "N"]:
            deselect(3)
    elif i in ["exit"]:
        deselect(2)
# ==================================================================================================
# U
def u():
    print("↓→uanxhzl114514")
def update():
    import package.update as upd_z
    upd_z.update(1)
def uncultivated():                      #附属于任何暂时不支持的命令
    print(colorama.Fore.YELLOW + "↓→前面的区域,以后再来探索吧？\n→→如果您的版本是最新的,请期待我们的更新,感谢您的支持")
# ==================================================================================================
# V
def v():
    print("↓→vaxmzip114514")
# ==================================================================================================
# W
def w():
    print("↓→wszjhlm114514")
# ==================================================================================================
# X
def x():
    print("↓→xhavoyq114514")
# ==================================================================================================
# Y
def y():
    print("↓→yyds")
# ==================================================================================================
# Z
def z():
    print("↓→zgxkanr114514")
# ==================================================================================================