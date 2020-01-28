from django.shortcuts import render
from django.http import HttpResponse

def about(request):
	return HttpResponse("hello")

def index(request):
	return HttpResponse("hello")
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context=context_dict)