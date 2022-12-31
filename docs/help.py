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
    print("The following is the content of the help document.")
    if hp_input == "docs" or hp_input == "help":
        def docs():
            f = open("docs\\help.txt",encoding='utf-8')
            x = f.read()
            print(x)
            f.close()
        docs()