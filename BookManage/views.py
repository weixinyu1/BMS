# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, response
from django.shortcuts import render

# Create your views here.
from BookManage.models import User


def index_view(request):
    if request.method=='GET':
        return HttpResponseRedirect('/login/')
    uname=request.POST.get('username','')
    upwd=request.POST.get('password','')
    # print uname,upwd
    count = User.objects.filter(uname=uname, upwd=upwd).count()
    user=User.objects.get(uname=uname, upwd=upwd)
    if count == 1:
        request.session['uname'] = uname
        request.session.set_expiry(600)
        return render(request,'index.html',{'user':user})
    else:
        return HttpResponse('登录失败！')

def person_view(request):
    return render(request, 'person.html')


def showall_view(request):
    return render(request, 'allbook.html')


def borrow_view(request):
    return render(request, 'borrow.html')


def contact_view(request):
    return render(request,'contact.html')


def login_view(request):
    if request.method == 'GET':
        return render(request,'login.html')



def register_view(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        #接收数据
        uname = request.POST.get('username','')
        upwd=request.POST.get('password','')
        # print uname,upwd
        insertUser(uname,upwd)
        return HttpResponseRedirect('/login/')

    return HttpResponse('注册失败')
def insertUser(uname,upwd):
    try:
        user = User.objects.get(uname=uname, upwd=upwd)
    except User.DoesNotExist:
        user = User.objects.create(uname=uname,upwd=upwd)