from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('add',views.add, name="add"),
    path('subtract',views.subtract, name="subtract"),
    path('multiply',views.multiply, name="multiply"),
    path('divide',views.divide, name="divide"),
    path('dictionary',views.dictionary, name="dictionary"),
]
