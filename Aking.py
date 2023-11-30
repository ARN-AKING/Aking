import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\x1b[1;37m[☆] Checking Update....');time.sleep(0.5)
def Update():
    xoss('\033[1;31m[+] Commands On Update Please Wait For Update ');exit()
def Run():
        AKING = platform.architecture()[0]
        if AKING == '64bit':
            Update()
            xoss("\x1b[1;92m[☆] Congratulations : Your Device Support this Tools");time.sleep(1)
            xoss("\x1b[1;92m[☆] Your Device 64 BIT");time.sleep(1)
            xoss("\x1b[1;92m[☆] FOLLOW MY FACEBOOK ACCOUNT");time.sleep(1)
            os.system("xdg-open https://www.facebook.com/Rayees.Amir4201/");Update()
            import AKING64

        elif AKING == '32bit':
            Update()
            xoss("\x1b[1;92m[☆] Congratulations : Your Device Support this Tools");time.sleep(1)
            xoss("\x1b[1;92m[☆] Your Device 32 BIT");time.sleep(1)
            xoss("\x1b[1;92m[☆] FOLLOW MY FACEBOOK ACCOUNT");time.sleep(1)
            os.system("xdg-open https://www.facebook.com/Rayees.Amir4201/")
            import AKING32
            print(50*"-")
        else:
            exit('\033[1;31m[+] Connection & Network Error')
Run()
