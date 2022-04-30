import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

        

def main_apv():

    imt="110Y=="

    ak="Hamza-1"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()

    except IOError:

        os.system("clear")

        print(logo)

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        print ("  Approval To le lo ")

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        print ("           Ani Dya Tari Key A wa ....")

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        print ("")

        myid=uuid.uuid4().hex[:10].upper()

        print ("          YOUR KEY : "+ak+myid+imt)

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')

        kok.write(myid+imt)

        kok.close()

        print ("")

        print ("")

        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+923011517172?text=' + tks)

        

    r1=requests.get("https://github.com/NAYABPARI/MZR/blob/main/z.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        print ("   Approval To le lo")

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        print ("          Ani Dya Tari Key A wa")

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        print ("          YOUR KEY : "+ak+key1)

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        print ("     Copy Key And Sent Me WP Approvel Your Key ")

        print ("[$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/03305867095?text=' + tks)


logo="""\033[1;37m
                                                        ####     ####            
 ##   ##  ######            ##  ##     ##      #####   ##  ##   ##  ##   ##   ## 
 ##   ##  ##   ##           ##  ##     ##     ##   ##      ##       ##   ###  ## 
 ### ###  ##   ##            ####     ####    ##         ###      ###    ###  ## 
 ## # ##  ######              ##      ## #     #####       ##       ##   ## # ## 
 ## # ##  ## ##               ##     ######        ##      ##       ##   ## # ## 
 ##   ##  ##  ##              ##     ##   #   ##   ##  ##  ##   ##  ##   ##  ### 
 ##   ##  ##   ##             ##    ###   ##   #####    ####     ####    ##   ## 
                                                                                 
                                                                                 
 [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]
    Author   : MR YSEEN   MR SARDAR
    Facebook :https://www.facebook.com/nauman.anwar.357
    Connect  : 03305867095
Connet  : 03051201515
 [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]
 \033[1;32m Use (Airplane) Mod Every 10 Min For Get More Ok iDz \033[1;32m
 [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]"""                     

def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97m/sdcard/OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97m/sdcard/CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back Ahmad Menu ")

	    R()

		
def R():

			os.system("clear")

			print(logo)

			print("               \033[1;92m• Premium • \033[1;97m")

