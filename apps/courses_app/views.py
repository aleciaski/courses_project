from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from  .models import Course
# the index function is called when root is visited
def index(request):
	print("i made it to the INDEX!")
	context={
		"courses" : Course.objects.all()
	}
	return render(request,"courses_app/index.html", context)

def new(request):
	print("yay!!!!!!!!!!!!!!! i made it to new!!!!!!")
	return render(request,"courses_app/index.html")

def create(request):
	print("Whoa!!!!!!!! made it to CREATE!!!!!!!!!!!!!!!!!!!!")
	Course.objects.create(
		name=request.POST['name'], 
		desc=request.POST['desc'])
	return render(request,"courses_app/index.html")

def destroy(request, id):
	print("DDDDDDDDDEEEEEEEEEEEESSSSSSSSSSSTTTTTTTTTTTTRRRRRRRRRRROOOOOOOOOOOOOOYYYYYYYYY")
	Course.objects.get(id=id).delete()
	return redirect("/")
