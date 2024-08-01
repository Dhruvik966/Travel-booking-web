from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from prompt_toolkit import HTML
from traveluser.models import Packages
from traveluser import models
from mytraveladmin.models import Packages
from traveluser.models import Confirm_booking
from traveluser.forms import ConfirmForm
from traveluser.forms import PaymentForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django import forms
from django.template.loader import render_to_string
from django.core.paginator import Paginator
# Create your views here.

def logoutview(request):
    logout(request)
    return redirect('user_index')

def user_indexview(request):
    package = Packages.objects.all()
    context = {'package':package}
    return render(request,'traveluser/index.html',context)

def user_about(request):
    return render(request,'traveluser/about.html')

def user_service(request):
    return render(request,'traveluser/service.html')

def user_contact(request):
    return render(request,'traveluser/contact.html')

def user_destination(request):
    return render(request,'traveluser/destination.html')

def user_packages(request):
    package = Packages.objects.all()
    context = {'package':package}
    return render(request,'traveluser/package.html',context)

def user_booking(request):
    data = models.Confirm_booking.objects.filter(user=request.user).filter(is_booked=True)
    paginator = Paginator(data, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'traveluser/booking.html', context)


def user_testimonial(request):
    return render(request,'traveluser/testimonial.html')

def user_team(request):
    return render(request,'traveluser/team.html')
    
def package_detail(request,id):
    data = models.Packages.objects.get(id=id)
    context = {'data':data}
    return render(request,'traveluser/package_detail.html',context)

def book_packages(request,id):
    pack = models.Packages.objects.get(id=id)
    if request.method == 'POST':
         form = ConfirmForm(request.POST)
         if form.is_valid():
            obj = form.save(commit=False) 
            obj.user = request.user
            obj.package = pack
            obj.save()  
            return redirect(user_payment,id) 
         else:
             print(form.errors)
    else:
         form = Confirm_booking()

    return render(request,'traveluser/book_packages.html',{'form': form})

def bookingdetail(request,id):
    data = Confirm_booking.objects.all()
    context = {'data' : data}
    return render(request,'traveluser/bookingdetail.html')

def user_register(request):
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
                return redirect(loginview)
         else:
             return HttpResponse("Password Does not match")
         
    return render(request,'traveluser/register.html')

def loginview(request):
     if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect(user_indexview)
      else:
         return HttpResponse("User not found")
         
     return render(request,'traveluser/login.html')

def user_payment(request, id):
    package = get_object_or_404(Packages, id=id)
    confirm = Confirm_booking.objects.filter(user=request.user,package=id).last()
    if request.method == 'POST':
        # card_name = request.POST.get('card_name')
        # card_number = request.POST.get('card_number') 
        # date = request.POST.get('date') 
        # Month = request.POST.get('Month') 
        # cvv = request.POST.get('cvv') 
        # bank = request.POST.get('bank') 
        # print(card_name)
        # print(card_number)
        # print(date)
        # print(Month)
        # print(cvv)
        # print(bank)
        form = PaymentForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)   
            transaction.user = request.user
            transaction.package = package
            transaction.save()
            confirm.is_booked = True
            confirm.transaction = transaction
            confirm.save()
            return redirect(confirmed,id)
        else:
            print(form.errors)
    else:
        form = PaymentForm()
    context = {'package': package, 'form': form}
    return render(request, 'traveluser/payment.html', context)

def confirmed(request,id):
    data = models.Confirm_booking.objects.get(id=id)
    context = {'data':data}
    return render(request,'traveluser/confirmed.html',context)


# def generate_pdf(request):
#     user = request.user
#     bookings = Confirm_booking.objects.filter(user=user)
#     html_string = render_to_string('traveluser/user_booking.html', {'bookings': bookings})
#     html = HTML(string=html_string)
#     pdf = html.write_pdf()

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="booking_confirmation.pdf"'
#     return response(request,'traveluser/generate_pdf.html')

def packagesearch(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        print(search)
        data = models.Packages.objects.filter(title__icontains=search)
        print(data)
    else:
        data = models.Packages.objects.all()

    context = {'package':data}
    return render(request,'traveluser/package.html',context)