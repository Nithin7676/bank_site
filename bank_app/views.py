from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *



# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login_page.html')

def registration_page(request):
    return render(request,'registration_page.html')

def save_registration(request):
    if request.method== 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        confirm= request.POST.get('confirm')


        if password==confirm:
            var = tbl_registraion()
            var.username = username
            var.password = password
            var.confirm = confirm
            var.save()
            return redirect('/login_page/')

        else:
            messages.error(request,"ReEnter Password")
            return redirect('/registration_page/')

def user_login_check(request):
    if request.method== 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        if (tbl_registraion.objects.filter(username=username, password=password)).exists():
            return redirect('/user_home/')
        else:
            return HttpResponse('wrong password')

def user_home(request):
    return render(request, 'user_home.html')

def application_form(request):
    return render(request, 'application_form.html')


def sub_area_view(request):
    district = request.GET.get("district")
    print(district)
    return render(request,"sub_area_view.html",{"district":district})

def save_application(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        dob= request.POST.get('dob')
        age= request.POST.get('age')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        district= request.POST.get('district')
        account= request.POST.get('account')
        debit= request.POST.get('debit')
        credit= request.POST.get('credit')
        cheque= request.POST.get('cheque')

        var= tbl_application()
        var.name=name
        var.dob=dob
        var.age=age
        var.gender=gender
        var.address=address
        var.phone=phone
        var.email=email
        var.district=district
        var.account=account
        var.debit=debit
        var.credit=credit
        var.cheque=cheque
        var.save()

        return redirect('/success_page/')

def success_page(request):
    return render(request, 'success_page.html')