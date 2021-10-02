from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User,Group
from datetime import datetime
from .serializer import GroupSerializer,UserSerializer,LanguageConverterSerializer
from ..models import NewUser,LanguageConvert
from libretranslatepy import LibreTranslateAPI
from validate_email import validate_email

@api_view(['GET'])
def test_server(request):
    if request.method=='GET':
        date =datetime.now().strftime("%d/%M/%Y")
        message='API Server is live '
        return Response(data=message+date,status=status.HTTP_200_OK)
  
@api_view(['GET','POST'])
def group(request):
    if request.method=='GET':
        response=Group.objects.all()
        serializer=GroupSerializer(response,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def user(request):
    if request.method=='GET':
        response=NewUser.objects.all()
        serializer=UserSerializer(response,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def languageconvert(request):
    if request.method=='GET':
        response=LanguageConvert.objects.all()
        serializer=LanguageConverterSerializer(response,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        data=request.data
        user_id=data['user']
        user=NewUser.objects.get(email=user_id)
        usergroup=user.group
        input_text=data['input_text']
        input_lan=data['input_lan']
        output_lan=data['output_lan']
        lt = LibreTranslateAPI("https://translate.astian.org/")
       
        if str(usergroup) == 'emailuser':
            data['is_valid_email']=2 if  validate_email(
            email_address=data['email'],
            check_format=True,
            check_blacklist=True,
            check_dns=True,
            dns_timeout=10,
            check_smtp=True,
            smtp_timeout=10,
            smtp_helo_host='my.host.name',
            smtp_from_address='my@from.addr.ess',
            smtp_skip_tls=False,
            smtp_tls_context=None,
            smtp_debug=False) else 3
            data['output_text']='null'
        elif str(usergroup) == 'translateuser':
            data['is_valid_email']=1
            data['output_text']=lt.translate(input_text, input_lan, output_lan)
        else:
            data['is_valid_email']==2 if validate_email(
            email_address=data['email'],
            check_format=True,
            check_blacklist=True,
            check_dns=True,
            dns_timeout=10,
            check_smtp=True,
            smtp_timeout=10,
            smtp_helo_host='my.host.name',
            smtp_from_address='my@from.addr.ess',
            smtp_skip_tls=False,
            smtp_tls_context=None,
            smtp_debug=False) else 2
            data['output_text']=lt.translate(input_text, input_lan, output_lan)

        serializer=LanguageConverterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

