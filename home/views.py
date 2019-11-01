from django.shortcuts import render
import requests,re,json
from aiqu import views as qiqu_view
# Create your views here.
def home(request):
   d1=0
   d2=0
   try:
      d1 ,d2 = qiqu_view.login()
   except Exception as e:
      d1 =e
   return  render(request,"home.html",{"register":d2,"pay":d1})


