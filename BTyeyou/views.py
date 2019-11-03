from django.shortcuts import render
import requests,time
# Create your views here.

def login():
   data={"name":"xinghai",
         "password":"xinghai12345"}
   session = requests.session()
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
   r = session.post("http://dl.00pk.cn/api/auth/login",data=data,headers=headers).json()
   # print(r)
   token = r.get("token")
   t = time.strftime("%Y-%m-%d", time.localtime())
   headers_refer = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                   "Referer":"http://dl.00pk.cn/dladmin/page/recharge/list.html","dladmin_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kbC4wMHBrLmNuXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNTcyNzgyMTY4LCJleHAiOjE1NzI3ODU3NjgsIm5iZiI6MTU3Mjc4MjE2OCwianRpIjoiRFE0bExBMDJLNWlEQ2lKRyIsInN1YiI6MTQxLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.DiAeyas5GHA59betEa1SY5zEYG3FYHdFBYzQ34cpTys",
                    "Authorization":"Bearer {}".format(token)}
   # r = session.get("http://dl.00pk.cn/api/daili/paylist?rows=10&page=1&sdate=2019-11-01+00%3A00%3A00&edate=2019-11-02+23%3A59%3A59&status=-1",headers=headers_refer).json()
   r = session.get("http://dl.00pk.cn/api/daili/paylist?rows=10&page=1&sdate="+t+"+00%3A00%3A00&edate="+t+"+23%3A59%3A59&status=-1",headers=headers_refer).json()
   #今日充值
   data = r.get("data")
   count = 0

   for i in data:
       if i.get("status") == 2:
           count = count + float(i.get("money"))
   return count


   

if __name__ == '__main__':
       login()

