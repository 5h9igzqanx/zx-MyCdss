"""
这是内置的命令定义文档
如果您不是专业人士,请不要修改这里的文件,这可能会伤害您的电脑！
展示时间
"""
# ==================================================================================================================================================
# ==================================================================================================================================================
# 导入
import colorama,contextlib,datetime,os,random,sys,threading,time,tkinter,webbrowser,wget
# ========================
# 初始化
# ========================
# 特殊符号
# ==================================================================================================
# A
def a():
    output(0,0,"aassxsw114514")
    output(1,0,"aassxsw114514")
    output(0,1,"aassxsw114514")
def ask(text:str="",type:int=0):
    i = input(colorama.Fore.GREEN + text + ">>" + colorama.Fore.BLUE)
    if type == 0:
        while not(i):
            i = input(colorama.Fore.GREEN + text + ">>" + colorama.Fore.BLUE)
        else:
            return i
    elif type == 1:
        return i
    return i
# ==================================================================================================
# B
def b():
    print("↓→bseuxqy114514")
def bell():
    output(0,0,"忙里偷闲,苦中作乐")
    while True:
        print("\a")
        time.sleep(1)
        i = ask("bell",0)
        if i in ["exit"]:
            deselect()
            break
        else:
            pass
# ==================================================================================================
# C
def c():
    print("↓→chyewiq114514")
def choose(level:int=0,text:str=""):
    if not(text):
        errors("Va","byd你整个选择不加问题是吧")
        return False
    i = colorama.Fore.GREEN + "↓" + int(level) * "--" + "→" + text + "(y/n)>>" + colorama.Fore.BLUE
    choose = input(i)
    while not(choose) or choose not in ["y","Y","n","N"]:
        choose = input(i)
    if choose in ["y","Y"]:
        return True
    elif choose in ["n","N"]:
        return False
    else:
        return False
# ==================================================================================================
# D
def d():
    print("↓→dqshsui114514")
def deselect(level:int=0):                      #附属于任何带有"exit"的elif分支
    output(0,level,"选择已取消")
    return
# ==================================================================================================
# E
def e():
    print("↓→edysjsi114514")
def errors(error_value:str="Va",describe:str="情报有诈"):
    describe = "\n" + describe + "\n如果您是用户,请上报作者"
    if error_value in ["Va"]:
        raise ValueError(describe)
    elif error_value in["Us"]:
        raise UserWarning(describe)
def exit():                                     #系统退出
    output(0,0,"再见")
    time.sleep(1)
    os._exit(0)
# ==================================================================================================
# F
def f():
    print("↓→fsialxq114514")
def fIle():
    output(0,0,"这是一个文件操作命令")
    output(0,0,"你可以在这里对你的文件进行一些操作")
    directory = ask("↓→请选择一个目录",1)
    while (not(os.path.exists(directory))) or directory in ["exit"]:
        if directory in ["exit"]:
            deselect(0)
            return
        directory = ask("↓→目录无效,请重新选择",1)
    output(1,0,"请选择你想执行的任务...")
    output(1,0,"[...]")
    i = ask(">file",0)
    if i in["114514"]:
        uncultivated()
    elif i in ["delete"]:
        fIle_delete(directory = directory)
    elif i in ["exit"]:
        deselect(0)
def fIle_delete(directory):                     #附属于 fIle()
    output(0,1,"这条命令可以删除你选择的文件")
    file = ask("↓--→请选择一个文件",1)
    while False or (file in["exit"]):#没找到办法
        file = ask("↓--→文件不存在，请重新选择",1)
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
def noCommand(input_zz:str):                   #不附属于任何命令
    print(colorama.Fore.YELLOW + "↓→很抱歉,此命令 \"{0}\" 未出现在您的定义文档中,或者我们不支持此命令\n→→您可以尝试重新输入此命令或在\"user_custom.py\"自定义此命令,或在\">>\"后输入\"help\"以获取帮助".format(input_zz))
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
def output(type:int=0,level:int=0,text:str=""):#附属于 print()
    #colorama.init(autoreset=False)
    def describe(level=level,text=text):
        print(colorama.Fore.RED + "↓" + level * "--" + "→" + text)
    def prompt(level=level,text=text):
        print(colorama.Fore.YELLOW + "↓" + level * "--" + "" + text)
    if not(text):
        errors("Va","byd你整个空的输出是吧,你还不胜直接\"print()\"呢")
    if type == 0:
        describe()
    elif type == 1:
        prompt()
    else:
        errors("Va","\"Type\"参数仅支持传入0到1以内的数值")
    #colorama.init(autoreset=True)
# ==================================================================================================
# P
def p():
    print("↓→psabxgz114514")
def practice():
    output(0,0,"这条命令用于您练习")
    output(0,0,"顾名思义,此命令可以帮助您熟悉此软件")
    output(1,0,"如果您想练习,请在下面输入\"present\"；如果这是您第一次使用它,请在下面输入\"learn\"")
    time.sleep(0.1)
    i = ask(">practice",0)
    while i not in ["present","learn","exit"]:
        i = ask(">practice",0)
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
def rickroll():                                 #附属于任何彩蛋
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
    output(0,0,"这是一个测试命令,用于测试这个软件是否可以正常使用")
    output(1,0,"试着在这里随便打些什么吧,例如输入\"114514\"就输出\"114514114514114514\",输入exit以退出")
    while True:
        i = ask(">test",0)
        if i == "exit":
            break
        else:
            j = i * 3
            output(0,0,str(j))
def tool():
    output(0,0,"这里有一些工具,其中的一些可能会帮到您")
    output(1,0,"请选择类别...")
    output(1,0,"[system,user,...]")
    i = ask(">tool",0)
    while i not in ["system","user","exit"]:
        i = ask(">tool", 0)
    if i in["system"]:
        tool_system()
    elif i in ["user"]:
        uncultivated()# TODO 还没做好
    elif i in ["exit"]:
        deselect(0)
def tool_system():                              #附属于 tool()
    output(0,1,"这里是系统工具")
    output(0,1,"这里备了一些常用的系统命令,所以您不用再东跑西跑了")
    output(1,1,"请选择您想执行的任务...")
    output(1,1,"[shutdown,open,...]")
    i = ask(">tool>system",1)
    while i not in ["shutdown","open","exit"]:
        i = ask(">tool>system", 1)
    if i in ["shutdown"]:
        tool_system_shutdown()
    elif i in ["open"]:
        tool_system_open()
    elif i in ["exit"]:
        deselect(1)
def tool_system_open():                         #附属于 tool_system()
    output(0,2,"这里可以打开一些系统管理程序,或许在计算机被勒索时可以用?")
    output(1,2,"选择您想打开的系统管理程序...")
    output(1,2,"[taskmgr,regedit,...]")
    i = ask(">tool>system>open",0)
    while i not in ["taskmgr","regedit","exit"]:
        i = ask(">tool>system>open",0)
    if i in ["taskmgr"]:
        output(0,2,"执行成功")
        os.system("taskmgr.exe")
    elif i in ["regedit"]:
        output(0,2,"执行成功")
        os.system("regedit.exe")
    elif i in ["exit"]:
        deselect(2)
def tool_system_shutdown():                     #附属于 tool_system()
    output(0,2,"这条命令用于关机等命令的执行,但注意\"…等命令…\",额...")
    output(0,2,"所以您是想关机还是想进行其他类似的命令(注销,睡眠)")
    output(1,2,"请选择你想执行的任务...")
    output(1,2,"[shutdown,restart,logoff,sleep]")
    i = ask(">tool>system>shutdown",0)
    while i not in ["shutdown","restart","logoff","sleep","exit"]:
        i = ask(">tool>system>shutdown",0)
    if i in ["shutdown"]:
        j = choose(3,"确定关机吗")
        if j == True:
            output(0,3,"5秒后关机")
            time.sleep(5.5)
            os.system("shutdown /s")
        elif j == False:
            deselect(3)
    elif i in ["restart"]:
        j = choose(3,"确定重启吗")
        if j == True:
            output(0,3,"5秒后重启")
            time.sleep(5.5)
            os.system("shutdown /r")
        elif j == False:
            deselect(3)
    elif i in ["logoff"]:
        j = choose(3,"确定注销吗")
        if j == True:
            output(0,3,"5秒后注销")
            time.sleep(5.5)
            os.system("shutdown /l")
        elif j == False:
            deselect(3)
    elif i in ["sleep"]:
        j = choose(3,"确定将此电脑设定为睡眠状态吗")
        if j == True:
            output(0,3,"5秒后此电脑将被设定为睡眠状态")
            time.sleep(5.5)
            os.system("shutdown /h")
        elif j == False:
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
def uncultivated():                             #附属于任何暂时不支持的命令
    output(0,0,"前面的区域,以后再来探索吧?")
    output(0,0,"如果您的版本是最新的,请期待我们的更新,感谢您的支持")
# ==================================================================================================
# V
def v():
    print("↓→vaxmzip114514")
# ==================================================================================================
# W
def w():
    print("↓→wszjhlm114514")
def widget():
    output(0,0,"这条命令能够召唤一些窗口小组件,让您能在一个窗口内实现一组事情")
    output(0,0,"您可以点击窗口右上角的\"X\"来退出")
    output(1,0,"请选择你想打开的小组件")
    T_widget_clock=threading.Thread(target=widget_clock)
    T_widget_random=threading.Thread(target=widget_random)
    output(1,0,"[clock,random,...]")
    i = ask(">widget",0)
    while i not in ["clock","random","exit"]:
        i = ask(">widget", 0)
    if i in["clock"]:
        T_widget_clock.start()
    elif i in["random"]:
        T_widget_random.start()
    elif i in["exit"]:
        deselect(0)
    output(0,0,"小组件已被召唤,点击窗口右上角的\"X\"来退出")
    output(0,0,"您可以继续使用")
def widget_clock():
    screen = tkinter.Tk()
    screen.title("小组件窗口")
    #screen.attributes("-alpha",0.7)
    screen.attributes("-topmost",True)
    label = tkinter.Label(screen,text="11:45:14",font=('Arial',108),fg="#75aac8",bg="#cadeea")
    label.pack(fill="both",expand=True)
    var = tkinter.IntVar()
    def updateGUI():
        var.set(var.get()+1)
        time_raw = time.localtime(time.time()) 
        time_processed =time.strftime("%H:%M:%S",time_raw)
        label.config(text=str(time_processed))
        screen.after(50,updateGUI)
    def quit():
        for after_id in screen.tk.eval('after info').split():
            screen.after_cancel(after_id)
        screen.destroy()
    updateGUI()
    screen.protocol('WM_DELETE_WINDOW',quit)
    screen.mainloop()
def widget_random():
    screen = tkinter.Tk()
    screen.title("小组件窗口")
    #screen.attributes("-alpha",0.7)
    screen.attributes("-topmost",True)
    label = tkinter.Label(screen,text="9999999999999999999",font=('Arial',54),fg="#75aac8",bg="#cadeea")
    label.pack(fill="both",expand=True)
    var = tkinter.IntVar()
    def updateGUI():
        var.set(var.get()+1)
        ran = random.randint(1000000000000000000,9999999999999999999)
        label.config(text=str(ran))
        screen.after(5,updateGUI)
    def quit():
        for after_id in screen.tk.eval('after info').split():
            screen.after_cancel(after_id)
        screen.destroy()
    updateGUI()
    screen.protocol('WM_DELETE_WINDOW',quit)
    screen.mainloop()
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