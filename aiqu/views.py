import requests, django, os, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webmanager.settings")
from django.shortcuts import render
from django.http import HttpResponse
from aiqu.models import Test

django.setup()


def login():
    data = {"username": "15210574043",
            "password": "qq148334969"}
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    session.post("http://qudao.5535.cn/public/dologin.html", data=data, headers=headers)
    r = session.get("http://qudao.5535.cn/index/ajaxagent.html", headers=headers).json()
    t = time.strftime("%Y-%m-%d", time.localtime())

    # 今日充值
    register_number = r.get("c")
    # 今日注册
    pay = r.get("e")
    if len(Test.objects.filter(date=t)) == 0:
        save(pay, register_number, t)
        print("1")
    else:
        update(pay, register_number, t)

    register_number,pay = view(t)
    return pay, register_number


def save(register_number, pay, t):
    obj = Test(name=register_number, password=pay, date=t)
    obj.save()
    return HttpResponse("ok")


def update(register_number, pay, t):
    obj = Test.objects.get(date=t)
    obj.name = register_number
    obj.password = pay
    obj.save()

def view(t):
    obj = Test.objects.get(date=t)
    register_number = obj.name
    pay = obj.password
    return register_number,pay

if __name__ == '__main__':
    # login()
    #  save()
    pass
