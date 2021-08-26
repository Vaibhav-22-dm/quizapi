from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from  .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'/question-list',
        'Test':'/test-list',
        'Token':'/token',
        'Register':'/register',
        'Student':'/student',
    }

    return Response(api_urls)

@api_view(['GET'])
def questionList(request, pk):
    test = Test.objects.get(id=pk)
    questions = Question.objects.filter(test=test)
    serializer = QuestionSerializer(questions, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def testList(request):
    tests = Test.objects.all()
    serializer = TestSerializer(tests, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def token(request):
    print(request.data)
    user = authenticate(request, username=request.data['username'], password=request.data['password'])
    # user = User.objects.get(username=request.data['username'])
    if user is not None:
        content = {
            'username': str(user.username),
            'token': str(Token.objects.get(user=user)),
        }
        return Response(content)
    else:
        content = {
            'message': "No such Users exist"
        }
        return Response(content)

@api_view(['POST'])
def register(request):
    username = request.data['username']
    email = request.data['email'] 
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    password1 = request.data['password1']
    password2 = request.data['password2']
    college = request.data['college']
    course = request.data['course']
    department = request.data['department']
    roll = request.data['roll']

    user = User(username=username, first_name=first_name, last_name=last_name, email=email)
    user.set_password(password1)
    print(user)
    user.save()
    student = Student(user=user, college=college, department=department, course=course, roll=roll)
    student.save()

    token = Token.objects.create(user=user)
    token.save()

    return Response({'message':'You have registered Successfuly!'})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def student(request, token):
    token = Token.objects.get(key=token)
    student = Student.objects.get(user=token.user)
    print(student.user.first_name)
    content = {
        'username':str(token.user.username),
        'first_name':str(token.user.first_name),
        'last_name':str(token.user.last_name),
        'email':str(token.user.email),
        'college':str(student.college),
        'department':str(student.department),
        'course':str(student.course),
        'roll':str(student.roll),
    }
    return Response(content)
    
