from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="apiOverView"),
    path('questionList/<str:pk>', views.questionList, name="questionList"),
    path('testList/', views.testList, name="testList"),
    path('auth/', views.token, name="token"),
    path('register/', views.register, name="register"),
    path('student/<slug:token>', views.student, name="student"),
]