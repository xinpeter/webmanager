from django.shortcuts import render
import requests,time
# Create your views here.

def login():
   data={"name":"xinghai",
         "password":"xinghai12345"}
   session = requests.session()
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
   session.post("http://dl.00pk.cn/api/auth/login",data=data,headers=headers)
   t = time.strftime("%Y-%m-%d", time.localtime())
   r = session.get("http://dl.00pk.cn/api/daili/paylist?rows=10&page=1&sdate="+t+"+00%3A00%3A00&edate="+t+"+23%3A59%3A59&status=-1",headers=headers).json()
   #今日充值
   data = r.get("data")

   

if __name__ == '__main__':
       # login()
       #今日
