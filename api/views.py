from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from api import serialize
from api.serialize import PackagesSerialize, UserSerializer 
from mytraveladmin.models import Categories, Packages

# from base.models import Item

@api_view(['GET'])
def index(request):
    return Response({'message': 'Hello World!'})

@api_view(['POST'])
def admin_sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        User.objects.create_user(username=username, password=password)
        return Response("User created successfully", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def admin_sign_in(request):
     if request.method == "POST":
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username,password=password)
      print("sdfvgbndsfg",user)
      if user:
        print("yyy",user)
        user = user.objects.get_or_create(user=user)
        return Response('user suecc')
      else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def admin_update(request, id):
    try:
        package = Packages.objects.get(id=id)
    except Packages.DoesNotExist:
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PackagesSerialize(package, data=request.data, partial=True)  

    if serializer.is_valid():
        serializer.save()
        return Response("Update successful", status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def admin_edit(request):
    s = serialize.PackagesSerialize(data=request.data)
    if s.is_valid():
        s.save()
    else:
        return Response(s.errors)
    return Response("data Added Suceesully")

@api_view(['POST'])
def admin_form(request):
    if request.method == 'POST':
      seri = serialize.CategoriesSerialize(data=request.data)
      if seri.is_valid(): 
         seri.save()
      else:
         print(seri.errors)
    return Response('Data added successfully')


@api_view(['POST'])
def additem(request):
    s = serialize.CategoriesSerialize(data=request.data)
    if s.is_valid():
        s.save()
    else:
        return Response(s.errors)
    return Response("data Added Suceesully")

@api_view(['POST'])
def deleteitem(request,id):
    data = Categories.objects.get(id=id)
    data.delete()
    return Response("data deleted successfully")
