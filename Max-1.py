import os, platform, time
#os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://facebook.com/groups/927380541994919/")
time.sleep(5)
os.system("xdg-open https://www.facebook.com/profile.php?id=100075043421846")
try:
    import requests
except(ImportError):
    os.system("pip install requests")

try:
    import bs4
except(ImportError):
    os.system("pip install bs4")

rana=platform.architecture()[0]
try:
    if rana=="32bit":
        exit(' 32 bit not executeble ')
        __import__("tok32").aahil_main_menu()
    elif rana=="64bit":
        #exit(' 32 bit not executeble ')
        __import__("pro").mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if rana == "32bit":
        exit(' 32 bit not executeble ')
        import tok32
        tok32.aahil_main_menu
    elif rana == "64bit":
        import pro
        pro.mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
