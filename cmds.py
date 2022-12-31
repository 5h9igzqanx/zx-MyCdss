# Here is the command definition document.
# Here you can manage what commands to enter before using them.
# System defined commands and user-defined commands can be defined here.
# If you have customized a command, please add it here. However, you cannot modify (not create) the code in any case!!!


import time,os
import commands.default as z_sys
import commands.user_custom as z_user
import docs.help as z_sys_hp
def welcome():
    print("Welcome!")
    print("As you can see, this is a particularly simple console applet.")
    print("You can enter some commands after \">>\" or ask me some questions.")
    print("If you are not familiar with it, you can search \"2109511809\" on QQ to find me, or enter \"Help\" after \">>\" to get help documents.")
    print("If you want to exit, you can enter \"exit\" after \">>\", or press the close button at y")
    input_z()
def input_z():
    input_zz = input('>>')
    while input_zz == '':
        input_zz = input('>>')
    judge_z(input_zz)
def judge_z(input_zz):
    if input_zz == "":
        input_z()
    elif input_zz == "exit" or input_zz == "退出":
        z_sys.exit(input_zz=input_zz)
    elif input_zz == "Help" or input_zz == "help":
        z_sys_hp.z_help()
    elif input_zz == "a":
        z_sys.a()
        input_z()
    elif input_zz == "b":
        z_sys.b()
        input_z()
    elif input_zz == "c":
        z_sys.c()
        input_z()
    elif input_zz == "d":
        z_sys.d()
        input_z()
    elif input_zz == "e":
        z_sys.e()
        input_z()
    else:
        z_sys.no_command()
        input_z()