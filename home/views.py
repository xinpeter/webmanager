from django.shortcuts import render
import requests, re, json
from aiqu import views as qiqu_view
from BTyeyou import views as BTyeyou_view
from gmyeyou import views as gmyeyou_view

# Create your views here.
def home(request):
    # 爱趣
    d1 = 0
    d2 = 0
    # BT页游
    count = 0
    #gm页游
    gmyeyou_register = 0
    gmyeyou_pay = 0
    try:
        d1, d2 = qiqu_view.login()

    except Exception as e:
        d1 = e
    try:
        count = BTyeyou_view.login()
    except Exception as e:
        count = e
    try:
        gmyeyou_register,gmyeyou_pay = gmyeyou_view.login()
    except Exception as e:
        gmyeou_pay = e
    return render(request, "home.html", {"aiqu_register": d2, "aiqu_pay": d1, "BT_pay": count,"gmyeyou_register":gmyeyou_register,"gmyeyou_pay":gmyeyou_pay})
