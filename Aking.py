import os, sys, platform,time
try:
    import requests
except:
    os.system('pip install requests')
os.system('am start https://t.me/DIVEL_TEAM_HACK');time.sleep(5)

bit = platform.architecture()[0]
if bit == '64bit':
    import Aking64
elif bit == '32bit':
    import Aking32
