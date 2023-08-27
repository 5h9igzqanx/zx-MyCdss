import time,os,webbrowser
import cmds as z_exitcmd
def z_help():
    print("→ 您可以在这里得到帮助。")
    print("→ 如果要查看帮助文档，请在\"help>>\"之后输入\"docs\"。")
    z_help_input()
def z_help_input():
    hp_input = input(">>help>")  
    while hp_input == "":
        hp_input = input(">>help>")
    hp_jduge(hp_input)
def hp_jduge(hp_input):
    if hp_input in["docs","help"]:
        def docs():
            f = open("docs\\help.txt",encoding='utf-8')
            x = f.read()
            print("→   以下是帮助文档的内容。")
            print()
            print(x)
            print()
            print("→   以上是帮助文档的内容。")
            f.close()
        docs()
        z_help_input()
    elif hp_input in ["exit","bye","quit","退出"]:
        z_exitcmd.input_z()
    elif hp_input in ["about","关于"]:
        print("→   如果你想参阅我们的更多内容，欢迎前往\"https://5h9igzqanx.github.io/TRDWBST\"！")
        webbrowser.open("https://5h9igzqanx.github.io/TRDWBST",new=0,autoraise=True)
    elif hp_input in ["feedback","反馈"]:
        print("→   如果你想反馈关于\"zx-MyCdss\"的BUG或者更新建议，欢迎前往\"https://github.com/5h9igzqanx/zx-MyCdss/discussions\"或\"https://5h9igzqanx.github.io/TRDWBST-pages/pages/project/0/feedback.htm\"！")
        webbrowser.open("https://github.com/5h9igzqanx/zx-MyCdss/discussions",new=0,autoraise=True)
        webbrowser.open("https://5h9igzqanx.github.io/TRDWBST-pages/pages/project/0/feedback.htm",new=0,autoraise=True)
    #elif hp_input in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
    #    print("→   这些命令用于测试。您可以把它们理解为占位符")
    #    print("→   事实上，我还没弄清楚该写什么命令")
    #    print("→   lol")
    else:
        print("→   额，其实我要说的都在帮助文档里了哈哈……")
        print("→   所以这个就没什么用了哈哈哈哈……哈哈……")
    z_help_input()