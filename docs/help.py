import time,os,webbrowser,colorama
def z_help():
    print(colorama.Fore.RED + "↓→您可以在这里得到帮助")
    print(colorama.Fore.YELLOW + "↓→如果要查看帮助文档,请在\"help>>\"之后输入\"docs\"")
    z_help_input()
def z_help_input():
    hp_input = input(colorama.Fore.GREEN + ">>help>" + colorama.Fore.BLUE)
    while hp_input == "":
        hp_input = input(colorama.Fore.GREEN + ">>help>" + colorama.Fore.BLUE)
    hp_jduge(hp_input)
def hp_jduge(hp_input):
    if hp_input in["docs","help","文档"]:
        def docs():
            f = open("docs\\help.txt",encoding='utf-8')
            x = f.read()
            print(colorama.Fore.RED + "↓--→以下是帮助文档的内容\n")
            print(x)
            print(colorama.Fore.RED + "\n↓--→以上是帮助文档的内容")
            f.close()
        docs()
        #z_help_input()
    elif hp_input in ["exit","bye","quit","退出"]:
        print(colorama.Fore.RED + "↓→您退出了\"帮助\",请继续使用")
        time.sleep(1)
        return
    elif hp_input in ["about","关于"]:
        print(colorama.Fore.RED + "↓--→如果你想参阅我们的更多内容,欢迎前往\"https://5h9igzqanx.github.io/TRDWBST\"！")
        webbrowser.open("https://5h9igzqanx.github.io/TRDWBST",new=0,autoraise=True)
    elif hp_input in ["feedback","反馈"]:
        print(colorama.Fore.RED + "↓--→如果你想反馈关于\"zx-MyCdss\"的BUG或者更新建议,欢迎前往\"https://github.com/5h9igzqanx/zx-MyCdss/issues\"！")
        webbrowser.open("https://github.com/5h9igzqanx/zx-MyCdss/issues",new=0,autoraise=True)
        webbrowser.open("https://5h9igzqanx.github.io/TRDWBST-pages/pages/project/0/feedback.htm",new=0,autoraise=True)
    #elif hp_input in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
    #    print(colorama.Fore.RED + "↓--→这些命令用于测试您可以把它们理解为占位符")
    #    print(colorama.Fore.RED + "↓--→事实上,我还没弄清楚该写什么命令")
    #    print(colorama.Fore.RED + "↓--→lol")
    else:
        print(colorama.Fore.RED + "↓--→额,其实我要说的都在帮助文档里了哈哈……")
        print(colorama.Fore.RED + "↓--→所以这个就没什么用了哈哈哈哈……哈哈……")
    print(colorama.Fore.GREEN + "↓")
    z_help_input()