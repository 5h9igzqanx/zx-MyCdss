# Here is the command definition document.
# Here you can manage what commands to enter before using them.
# System defined commands and user-defined commands can be defined here.
# If you have customized a command, please add it here. However, you cannot modify (not create) the code in any case!!!


import time,os,sys
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
        pass
    elif input_zz == "exit" or input_zz == "bye" or input_zz == "退出":
        z_sys.exit(input_zz=input_zz)
    elif input_zz == "Help" or input_zz == "help":
        z_sys_hp.z_help()
    elif input_zz == "A" or input_zz == "a":
        z_sys.a()
    elif input_zz == "B" or input_zz == "b":
        z_sys.b()
    elif input_zz == "C" or input_zz == "c":
        z_sys.c()
    elif input_zz == "D" or input_zz == "d":
        z_sys.d()
    elif input_zz == "E" or input_zz == "e":
        z_sys.e()
    elif input_zz == "F" or input_zz == "f":
        z_sys.f()
    elif input_zz == "G" or input_zz == "g":
        z_sys.g()
    elif input_zz == "H" or input_zz == "h":
        z_sys.h()
    elif input_zz == "I" or input_zz == "i":
        z_sys.i()
    elif input_zz == "J" or input_zz == "j":
        z_sys.j()
    elif input_zz == "K" or input_zz == "k":
        z_sys.k()
    elif input_zz == "L" or input_zz == "l":
        z_sys.l()
    elif input_zz == "M" or input_zz == "m":
        z_sys.m()
    elif input_zz == "N" or input_zz == "n":
        z_sys.n()
    elif input_zz == "O" or input_zz == "o":
        z_sys.o()
    elif input_zz == "P" or input_zz == "p":
        z_sys.p()
    elif input_zz == "Q" or input_zz == "q":
        z_sys.q()
    elif input_zz == "R" or input_zz == "r":
        z_sys.r()
    elif input_zz == "S" or input_zz == "s":
        z_sys.s()
    elif input_zz == "T" or input_zz == "t":
        z_sys.t()
    elif input_zz == "U" or input_zz == "u":
        z_sys.u()
    elif input_zz == "V" or input_zz == "v":
        z_sys.v()
    elif input_zz == "W" or input_zz == "w":
        z_sys.w()
    elif input_zz == "X" or input_zz == "x":
        z_sys.x()
    elif input_zz == "Y" or input_zz == "y":
        z_sys.y()
    elif input_zz == "Z" or input_zz == "z":
        z_sys.z()
    else:
        z_sys.no_command()
    input_z()