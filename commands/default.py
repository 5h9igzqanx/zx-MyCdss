# 这是内置的命令定义文档
# 如果您不是专业人士，请不要修改这里的文件，这可能会伤害您的电脑！
# 展示时间
# ==========================================================================================================================
# ==========================================================================================================================
#导入
import time,os,sys,wget
# ========================
# 特殊符号
# =============================================================
# A
def a():
    print("→ aassxsw114514")
# =============================================================
# B
def b():
    print("→ bseuxqy114514")
# =============================================================
# C
def c():
    print("→ chyewiq114514")
# =============================================================
# D
def d():
    print("→ dqshsui114514")
# =============================================================
# E
def e():
    print("→ edysjsi114514")
def exit():
    print("→ 再见")
    time.sleep(1)
    sys.exit(0)
# =============================================================
# F
def f():
    print("→ fsialxq114514")
# =============================================================
# G
def g():
    print("→ gqeanxz114514")
# =============================================================
# H
def h():
    print("→ hexuaqi114514")
# =============================================================
# I
def i():
    print("→ i love u(bushi)")
# =============================================================
# J
def j():
    print("→ jntm,jnszstm(bushi)")
# =============================================================
# K
def k():
    print("→ 我妹K")
# =============================================================
# L
def l():
    print("→ lshznga114514")
# =============================================================
# M
def m():
    print("→ mshanxg114514")
# =============================================================
# N
def n():
    print("→ nxiwlaz114514")
def no_command(input_zz):
    print("→ 很抱歉，此命令 \"{0}\" 未出现在您的定义文档中，或者我们不支持此命令\n→ 您可以尝试重新输入此命令或在\"user_costom.py\"自定义此命令，或在\">>\"后输入\"help\"以获取帮助".format(input_zz))
# =============================================================
# O
def o():
    print("→ o point o")
    print("→ \"Whook whook\"")
    time.sleep(1)
    print("→ \"Ay look at that moving eye eyes\"")
    time.sleep(2.5)
    print("→ \"봤니 shoog shoog shoog\"")
    time.sleep(2.3)
    print("→ \"Hook 들어와 내게 좀 더\"")
    time.sleep(2.4)
    print("→ \"좋아 zoom zoom good\"")
# =============================================================
# P
def p():
    print("→ psabxgz114514")
def practice():
    print("→ 这条命令用于您练习\n→ 顾名思义，此命令可以帮助您熟悉此软件")
    print("→ *如果您想练习，请在下面输入\"present\"；如果这是您第一次使用它，请在下面输入\"learn\"")
    time.sleep(0.1)
    i = input(">practice>>")
    while i not in ["present","learn","exit"]:
        i = input(">practice>>")
    if i in ["present"]:
        uncultivated()
    elif i in ["learn"]:
        uncultivated()
    elif i in ["exit"]:
        pass
# =============================================================
# Q
def q():
    print("→ qixznug114514")
# =============================================================
# R
def r():
    print("→ riznxco114514")
# =============================================================
# S
def s():
    print("→ sxczhag114514")
# =============================================================
# T
def t():
    print("→ tsanzhx114514")
def test():
    print("→ 这是一个测试命令，用于测试这个软件是否可以正常使用")
    print("→ 试着在这里随便打些什么吧，例如输入\"114514\"就输出\"114514114514114514\"，输入exit以退出")
    while True:
        i = input(">test>>")
        if i == "exit":
            break
        else:
            print("→ " + i * 3)
def tool():
    print("→ 这里有一些工具，其中的一些可能会帮到您")
    print("→ 请选择类别...")
    print("→ *[system,user,...]")
    i = input(">tool>>")
    while i not in ["system","user"]:
        i = input(">tool>>")
    if i in["system"]:
        tool_system()
    elif i in ["user"]:
        pass# TODO 还没做好
def tool_system():                       #附属于 tool()
    print("→   这里是系统工具\n→   这里备了一些常用的系统命令，所以您不用再东跑西跑了")
    print("→   请选择您想执行的任务...")
    print("→   *[shutdown,open,...]")
    i = input(">tool>system>>")
    while i not in ["shutdown", "open","exit"]:
        i = input(">tool>system>>")
    if i in ["shutdown"]:
        tool_system_shutdown()
    elif i in ["open"]:
        print("→     选择您想打开的系统管理程序")
        print("→     *[taskmgr,regedit]")
        j = input(">tool>system>open>>")
        while j not in ["taskmgr","regedit"]:
            j = input(">tool>system>open>>")
        if j in ["taskmgr", "任务管理器"]:
            os.system("taskmgr.exe")
        elif j in ["regedit", "注册表编辑器"]:
            os.system("regedit.exe")
        print("→     执行成功")
    elif i in ["exit"]:
        pass
def tool_system_shutdown():              #附属于 tool_system()
    print("→   这条命令用于关机等命令的执行，但注意\"…等命令…\"，额……\n→   所以您是想关机还是想进行其他类似的命令(注销，睡眠)")
    print("")
    print("→   请选择你想执行的任务...")
    print("→   *[shutdown,restart,logoff,sleep]")
    i = input(">tool>system>shutdown>>")
    while i not in ["shutdown", "restart", "logoff", "sleep"]:
        i = input(">tool>system>shutdown>>")
    if i in ["shutdown"]:
        j = input("→     确定关机吗(y/n)>>")
        while j in ["y", "Y", "n", "N"]:
            j = input("→     确定关机吗(y/n)>>")
        if j in ["y", "Y"]:
            print("→     5秒后关机")
            time.sleep(5.5)
            os.system("shutdown /s")
        elif j in ["n", "N"]:
            pass
    elif i in ["restart"]:
        j = input("→     确定重启吗(y/n)>>")
        while j in ["y", "Y", "n", "N"]:
            j = input("→     确定重启吗(y/n)>>")
        if j in ["y", "Y"]:
            print("→     5秒后重启")
            time.sleep(5.5)
            os.system("shutdown /r")
        elif j in ["n", "N"]:
            pass
    elif i in ["logoff"]:
        j = input("→     确定注销吗(y/n)>>")
        while j in ["y", "Y", "n", "N"]:
            j = input("→     确定注销吗(y/n)>>")
        if j in ["y", "Y"]:
            print("→     5秒后注销")
            time.sleep(5.5)
            os.system("shutdown /l")
        elif j in ["n", "N"]:
            pass
    elif i in ["sleep"]:
        j = input("→     确定睡眠此电脑吗(y/n)>>")
        while j in ["y", "Y", "n", "N"]:
            j = input("→     确定睡眠此电脑吗(y/n)>>")
        if j in ["y", "Y"]:
            print("→     5秒后睡眠此电脑")
            time.sleep(5.5)
            os.system("shutdown /h")
        elif j in ["n", "N"]:
            pass
    elif i in ["exit"]:
        pass
# =============================================================
# U
def u():
    print("→ uanxhzl114514")
def update():
    import package.update as upd_z
    upd_z.update(1)
def uncultivated():                      #附属于任何暂时不支持的命令
    print("→ 我们似乎还没在这个版本中做好这个功能，您还没有更新吗？\n→ 如果您的版本是最新的，请期待我们的更新，感谢您的支持")
# =============================================================
# V
def v():
    print("→ vaxmzip114514")
# =============================================================
# W
def w():
    print("→ wszjhlm114514")
# =============================================================
# X
def x():
    print("→ xhavoyq114514")
# =============================================================
# Y
def y():
    print("→ yyds")
# =============================================================
# Z
def z():
    print("→ zgxkanr114514")
# =============================================================