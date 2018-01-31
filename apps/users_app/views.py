from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def main(request):
    return render(request, "users_app/index.html")

def info(request):
   Users.objects.all()
   Users.objects.last()
   Users.objects.create(first_name="John", last_name="Smith", email="johnsmith@gmail.com", age=30)
   Users.objects.first()
   Users.objects.order_by("-first_name")
   last_name = Users.objects.get(id=3)
   last_name.last_name = "asdf"
   last_name.save()
   delete = Users.objects.get(id=4)
   delete.delete()
return redirect("/")


   
