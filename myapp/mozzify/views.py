#create your views here
from django.shortcuts import render

from django.http import HttpResponse
from . models import ToDoList,Item

def index(response,id):
    ls = ToDoList.objects.get(id=id)
    Item = ls.Item_set.get(id=1)
    return HttpResponse('<h1>%s</h1>' %ls.name)