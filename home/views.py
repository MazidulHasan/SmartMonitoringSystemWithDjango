from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples =[
        {'name' : 'Name1', 'age': 10},
        {'name' : 'Name2', 'age': 20},
        {'name' : 'Name3', 'age': 30},
        {'name' : 'Name4', 'age': 40},
        {'name' : 'Name5', 'age': 50},
        {'name' : 'Name6', 'age': 60},
        {'name' : 'Name7', 'age': 70}
    ]
    return render(request, "home/index.html", context={'peoples':peoples})

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def success_page(request):
    return HttpResponse("Success page")