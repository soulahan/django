from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
# Create your views here.



def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.session.get('is_login',None):  # 不允许重复登录
        return redirect('/index/')
    request.session.flush()
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            message = '请检查填写的内容！'
            try:
                user = models.User.objects.get(name=username)
                message = user
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return render(request,'/login/')