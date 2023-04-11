from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import History
from user.models import User
import datetime
@api_view(['POST'])
def create_history(request,id_user):
    data=request.GET 
    hist=History(ph=data.get('ph'),turbidity=data.get('turbidity'),tds=data.get('tds'),result=data.get('result'),time_posted=datetime.datetime.now(),user=User.objects.get(id_user=id_user))
    if data.get('ph')!=None and data.get('tds')!=None and data.get('turbidity')!= None and data.get('result') != None:
        hist.save()
        return Response({"data":"No content","message":"Successfully","code":status.HTTP_200_OK},status=status.HTTP_200_OK)
    return Response({"data":"No content","message":"Failded","code":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getHistory(request,id_user):
    listHist=History.objects.filter(user_id=id_user)
    data=[]
    for hist in listHist:
        data.append({"id":hist.id_history,"ph":hist.ph,"turbidity":hist.turbidity,"tds":hist.tds,"result":hist.result,"time_posted":hist.time_posted,"user_id":id_user})
    return Response({"data":data,"message":"No content","code":status.HTTP_200_OK},status=status.HTTP_200_OK)

@api_view(['DELETE'])
def removeHistory(request,id):
    hist=History.objects.filter(id_history=id)
    if hist:
        hist.delete()
        return Response({"data":"No content","message":"Successfully","code":status.HTTP_202_ACCEPTED},status=status.HTTP_202_ACCEPTED)
    return Response({"data":"No content","message":"Failded","code":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)