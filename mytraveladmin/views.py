from audioop import reverse
from importlib.resources import Package
from multiprocessing import context
from django.shortcuts import redirect, render,HttpResponse
from mytraveladmin import models
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from mytraveladmin import forms


def admin_logoutview(request):
    logout(request)
    return redirect(admin_sign_in)

def admin_indexview(request):
    if request.user.is_authenticated:
        total_packages = models.Packages.objects.all().count()
        context = {'totalpackages': total_packages,}
        return render(request, 'mytraveladmin/index.html', context) 
    else:
       return redirect(admin_sign_in)
    
def admin_dashview(request):
    return render(request,"mytraveladmin/dashboard.html")


def admin_sign_in(request):
     if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect(admin_indexview)
      else:
         return HttpResponse("User not found")
   
     return render(request,'mytraveladmin/sign_in.html')

def admin_sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            try:
                User.objects.get(username=username)
                return HttpResponse("Username already exists")
            except:
                User.objects.create_user(username=username,password=password)
                return redirect(admin_sign_in)
        else:
          return HttpResponse("Password Does not match")
    
    return render(request,'mytraveladmin/sign_up.html')

def admin_form(request):
    if request.method == 'POST':
      form = forms.CategoriesForm(request.POST)
      if form.is_valid():
         obj = form.save(commit=False)
         obj.user = request.user
         obj.save()
         return redirect(admin_tables)
      else:
         print("error")
         print(form.errors)
    return render(request,'mytraveladmin/form.html')



def admin_delete(request,id):
    data = models.Categories.objects.get(id=id)
    data.delete()
    return redirect(admin_tables)


def admin_edit(request,id):
    data = models.Categories.objects.get(id=id)
    context = {'data':data}
    return render(request,'mytraveladmin/edittask.html',context=context)

def admin_update(request,id):
    data = models.Categories.objects.get(id=id)
    if request.method == "POST":
       form = forms.CategoriesForm(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect(admin_tables)
       else:
          print("error")
          print(form.errors)

    return render(request,'mytraveladmin/edittask.html')


def admin_tables(request):
    data = models.Categories.objects.all()
    context = {'data':data}
    return render(request,'mytraveladmin/tables.html',context=context)

# pakagesforms

def admin_tables1(request):
    data = models.Packages.objects.all()
    context = {'data':data}
    return render(request,'mytraveladmin/tables1.html',context=context)


def admin_form1(request):
    if request.method == 'POST':
      form = forms.PackagesForm(request.POST,request.FILES)
      if form.is_valid():
         obj = form.save(commit=False)
         obj.user = request.user
         obj.save()
         return redirect(admin_tables1)
      else:
         print("error")
         print(form.errors)
    return render(request,'mytraveladmin/form1.html')

def admin_packagesdelete(request,id):
    data = models.Packages.objects.get(id=id)
    data.delete()
    return redirect(admin_tables1)


def admin_packagesedit(request,id):
    data = models.Packages.objects.get(id=id)
    context = {'data':data}
    return render(request,'mytraveladmin/edittaskpakages.html',context=context)

def admin_packagesupdate(request,id):
    data = models.Packages.objects.get(id=id)
    if request.method == "POST":
       form = forms.PackagesForm(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect(admin_tables1)
       else:
          print("error")
          print(form.errors)
          return redirect(admin_tables1)


    return render(request,'mytraveladmin/edittaskpakages.html')