import time,os
def z_help():
    print("help")
    print("You can get help here.")
    print("If you want to view the help document, enter \"docs\" after \"help>>\".")
    z_help_input()
def z_help_input():
    hp_input = input("help>>")  
    while hp_input == "":
        hp_input = input("help>>")
    hp_jduge(hp_input)
def hp_jduge(hp_input):
    if hp_input == "docs" or hp_input == "help":
        def docs():
            f = open("docs\\help.txt",encoding='utf-8')
            x = f.read()
            print("∟     The following is the content of the help document.")
            print(x)
            print("∟     The above is the content of the help document.")
            f.close()
        docs()
        z_help_input()
    elif hp_input == "exit" or hp_input == "退出":
        exitcmd = r"cd . && python main.py"
        os.system(exitcmd)
    else:
        abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        if hp_input in abc:
            print("∟     These commands are for testing. You can understand them as placeholders.")
            print("∟     Actually, I haven't figured out what commands to write.")
            print("∟     lol")
        z_help_input()