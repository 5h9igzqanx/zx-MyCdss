# 这是内置的命令定义文档
# 如果您不是专业人士，请不要修改这里的文件，这可能会伤害您的电脑！
# 展示时间


#导入
import time,os,sys,wget
# ========================
# 特殊符号

# =============================================================
# A
def a():
    print("∟ aassxsw114514")
# =============================================================
# B
def b():
    print("∟ bseuxqy114514")
# =============================================================
# C
def c():
    print("∟ chyewiq114514")
# =============================================================
# D
def d():
    print("∟ dqshsui114514")
# =============================================================
# E
def e():
    print("∟ edysjsi114514")
def exit():
    print("∟ 再见")
    sys.exit(0)
# =============================================================
# F
def f():
    print("∟ fsialxq114514")
# =============================================================
# G
def g():
    print("∟ gqeanxz114514")
# =============================================================
# H
def h():
    print("∟ hexuaqi114514")
# =============================================================
# I
def i():
    print("∟ i love u(bushi)")
# =============================================================
# J
def j():
    print("∟ jntm,jnszstm(bushi)")
# =============================================================
# K
def k():
    print("∟ kshxgam114514")
# =============================================================
# L
def l():
    print("∟ lshznga114514")
# =============================================================
# M
def m():
    print("∟ mshanxg114514")
# =============================================================
# N
def n():
    print("∟ nxiwlaz114514")
def no_command(input_zz):
    print("∟ 很抱歉，此命令 \"" + input_zz + "\" 未出现在您的定义文档中，或者我们不支持此命令")
    print("∟ 您可以尝试重新输入此命令或自定义此命令，或在\">>\"后输入\"help\"以获取帮助")
# =============================================================
# O
def o():
    print("∟ o point o")
    print("∟ \"Whook whook\"")
    time.sleep(1)
    print("∟ \"Ay look at that moving eye eyes\"")
    time.sleep(2.5)
    print("∟ \"봤니 shoog shoog shoog\"")
    time.sleep(2.3)
    print("∟ \"Hook 들어와 내게 좀 더\"")
    time.sleep(2.4)
    print("∟ \"좋아 zoom zoom good\"")
# =============================================================
# P
def p():
    print("∟ psabxgz114514")
def practice():
    print("∟ 这条命令用于您练习")
    print("∟ 顾名思义，此命令可以帮助您熟悉此软件")
    print("∟ 如果您想练习，请在下面输入\"present\"；如果这是您第一次使用它，请在下面输入\"learn\"")
    time.sleep(0.1)
    i = input(">practice>>")
    while i not in ["present","learn"]:
        i = input(">practice>>")
    if i == "present":
        uncultivated()
    elif i == "learn":
        uncultivated()
# =============================================================
# Q
def q():
    print("∟ qixznug114514")
# =============================================================
# R
def r():
    print("∟ riznxco114514")
# =============================================================
# S
def s():
    print("∟ sxczhag114514")
def shutdown():  #附属于system()
    print("∟   这条命令用于关机等命令的执行，但注意\"…等命令…\"，额……")
    print("∟   所以您是想关机还是想进行其他类似的命令(注销，睡眠)")
    print("ps. 关机shutdown,重启restart,注销logoff,睡眠sleep")
    i = input(">system>shutdown>>")
    while i in ["shutdown","restart","logoff","sleep"]:
        i = input(">system>shutdown>>")
    if i == "shutdown":
        j = input("∟ 确定关机吗(y/n)>>")
        while j in ["y","Y","n","N"]:
            j = input("∟ 确定关机吗(y/n)>>")
        if j in ["y","Y"]:
            print("∟ 5秒后关机")
            time.sleep(5.5)
            os.system("shutdown /s")
        elif j in["n","N"]:
            pass
    elif i == "restart":
        j = input("∟ 确定重启吗(y/n)>>")
        while j in ["y","Y","n","N"]:
            j = input("∟ 确定重启吗(y/n)>>")
        if j in ["y","Y"]:
            print("∟ 5秒后重启")
            time.sleep(5.5)
            os.system("shutdown /r")
        elif j in["n","N"]:
            pass
    elif i == "logoff":
        j = input("∟ 确定注销吗(y/n)>>")
        while j in ["y","Y","n","N"]:
            j = input("∟ 确定注销吗(y/n)>>")
        if j in ["y","Y"]:
            print("∟ 5秒后注销")
            time.sleep(5.5)
            os.system("shutdown /l")
        elif j in["n","N"]:
            pass
    elif i == "sleep":
        j = input("∟ 确定睡眠此电脑吗(y/n)>>")
        while j in ["y","Y","n","N"]:
            j = input("∟ 确定睡眠此电脑吗(y/n)>>")
        if j in ["y","Y"]:
            print("∟ 5秒后睡眠此电脑")
            time.sleep(5.5)
            os.system("shutdown /h")
        elif j in["n","N"]:
            pass 
def system():
    print("∟ 这里是系统工具")
    print("∟ 这里备了一些常用的系统命令，所以您不用再东跑西跑了")
    print("∟ 选择您想进行的任务")
    i = input(">system>>")
    while i not in ["shutdown","open"]:
        i = input(">system>>")
    if i == "shutdown":
        shutdown()
    elif i == "open":
        print("∟   选择您想打开的系统管理程序")
        j = input(">system>open>>")
        while j in []:
            j = input(">system>open>>")
        if j == "taskmgr":
            os.system("taskmgr.exe")
        elif j == "":
            pass
        print("∟   执行成功")
# =============================================================
# T
def t():
    print("∟ tsanzhx114514")
def test():
    print("∟ 这是一个测试命令，用于测试这个软件是否可以正常使用")
    print("∟ 试着在这里随便打些什么吧，例如输入\"114514\"就输出\"114514114514114514\"，输入exit以退出")
    while True:
        i = input(">test>>")
        if i == "exit":
            break
        else:
            print("∟ " + i * 3)
# =============================================================
# U
def u():
    print("∟ uanxhzl114514")
def update():
    import package.update as upd_z
    upd_z.update(1)
def uncultivated():  # This isn't a command!
    print("∟ 我们似乎还没有这个功能，您还没有更新吗？")
    print("∟ 如果您有最新版本，请期待我们的更新，感谢您的支持。")
# =============================================================
# V
def v():
    print("∟ vaxmzip114514")
# =============================================================
# W
def w():
    print("∟ wszjhlm114514")
# =============================================================
# X
def x():
    print("∟ xhavoyq114514")
# =============================================================
# Y
def y():
    print("∟ yyds")
# =============================================================
# Z
def z():
    print("∟ zgxkanr114514")
# =============================================================