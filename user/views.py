from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
# Create your views here.

@api_view(['POST'])
def register_user(request):
    data=request.GET 
    name=data.get('fullname')
    username=data.get('username')
    password1=data.get('password1')
    password2=data.get('password2')
    for u in User.objects.all():
        id=u.id_user
    user=User(id_user=id+1,fullname=name,username=username,password=password1)
    if password1==password2:
        listU=User.objects.all()
        for u in listU:
            if u.fullname==name and u.username==username and u.password==password1:
                return Response({"data":"No content","message":"Invalid","code":status.HTTP_204_NO_CONTENT},status=status.HTTP_204_NO_CONTENT)
        user.save()
        return Response({"data":"No content","message":"Success","code":status.HTTP_200_OK},status=status.HTTP_200_OK)
    else:
        return Response({"data":"No content","message":"Error Registration","code":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    data=request.GET 
    uname=data.get('username')
    passw=data.get('password')
    listU=User.objects.all()
    for u in listU:
        if u.username==uname and u.password==passw:
            data=[{"id":u.id_user}]
            return Response({"data":(str)(u.id_user),"message":"Login Success","code":status.HTTP_200_OK},status=status.HTTP_200_OK)
    return Response({"data":None,"message":"Login Failed","code":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_id(request,id):
    user = User.objects.get(id_user=id)
    data=[{"id":user.id_user,"fullname":user.fullname,"avatar":user.avatar,"username":user.username,"password":user.password}]
    return Response({"data":data,"message":"No content","code":status.HTTP_200_OK},status=status.HTTP_200_OK)

@api_view(['PUT'])
def set_user(request, id_user):
    user=User.objects.get(id_user=id_user)
    if user:
        if request.GET.get('avatar'):
            user.set_avatar(request.GET.get('avatar'))
        if request.GET.get('fullname'):    
            user.set_fullname(request.GET.get('fullname'))
        
        user.save()
        
        return Response({"data":"No content","message":"Success","code":status.HTTP_200_OK},status=status.HTTP_200_OK)
    return Response({"data":"No content","message":"Failded","code":status.HTTP_204_NO_CONTENT},status=status.HTTP_204_NO_CONTENT)
        
    
    
    