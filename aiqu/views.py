import requests
from django.shortcuts import render

def login():
   data={"username":"15210574043",
         "password":"qq148334969"}
   session = requests.session()
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
   session.post("http://qudao.5535.cn/public/dologin.html",data=data,headers=headers)
   r = session.get("http://qudao.5535.cn/index/ajaxagent.html",headers=headers).json()
   #今日充值
   d1 = r.get("c")
   #今日注册
   d2 = r.get("e")
   return d1,d2

if __name__ == '__main__':
       login()

# Create your views here.
