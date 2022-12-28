import time,os
import docs.help as z_hp
def welcome():
    print("Welcome!")
    print("As you can see, this is a particularly simple console applet.")
    print("You can enter some commands after \">>\" or ask me some questions.")
    print("If you are not familiar with it, you can search \"2109511809\" on QQ to find me, or enter \"Help\" after \">>\" to get help documents.")
    print("If you want to exit, you can enter \"exit\" or \"quit\" or \"bye\" or \"pause\" after \">>\", or press the close button at y")
    input_z()
def input_z():
    input_zz = input('>>')
    while input_zz == '':
        input_zz = input('>>')
    judge_z(input_zz)
def judge_z(input_zz):
    if input_zz == "":
        input_z()
    elif input_zz == "quit" or input_zz == "exit" or input_zz == "bye" or input_zz == "pause" or input_zz == "退出":
        if input_zz == "bye":
            print("∟ See you!")
            time.sleep(0.5)
        elif input_zz == "pause":
            print("paused")
            os.system("pause")
        else:
            print("∟",input_zz, "okay")
            time.sleep(0.5)
    elif input_zz == "Help" or input_zz == "help":
        z_hp.z_help()
    elif input_zz == "a":
        print("∟ aassxsw114514")
        input_z()
    elif input_zz == "b":
        print("∟ bseuxqy114514")
        input_z()
    elif input_zz == "c":
        print("∟ chyewiq114514")
        input_z()
    elif input_zz == "d":
        print("∟ dqshsuid114514")
        input_z()
    else:
        print("∟ not supput")
        input_z()

